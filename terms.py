import simplejson
from topia.termextract import extract

# Load note data

notes_file = open('notes_workfile', 'r')

notes = simplejson.loads(notes_file.read())

# Load tweet data

tweets_file = open('tweet_workfile', 'r')

tweets = simplejson.loads(tweets_file.read())

tweets_file.close()
notes_file.close()

# Get key terms for notes

extractor = extract.TermExtractor()

all_notes = ""

for note in notes:
    all_notes.join(note['content'])

note_terms = [item[0] for item in extractor(all_notes)]

terms_file = open('terms_workfile', 'w')

terms_file.write(simplejson.dumps(note_terms))

# Get key terms for tweets

extractor = extract.TermExtractor()

def key_tweet_terms(tweet, user):
	keyterms = [user]
	for term in tweet.split():
		if "http://" in term:
			continue
		if "RT" in term:
			continue
		if len(term) < 4:
			continue
		keyterms.append(term)
	return keyterms

for tweet in tweets:
    tweet['key_terms'] = key_tweet_terms(tweet['text'], tweet['user'])

terms_file.write(simplejson.dumps(tweets, indent=4, sort_keys=True))

# Look for matches

for note_term in note_terms:
    for tweet in tweets:    
        for tweet_term in tweet['key_terms']:
            print "Note term: " + note_term + ", Tweet term: " + tweet_term
            if note_term in tweet_term:
                print "MATCH"

terms_file.close()