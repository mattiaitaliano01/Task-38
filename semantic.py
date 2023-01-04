import spacy

nlp = spacy.load("en_core_web_md")

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp("cat apple monkey banana")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

'''
I find very interesting the results of the similarities between these given words:

Speaking of cats and monkeys, they are both animals, while banana's a food that it's mostly related to monkeys as they enjoy eating them. 

These are the reasons why I appreciate the results that relate together animals but keep in consideration also the interraction between the animal itself and the food. In fact, even if the apple is a food that both of them could eat, the banana is definetely more bonded to monkeys than cats (or comparing monkey and apples).

An example might be about dogs, pandas, bamboo and bonsai.
The first two are animals, while the seconds are plants. However, analyzing the similarity between panda and bamboo, they are related cause often pandas eat bamboo. 

'''

sentence_to_compare = "Why is my cat on the car"

sentences = [
    "where did my dog go",
    "hello, there's my car",
    "I've lost my car in my car",
    "I'd like my boat",
    "I will name my dog Diana"
]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similiarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similiarity)

# |==========||NOTES ABOUT 2ND POINT OF THE FIRST TASK==========||

'''
By running the examples file with 'en_core_web_sm' instead of the 'en_core_web_md' I've found out that the first one have no word vectors loaded, wich give the following error:

UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.

In fact, if we compare the results of comparison, we can easily notice how the similarities are way less in en_core_web_sm model than in en_core_web_md one.

'''