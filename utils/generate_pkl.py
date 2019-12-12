import json
import os
import pandas as pd
import pickle
input_file_path = '/data/opencorpus-dataset/papers-2017-02-21.json'

s = 1
X = []
shard_size = 100000
for line in open(input_file_path):
    X.append(json.loads(line))
    if s % shard_size == 0:
        with open('new_data/{}.pkl'.format(s//shard_size), 'wb') as f:
            pickle.dump(pd.DataFrame(X), f, -1)
        X = []
    s += 1
