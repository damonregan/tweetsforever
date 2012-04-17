import sys
import simplejson
from HTMLParser import HTMLParser
import ConfigParser

sys.path.append('./lib')

#
# A simple Evernote API demo application that authenticates with the
# Evernote web service, lists all notebooks in the user's account,
# and creates a simple test note in the default notebook.
#
# Before running this sample, you must change the API consumer key
# and consumer secret to the values that you received from Evernote.
#
# To run (Unix):
#   export PYTHONPATH=../lib; python EDAMTest.py myuser mypass
#

import hashlib
import binascii
import time
import thrift.protocol.TBinaryProtocol as TBinaryProtocol
import thrift.transport.THttpClient as THttpClient
import evernote.edam.userstore.UserStore as UserStore
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.notestore.NoteStore as NoteStore
import evernote.edam.type.ttypes as Types
import evernote.edam.error.ttypes as Errors

config = ConfigParser.RawConfigParser()

# You need to change this to point to your oauth.cfg
# containing your oauth credentials
config.read('../oauth.private.cfg')

username = config.get("evernote", "username")
password = config.get("evernote", "password")

consumerKey = config.get("evernote", "consumer-key")
consumerSecret = config.get("evernote", "consumer-secret")

evernoteHost = "sandbox.evernote.com"
userStoreUri = "https://" + evernoteHost + "/edam/user"

userStoreHttpClient = THttpClient.THttpClient(userStoreUri)
userStoreProtocol = TBinaryProtocol.TBinaryProtocol(userStoreHttpClient)
userStore = UserStore.Client(userStoreProtocol)

versionOK = userStore.checkVersion("Python EDAMTest",
                                   UserStoreConstants.EDAM_VERSION_MAJOR,
                                   UserStoreConstants.EDAM_VERSION_MINOR)

print "Is my EDAM protocol version up to date? ", str(versionOK)
print ""
if not versionOK:
    exit(1)

# Authenticate the user
try :
    authResult = userStore.authenticate(username, password,
                                        consumerKey, consumerSecret)
except Errors.EDAMUserException as e:
    # See http://www.evernote.com/about/developer/api/ref/UserStore.html#Fn_UserStore_authenticate
    parameter = e.parameter
    errorCode = e.errorCode
    errorText = Errors.EDAMErrorCode.tostring(errorCode)
    
    print "Authentication failed (parameter: " + parameter + " errorCode: " + errorText + ")"
    
    if errorCode == Errors.EDAMErrorCode.INVALID_AUTH:
        if parameter == "consumerKey":
            if consumerKey == "en-edamtest":
                print "You must replace the variables consumerKey and consumerSecret with the values you received from Evernote."
            else:
                print "Your consumer key was not accepted by", evernoteHost
                print "This sample client application requires a client API key. If you requested a web service API key, you must authenticate using OAuth."
            print "If you do not have an API Key from Evernote, you can request one from http://dev.evernote.com/documentation/cloud/"
        elif parameter == "username":
            print "You must authenticate using a username and password from", evernoteHost
            if evernoteHost != "www.evernote.com":
                print "Note that your production Evernote account will not work on", evernoteHost
                print "You must register for a separate test account at https://" + evernoteHost + "/Registration.action"
        elif parameter == "password":
            print "The password that you entered is incorrect"

    print ""
    exit(1)

user = authResult.user
authToken = authResult.authenticationToken
print "Authentication was successful for ", user.username
print "Authentication token = ", authToken

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ' '.join(self.fed)

noteStoreUrl = "https://sandbox.evernote.com/edam/note/" + user.shardId
print noteStoreUrl

noteStoreHttpClient = THttpClient.THttpClient(noteStoreUrl)
noteStoreProtocol = TBinaryProtocol.TBinaryProtocol(noteStoreHttpClient)
noteStore = NoteStore.Client(noteStoreProtocol)

noteFilter = NoteStore.NoteFilter()

notes = noteStore.findNotes(authToken, noteFilter, 0, 10)
data = []

for noteShell in notes.notes:
    note = noteStore.getNote(authToken, noteShell.guid, True)
    s = MLStripper()
    s.feed(note.content)
    data.append(dict(title=note.title, content=s.get_data()))

f = open('notes_workfile', 'w')

f.write(simplejson.dumps(data, indent=4, sort_keys=True))

f.close()