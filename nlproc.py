import nltk
import docx
from bs4 import BeautifulSoup
from string import punctuation


tbl = str.maketrans({ord(ch):"" for ch in punctuation})
stopwords = nltk.corpus.stopwords.words('english')


def nlproc(nl_input):
    soup = BeautifulSoup(nl_input, 'html.parser')
    clean_text = soup.get_text().translate(tbl)
    allwords = nltk.tokenize.word_tokenize(clean_text)
    allWordExceptStopDist = nltk.FreqDist(w.lower() for w in allwords if w not in stopwords)
    most_common = str(allWordExceptStopDist.most_common(5))
    return most_common

def resume_parser(resume_input):
    doc = docx.Document(resume_input)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)
