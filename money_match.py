from matplotlib import pyplot as plt
import numpy as np
import cv2
import spacy
from spacy.matcher import Matcher

nlp = spacy.load("de_core_news_sm")

matcher = Matcher(nlp.vocab)
pattern_money1 = [{'SHAPE': 'd,dd'}]
pattern_money2 = [{'SHAPE': 'dd,dd'}]
pattern_money3 = [{'SHAPE': 'ddd,dd'}]
pattern_money4 = [{'SHAPE': 'd.dd'}]
pattern_money5 = [{'SHAPE': 'dd.dd'}]
pattern_money6 = [{'SHAPE': 'ddd.dd'}]
pattern_money7 = [{'IS_DIGIT': True}, {'IS_PUNCT': True}, {'IS_DIGIT': True, 'LENGTH': 2}]
matcher.add("MONEY", None, pattern_money1, pattern_money2, pattern_money3, pattern_money4, pattern_money5, pattern_money6)
matcher.add("MONEY2", None, pattern_money7)




test = "214,87 3,80 34,87 23.80 3.80 123.45 9 56 567 56778 , 87" 

doc = nlp(test)

matches = matcher(doc)

print([token.text for token in doc])

for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]
    span = doc[start:end]
    print(string_id, span.text)