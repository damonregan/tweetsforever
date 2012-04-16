
text ='''
... Police shut Palestinian theatre in Jerusalem.
...
... Israeli police have shut down a Palestinian theatre in East Jerusalem.
...
... The action, on Thursday, prevented the closing event of an international
... literature festival from taking place.
...
... Police said they were acting on a court order, issued after intelligence
... indicated that the Palestinian Authority was involved in the event.
...
... Israel has occupied East Jerusalem since 1967 and has annexed the
... area. This is not recognised by the international community.
...
... The British consul-general in Jerusalem , Richard Makepeace, was
... attending the event.
...
... "I think all lovers of literature would regard this as a very
... regrettable moment and regrettable decision," he added.
...
... Mr Makepeace said the festival's closing event would be reorganised to
... take place at the British Council in Jerusalem.
...
... The Israeli authorities often take action against events in East
... Jerusalem they see as connected to the Palestinian Authority.
...
... Saturday's opening event at the same theatre was also shut down.
...
... A police notice said the closure was on the orders of Israel's internal
... security minister on the grounds of a breach of interim peace accords
... from the 1990s.
...
... These laid the framework for talks on establishing a Palestinian state
... alongside Israel, but left the status of Jerusalem to be determined by
... further negotiation.
...
... Israel has annexed East Jerusalem and declares it part of its eternal
... capital.
...
... Palestinians hope to establish their capital in the area.
... '''

from topia.termextract import extract
extractor = extract.TermExtractor()

extractList = extractor(text)

termList = [item[0] for item in extractList]

print termList










