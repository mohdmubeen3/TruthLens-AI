import re
import string
import unicodedata
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download stopwords if not already available
try:
    stopwords.words("english")
except LookupError:
    nltk.download("stopwords")

stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()


def preprocess_text(text):

    # lowercase
    text = text.lower()

    # Remove Reuters prefix
    text = re.sub(
        r'^[A-Z\s,/\-()]+\(reuters\)\s*-\s*',
        '',
        text,
        flags=re.IGNORECASE
    )

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)

    # Unicode normalization
    text = unicodedata.normalize(
        "NFKD",
        text
    ).encode(
        "ascii",
        "ignore"
    ).decode("utf-8")

    # Remove punctuation
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    # Remove numbers
    text = re.sub(r"\d+", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    words = text.split()

    words = [
        stemmer.stem(word)
        for word in words
        if word not in stop_words
        and len(word) > 2
    ]

    return " ".join(words)