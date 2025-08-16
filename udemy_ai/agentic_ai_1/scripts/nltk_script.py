import nltk

# Natural Language Toolkit

# nltk.download("punkt")
# nltk.download("punkt_tab")
# nltk.download('averaged_perceptron_tagger_eng')

sentence = """At eight o'clock on Thursday morning
... Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)
print(tokens)
tagged = nltk.pos_tag(tokens)
print(tagged[0:6])

# 