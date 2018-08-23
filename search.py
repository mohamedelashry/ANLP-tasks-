#from __future__ import unicode_literals
import nltk
import pyaramorph as par
import naftawayh.wordtag as wordtag
from tashaphyne.stemming import ArabicLightStemmer
from nltk.stem.isri import ISRIStemmer
from nltk import CFG
from nltk.parse import *

text = 'كتب محمد كتاب عن المكتبات التى تمتلاء بالكتب والمكاتب'
Word = 'كتب'
#  بقطع الجمله لكلام
tokens = nltk.word_tokenize(text)
# الجرامر اللى هعمل بارص بيه
grm = CFG.fromstring("""
                S -> VP
                VP -> V NP
                NP -> N|N NP
                N -> 'السيارة'|'البيضاء'
                V ->'اركب'
                """)
# الجمله اللى هعملها بارص
sent = 'اركب السيارة البيضاء'.split()


# get the root of word
def _getstem(_word):
    st = ISRIStemmer()
    return st.stem(_word)
# get the translation of word
def _GetGloss(_word):
    analizer = par.Analyzer()
    analized = analizer.analyze_text(_word)
    return analized
# get the tag of word
def _PosTag (_word):
    tagger = wordtag.WordTagger();
    if tagger.is_noun(_word):
      res=" is noun' "+_word
    elif  tagger.is_verb(_word):
       res=" is verb' "+_word
    elif tagger.is_stopword(_word):
       res=" is stopword'"+_word
    return res

def Top_downParsing():
    rd = RecursiveDescentParser(grm)
    for w in rd.parse(sent):
        print(w)
def Bottom_upParsing():
    sr = ShiftReduceParser(grm)
    for w in sr.parse(sent):
        print(w)
def Top_downWithBottom_upFiltering():
    lcp = LeftCornerChartParser(grm)
    for w in lcp.parse(sent):
        print(w)
def EarleyParser():
    ecp = EarleyChartParser(grm)
    for w in ecp.parse(sent):
        print(w)




for tok in tokens :
    # check the root of each token in text with root of word
  if _getstem(tok) == _getstem(Word):
       print(tok)
       print(_PosTag(tok))


Top_downParsing()
Bottom_upParsing()
Top_downWithBottom_upFiltering()
EarleyParser()
