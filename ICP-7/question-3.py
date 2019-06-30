import nltk
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from nltk import word_tokenize, pos_tag, ne_chunk


def create_file():
    sent = open('input.txt', encoding="utf8").read()
    return sent


def create_tokenization(sent):
    sent_tokens = nltk.sent_tokenize(sent)
    wrd_tokens = nltk.word_tokenize(sent)

    print("\n==================== Tokenization ====================")

    sent_token_count = 0
    for sent_token in sent_tokens:
        sent_token_count += 1
        if sent_token_count < 4:
            print("+++sent_token+++:", sent_token)

    wrd_token_count = 0
    for wrd_token in wrd_tokens:
        wrd_token_count += 1
        if wrd_token_count < 4:
            print("+++word_token+++:", wrd_token)

    return sent_tokens, wrd_tokens


def create_stemming(wrd_tokens):
    print("\n==================== Stemming ====================")

    p_stemmer = PorterStemmer()
    l_stemmer = LancasterStemmer()
    s_stemmer = SnowballStemmer('english')

    wrd_token_count = 0
    for wrd_token in wrd_tokens:
        wrd_token_count += 1
        if wrd_token_count < 7:
            print(p_stemmer.stem(wrd_token), l_stemmer.stem(wrd_token), s_stemmer.stem(wrd_token))


def create_lemmatization(wrd_tokens):
    print("\n==================== Lemmatization ====================")

    lemmatizer = WordNetLemmatizer()

    wrd_token_count = 0
    for wrd_token in wrd_tokens:
        wrd_token_count += 1
        if wrd_token_count < 6:
            print("Lemmatizer:", lemmatizer.lemmatize(wrd_token), ",    With POS=a:",
                  lemmatizer.lemmatize(wrd_token, pos="a"))


def create_trigram(sent, sent_tokens):
    print("\n==================== Trigram ====================")

    sent_token_count = 0
    for sent_token in sent_tokens:
        sent_token_count += 1
        if sent_token_count < 2:
            token = nltk.word_tokenize(sent_token)
            bigrams = list(ngrams(token, 2))
            trigrams = list(ngrams(token, 3))
            print("The text:", sent[:100], "\nword_tokenize:", token, "\nbigrams:", bigrams, "\ntrigrams", trigrams)


def create_ner(sent_tokens):
    print("\n==================== NER ====================")

    sent_token_count = 0
    for sent_token in sent_tokens:
        sent_token_count += 1
        if sent_token_count < 2:
            print(ne_chunk(pos_tag(word_tokenize(sent_token))))


if __name__ == '__main__':
    sentence = create_file()
    sentence_tokens, word_tokens = create_tokenization(sentence)
    create_stemming(word_tokens)
    create_lemmatization(word_tokens)
    create_trigram(sentence, sentence_tokens)
    create_ner(sentence_tokens)
