# -*- coding: UTF-8 -*-

from gensim.models import word2vec

import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = word2vec.Text8Corpus("corpus.dat")

model = word2vec.Word2Vec(sentences, size=200)

model.save("words.model") 
