import spacy
from spacy.matcher import Matcher


nlp = spacy.load("de_core_news_sm")

# matcher initialisieren (dcm ... date, currency, money)
dcm_matcher = Matcher(nlp.vocab)

# 12. Aug 2020 mit verschiedenen Monatsnamen und Zahlenlängen
pattern_date_word1 = [{'IS_DIGIT': True, 'LENGTH': 2}, {'IS_PUNCT': True, 'OP': "?"}, {'LOWER': {'IN':["jan", "januar", "februar", "feb", "mar", "mär", "märz", "march", "february", "january", "apr", "april", "may", "mai", "jun", "juni", "june", "jul", "juli", "july", "aug", "august", "sep", "september", "oct", "okt", "october", "nov", "november", "dez", "dec", "dezember", "december"]}}, {'IS_DIGIT': True, 'LENGTH': 2, 'OP': "?"}, {'IS_DIGIT': True, 'LENGTH': 4, 'OP': "?"}]

# 12.04.2020 als gemeinsames Token mit verschiedenen Zahlenlängen und .,/ als Trennzeichen
pattern_date1 = [{'SHAPE': 'dd.dd.dddd'}]
pattern_date2 = [{'SHAPE': 'dd.dd.dd'}]
pattern_date3 = [{'SHAPE': 'dd,dd,dddd'}]
pattern_date4 = [{'SHAPE': 'dd,dd,dd'}]
pattern_date5 = [{'SHAPE': 'dd/dd/dddd'}]
pattern_date6 = [{'SHAPE': 'dd/dd/dd'}]
pattern_date7 = [{'SHAPE': 'dd.d.dddd'}]
pattern_date8 = [{'SHAPE': 'dd.d.dd'}]
pattern_date9 = [{'SHAPE': 'dd,d,dddd'}]
pattern_date10 = [{'SHAPE': 'dd,d,dd'}]
pattern_date11 = [{'SHAPE': 'dd/d/dd'}]
pattern_date12 = [{'SHAPE': 'd/d/dddd'}]
pattern_date13 = [{'SHAPE': 'd.dd.dddd'}]
pattern_date14 = [{'SHAPE': 'd.dd.dd'}]
pattern_date15 = [{'SHAPE': 'd,dd,dddd'}]
pattern_date16 = [{'SHAPE': 'd,dd,dd'}]
pattern_date17 = [{'SHAPE': 'd/dd/dd'}]
pattern_date18 = [{'SHAPE': 'd/dd/dddd'}]
pattern_date19 = [{'SHAPE': 'd.d.dddd'}]
pattern_date20 = [{'SHAPE': 'd.d.dd'}]
pattern_date21 = [{'SHAPE': 'd,d,dddd'}]
pattern_date22 = [{'SHAPE': 'd,d,dd'}]
pattern_date23 = [{'SHAPE': 'd/d/dd'}]
pattern_date24 = [{'SHAPE': 'd/d/dddd'}]


# 12.04.2020 mit allen möglichen Punctuations und Zahlenlänge als getrennte Tokens
pattern_date_general1 = [{'IS_DIGIT': True, 'LENGTH': {'IN': [1, 2]}}, {'IS_PUNCT': True, 'OP': "?"}, {'IS_DIGIT': True, 'LENGTH': {'IN': [1, 2]}}, {'IS_PUNCT': True, 'OP': "?"}, {'IS_DIGIT': True, 'LENGTH': {'IN': [2, 4]}}]

#Währungssymbole
pattern_currency1 = [{'IS_CURRENCY': True}]
pattern_currency2 = [{'LOWER': {'IN': ["euro", "eur", "chf", "sfr"]}}]

# Geld in verschiedenen Formen und Tokenzusammensetzungen
# einzelnes Token
pattern_money1 = [{'SHAPE': 'd,dd'}]
pattern_money2 = [{'SHAPE': 'dd,dd'}]
pattern_money3 = [{'SHAPE': 'ddd,dd'}]
pattern_money4 = [{'SHAPE': 'dddd,dd'}]
pattern_money5 = [{'SHAPE': 'd.dd'}]
pattern_money6 = [{'SHAPE': 'dd.dd'}]
pattern_money7 = [{'SHAPE': 'ddd.dd'}]
pattern_money8 = [{'SHAPE': 'dddd.dd'}]
# 2 Token (Eurobetrag plus punctuation in einem Token oder punctuation und Centbetrag in einem Token)
pattern_money9 = [{'SHAPE': 'd,'}, {'IS_DIGIT': True, 'LENGTH': 2}]
pattern_money10 = [{'SHAPE': 'dd,'}, {'IS_DIGIT': True, 'LENGTH': 2}]
pattern_money11 = [{'SHAPE': 'ddd,'}, {'IS_DIGIT': True, 'LENGTH': 2}]
pattern_money12 = [{'SHAPE': 'dddd,'}, {'IS_DIGIT': True, 'LENGTH': 2}]
pattern_money13 = [{'SHAPE': 'd.'}, {'IS_DIGIT': True, 'LENGTH': 2}]
pattern_money14 = [{'SHAPE': 'dd.'}, {'IS_DIGIT': True, 'LENGTH': 2}]
pattern_money15 = [{'SHAPE': 'ddd.'}, {'IS_DIGIT': True, 'LENGTH': 2}]
pattern_money16 = [{'SHAPE': 'dddd.'}, {'IS_DIGIT': True, 'LENGTH': 2}]
pattern_money17 = [{'IS_DIGIT': True, 'LENGTH': {'IN': [1, 2, 3, 4]}}, {'SHAPE': ',dd'}]
pattern_money18 = [{'IS_DIGIT': True, 'LENGTH': {'IN': [1, 2, 3, 4]}}, {'SHAPE': '.dd'}]

# 3 Token
pattern_money19 = [{'IS_DIGIT': True}, {'IS_PUNCT': True}, {'IS_DIGIT': True, 'LENGTH': 2}]


# Verschiedene Labels zum Matcher hinzufügen
dcm_matcher.add("DATE", None, pattern_date1, pattern_date2, pattern_date3, pattern_date4, pattern_date5, pattern_date6, pattern_date7, pattern_date8, pattern_date8, pattern_date9, pattern_date10, pattern_date11, pattern_date12, pattern_date13, pattern_date14, pattern_date15, pattern_date16, pattern_date17, pattern_date18, pattern_date19, pattern_date20, pattern_date21, pattern_date22, pattern_date23, pattern_date24, pattern_date_word1)
dcm_matcher.add("GEN DATE", None, pattern_date_general1)
dcm_matcher.add("CURRENCY", None, pattern_currency1, pattern_currency2)
dcm_matcher.add("MONEY", None, pattern_money1, pattern_money2, pattern_money3, pattern_money4, pattern_money5, pattern_money6, pattern_money7, pattern_money8, pattern_money9, pattern_money10, pattern_money11, pattern_money12, pattern_money13, pattern_money14, pattern_money15, pattern_money16, pattern_money17, pattern_money18, pattern_money19)


test = "28-04-2019 28.05.2017 23 10 96 23 - 10-1999 € EUR CHF  28 AUG 2014 345 ,45" 

doc = nlp(test)
print([token.text for token in doc])

matches = dcm_matcher(doc)


for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]
    span = doc[start:end]
    print(string_id, span.text)