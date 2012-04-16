A project to explore python a little further while trying to find relevant tweets. Right now, the project is a set of individual experiments with APIs and packages of interest.

It uses the [Evernote Cloud API](http://dev.evernote.com/documentation/cloud/), [Twitter API](https://dev.twitter.com/docs) (not through a client library at this time), and the [topia.termextract](http://pypi.python.org/pypi/topia.termextract) python package.

NOTE: I made a couple of changes to the python Evernote library to get the sample application working.  Once I get a bit more confidence with the API I may consider filing a bug report. They may be issues with Thrift and not Evernote code.

The `EDAMErrorCode` enum wasn't fetching the string value of the enum for the error code text:

     errorText = Errors.EDAMErrorCode._VALUES_TO_NAMES[errorCode]
     AttributeError: type object 'EDAMErrorCode' has no attribute '_VALUES_TO_NAMES'

I modified the `EDAMErrorCode` class to include [enum tostring and fromstring methods](http://stackoverflow.com/questions/4472901/python-enum-class-with-tostring-fromstring/):

     class EDAMErrorCode(object):
       UNKNOWN = 1
       BAD_DATA_FORMAT = 2
       PERMISSION_DENIED = 3
       INTERNAL_ERROR = 4
       DATA_REQUIRED = 5
       LIMIT_REACHED = 6
       QUOTA_REACHED = 7
       INVALID_AUTH = 8
       AUTH_EXPIRED = 9
       DATA_CONFLICT = 10
       ENML_VALIDATION = 11
       SHARD_UNAVAILABLE = 12
       
       @classmethod
       def tostring(cls, val):
         for k,v in vars(cls).iteritems():
           if v == val:
             return k
       
       @classmethod
       def fromstring(cls, str):
         return getattr(cls, str.upper(), None)

and then then modified the errorText statement to be:

     errorText = Errors.EDAMErrorCode.tostring(errorCode)

The other issue I had was with `noteStoreUrl` -- authResult didn't seem to include it:

     noteStoreHttpClient = THttpClient.THttpClient(authResult.noteStoreUrl)
     AttributeError: 'AuthenticationResult' object has no attribute 'noteStoreUrl'

Based on the [evernote API documentation](http://dev.evernote.com/documentation/cloud/chapters/Testing.php), I constructed the noteStoreUrl:

     noteStoreUrl = "https://sandbox.evernote.com/edam/note/" + user.shardId
     noteStoreHttpClient = THttpClient.THttpClient(noteStoreUrl)