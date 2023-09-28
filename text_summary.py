import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
rawtext = """
hello world
"""
def summarizer(text=rawtext,sentence_length=3):
    stopwords = list(STOP_WORDS)
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    word_freq = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation and word.text.lower() not in ['\n']:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1
    #Obtaining the maximum frequency element
    max_freq = max(word_freq.values())

    #Normalising the word frequency [0-1]
    for word in word_freq.keys():
        word_freq[word] /= max_freq
    sentences = [sent for sent in doc.sents]
    sentence_score = {}
    for sent in sentences:
        for word in sent:
            if word.text in word_freq:
                if sent in sentence_score:
                    sentence_score[sent] += word_freq[word.text]
                else:
                    sentence_score[sent] = word_freq[word.text]
    sentence_length = int(sentence_length)
    if 0<=sentence_length<4:
        sentence_length = int(len(sentences)*0.3)
    elif 4<=sentence_length<8:
        sentence_length = int(len(sentences)*0.5)
    else:
        sentence_length = int(len(sentences)*0.99)
    summary = nlargest(sentence_length,sentence_score,key=sentence_score.get)
    fsummary = [word.text for word in summary]
    summary = ' '.join(fsummary)
    print(summary)
    return summary