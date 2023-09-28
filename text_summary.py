import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
text = """
Sripathi Panditaradhyula Balasubrahmanyam (4 June 1946 – 25 September 2020), also referred to as SPB or SP Balu or Balu, was an Indian playback singer, television presenter, actor, music composer, dubbing artist, and film producer.[7][8] He is widely regarded as one of the greatest Indian singers of all time.[9][10][11] He predominantly worked in Tamil ,Telugu, Kannada, Malayalam, and Hindi films and sang in a total of 16 languages.[12]
Balasubrahmanyam debuted as a playback singer on 15 December 1966 with a Telugu film Sri Sri Sri Maryada Ramanna scored by his mentor, S. P. Kodandapani.[8][13] In career spanning over five decades, he has won six National Film Awards for Best Male Playback Singer for his works in four different languages – Telugu, Tamil, Kannada, and Hindi; 25 Andhra Pradesh state Nandi Awards for his work in Telugu cinema; and numerous other state awards from Karnataka and Tamil Nadu governments.[14][15] In addition, he won six Filmfare Awards South and a Filmfare Award.[16] According to some sources, he held the Guinness World Record for recording the highest number of songs by a singer with over 50,000 songs in 16 languages.[12][17][8][18] On 8 February 1981, he created a record by recording 27 songs in Kannada from 9 am to 9 pm. In addition, he recorded 19 songs in Tamil, and 16 songs in Hindi in a day, which has also been called a record.[8]
In 2012, Balasubrahmanyam received the NTR National Award from Government of Andhra Pradesh.[19] In 2015, he received the Harivarasanam Award from the Government of Kerala.[20] In 2016, he was honoured with the Indian Film Personality of the Year award at the 47th International Film Festival of India.[21][22][23] He was a recipient of the Padma Shri (2001), Padma Bhushan (2011), and Padma Vibhushan (posthumously) (2021) from the Government of India.[24][25] On 25 September 2020, Balasubrahmanyam died in Chennai after being hospitalized for over a month for complications due to COVID-19.[26]
"""
def summarizer(text=text):
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
    sentence_length = int(len(sentences)*0.5)
    summary = nlargest(sentence_length,sentence_score,key=sentence_score.get)
    fsummary = [word.text for word in summary]
    summary = ' '.join(fsummary)
summarizer()