import nltk
from nltk import wordpunct_tokenize, sent_tokenize, Text
from nltk.corpus import stopwords, treebank_raw
from nltk.classify import NaiveBayesClassifier
import re


class klassify:

    def train(self):
        sents = treebank_raw.sents()
        tokens = []
        boundaries = set()
        offset = 0
        for sent in sents:
            tokens.extend(sent)
            offset += len(sent)
            boundaries.add(offset - 1)
        self.train_set = {
            'tokens': tokens,
            'boundaries': boundaries
        }
        featuresets = self.feature_sets(self.train_set)
        #print(featuresets[0:15])
        size = int(len(featuresets) * 0.1)
        #print(size)
        train_set = featuresets#, test_set = featuresets[size:], featuresets[:size]
        classifier = NaiveBayesClassifier.train(train_set)
        #print(type(classifier))
        #print(nltk.classify.accuracy(classifier, test_set))
        return classifier

    def feature_sets(self, text):
        return [(self.punct_features(text['tokens'], i), (i in text['boundaries']))
            for i in range(1, len(text['tokens']) - 1)
            if text['tokens'][i] in '.?!']

    def punct_features(self, tokens, i):
        return {
            'next-word-capitalized': tokens[i + 1][0].isupper(),
            'prev-word': tokens[i - 1].lower(),
            'punct': tokens[i],
            'prev-word-is-one-char': len(tokens[i - 1]) == 1
        }

    def sentence(self, text):
        start = 0
        sents = []
        for i, word in enumerate(text):
            if word[0] in '.?!' and self.classifier.classify(self.punct_features(text, i)):
                sents.append(text[start:i + 1])
                start = i + 1
        if start < len(text):
            sents.append(text[start:])
            #print('aaaa = ' + text[start:] + '\n')
        return sents


    def __init__(self):
        self.train_set = {}
        self.classifier = self.train()


class SpiderUtils:

    def clean_text(self, text):
        blob = ' '.join(text)
        blob = self.strip_odd_spacing(blob)
        #blob = self.strip_stop_words(blob)
        return blob

    def strip_stop_words(self, text):
        return ' '.join([word for word in text.split() if word not in self.sw])

    def strip_odd_spacing(self, text):
        '''
        Clean up weird formatting by removing double spaces and things like Foo 's or Bar .
        Uses a backreference to replace with thing it matched
        '''
        return re.sub(r'\s([,.\']|\s{1,})', r'\1', text)

    def tokenize(self, text):
        return Text(wordpunct_tokenize(text))

    def pipeline(self, text):
        '''
            NLP pipleine is built as follows:
            https://medium.com/@surmenok/natural-language-pipeline-for-chatbots-897bda41482
            0. Clean Text
            1. Spellcheck
            2. Split into sentences
            3. Split into words
            4. POS tagging
            5. Lemmatize words
            6. Entity recognition: dates, numbers, proper nouns
            7. Find concepts/synonyms
        '''

        #0 Clean text
        blob = self.clean_text(text)

        test = sent_tokenize(blob)
        print(test[0:3])
        print('\n\n=========================================================\n\n')

        #2 Split into sentences
        sents = self.klassify.sentence(blob)
        print(sents[0:3])

        #return sents

    def __init__(self):
        self.sw = stopwords.words("english")
        self.klassify = klassify()
