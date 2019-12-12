#!/usr/bin/env python3
import logging

import tqdm

from citeomatic.common import DatasetPaths, FieldNames, global_tokenizer
from citeomatic.corpus import Corpus
import os
import json
from citeomatic import file_util
import pickle


input_path = '/data/split_opencorpus/1.json'
output_path ='/data/split_stripped_opencorpus/1.json'
output_pkl_path = '/data/split_stripped_opencorpus/1.pkl'

logging.info("Reading Open Corpus file from: {}".format(input_path))
logging.info("Writing json file to: {}".format(output_path))

dp = DatasetPaths()

assert os.path.exists(input_path)
assert not os.path.exists(output_path)
assert not os.path.exists(output_pkl_path)

with open(output_path, 'w') as f:
    for obj in tqdm.tqdm(file_util.read_json_lines(input_path)):
        if 'year' not in obj:
            continue
        translated_obj = {
            FieldNames.PAPER_ID: obj['id'],
            FieldNames.TITLE_RAW: obj['title'],
            FieldNames.ABSTRACT_RAW: obj['paperAbstract'],
            FieldNames.AUTHORS: [a['name'] for a in obj['authors']],
            #FieldNames.IN_CITATION_COUNT: len(obj['inCitations']),
            FieldNames.KEY_PHRASES: obj['keyPhrases'],
            #FieldNames.OUT_CITATIONS: obj['outCitations'],
            FieldNames.URLS: obj['pdfUrls'],
            FieldNames.S2_URL: obj['s2Url'],
            FieldNames.VENUE: obj['venue'],
            FieldNames.YEAR: obj['year'],
            FieldNames.TITLE: ' '.join(global_tokenizer(obj['title'])),
            FieldNames.ABSTRACT: ' '.join(global_tokenizer(obj['paperAbstract']))
        }
        f.write(json.dumps(translated_obj))
        f.write("\n")
f.close()

oc_corpus = Corpus.load(dp.get_db_path('oc'))
pickle.dump(oc_corpus, open(output_pkl_path, 'wb'))
