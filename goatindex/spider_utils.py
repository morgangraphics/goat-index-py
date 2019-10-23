import nltk
from nltk import wordpunct_tokenize, word_tokenize, sent_tokenize, Text
from nltk.corpus import stopwords, treebank_raw
#from nltk.book import gutenberg
from nltk.tokenize import RegexpTokenizer
from nltk.classify import NaiveBayesClassifier
import re


text1 = nltk.corpus.gutenberg.words('melville-moby_dick.txt')

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

    def FreqDist(self, text):
        return nltk.FreqDist(text)

    def strip_punctuation(self, text):
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(text)
        #filtered_words = [w for w in tokens if not w in set(stopwords.words('english'))]
        filtered_words = filter(lambda token: token not in set(stopwords.words('english')), tokens)
        return " ".join(filtered_words)

    def strip_stop_words(self, text):
        return ' '.join([word.lower() for word in text if word not in set(self.sw)])

    def strip_odd_spacing(self, text):
        '''
        Clean up weird formatting by removing double spaces and things like Foo 's or Bar .
        Uses a backreference to replace with thing it matched
        '''
        return re.sub(r'\s([,.\']|\s{1,})', r'\1', text)

    def tokenize(self, text):
        return Text(wordpunct_tokenize(text))

    def dispersion_plot(self, text, words, ignore_case=False, title="Lexical Dispersion Plot"):
        """
        Generate a lexical dispersion plot data. - http://www.nltk.org/_modules/nltk/draw/dispersion.html

        :param text: The source text
        :type text: list(str) or enum(str)
        :param words: The target words
        :type words: list of str
        :param ignore_case: flag to set if case should be ignored when searching text
        :type ignore_case: bool
        """

        text = list(text)
        words.reverse()

        if ignore_case:
            words_to_comp = list(map(str.lower, words))
            text_to_comp = list(map(str.lower, text))
        else:
            words_to_comp = words
            text_to_comp = text

        points = [(x, words_to_comp[y]) for x in range(len(text_to_comp))
                  for y in range(len(words_to_comp))
                  if text_to_comp[x] == words_to_comp[y]]
        if points:
            x, y = list(zip(*points))
        else:
            x = y = ()

        return { 'data': { 'coords': [list(x), list(y)], 'y-ticks': list(range(len(words))), 'y-max': len(words) }}
        #pylab.plot(x, y, "b|", scalex=.1)
        #pylab.yticks(list(range(len(words))), words, color="b")
        #pylab.ylim(-1, len(words))
        #pylab.title(title)
        #pylab.xlabel("Word Offset")
        #pylab.show()


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

        print('RAW')
        print(blob[0:200])

        print('No Punctuation')
        no_punct = self.strip_punctuation(blob)
        print(no_punct[0:200])

        print('No Stop Words')
        no_stop = self.strip_stop_words(word_tokenize(no_punct.lower()))
        print(no_stop[0:200])

        print('Frequency Distribution')
        freq_dist = self.FreqDist(word_tokenize(no_stop))
        print(freq_dist.most_common(50))

        print('Dispersion Data')
        words = [x[0] for x in freq_dist.most_common(50)]

        disp = self.dispersion_plot(word_tokenize(no_stop), words[0:5])
        print(disp)

        # print(stopwords.words('english'))


        #test = sent_tokenize(blob)
        #print(test[0:3])
        #print('\n\n=========================================================\n\n')

        #2 Split into sentences
        #sents = self.klassify.sentence(blob)
        #print(sents[0:3])

        #return sents

    def __init__(self):
        self.sw = stopwords.words("english")
        self.klassify = klassify()



a = SpiderUtils()
a.pipeline(text1[0:5000])