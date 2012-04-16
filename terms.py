import simplejson

# Load note data

notes_file = open('notes_workfile', 'r')

notes = simplejson.loads(notes_file.read())

# Load tweet data

tweets_file = open('tweet_workfile', 'r')

tweets = simplejson.loads(tweets_file.read())

tweets_file.close()
notes_file.close()

# Get key terms for notes

from topia.termextract import extract
extractor = extract.TermExtractor()

for note in notes:
    note['key_terms'] = [item[0] for item in extractor(note['content'])]

# Get key terms for tweets

extractor = extract.TermExtractor()

for tweet in tweets:
    tweet['key_terms'] = [item[0] for item in extractor(tweet['text'] + " " + tweet['user'])]

# Update the tweets and notes files

tweets_file = open('tweet_workfile', 'w')
notes_file = open('notes_workfile', 'w')

tweets_file.write(simplejson.dumps(tweets, indent=4, sort_keys=True))
notes_file.write(simplejson.dumps(notes, indent=4, sort_keys=True))

tweets_file.close()
notes_file.close()

# Look for matches

for note in notes:
    for tweet in tweets:
        for note_term in note['key_terms']:
            for tweet_term in tweet['key_terms']:
                print "Note term: " + note_term + ", Tweet term: " + tweet_term
                if note_term in tweet_term:
                    print "MATCH"