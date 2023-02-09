import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Note 1: Interestingly, to 1 s.f., spacy rates the similarity between Monkey and Cat the highest, at 0.6, followed by Monkey and Banana at 0.4,
# and puts the similarity between Cat and Banana the lowest, at 0.2. This makes sense, because monkeys and cats both represent animals,
# bananas are something which monkeys are commonly believed to eat, whilst cats and monkeys are who different types of things, and there is
# no commonly recognised association between the two of them. So the similarity ratings given by SpaCy in this case seem to be relatively good!

# Note 2: When I ran the example.py file, with the language model 'en_core_web_sm' instead of 'en_core_web_md', I noticed that the similarity
# scores decreased, apparently for all comparisons made. This will be because some things have been left out of this model to allow it to
# be smaller.