#!/usr/bin/env python3

import json
import os
import pandas as pd
import pickle
input_file_path = '/data/opencorpus-dataset/papers-2017-02-21.json'
output_directory = '/data/split_opencorpus/'

s = 1
X = []
shard_size = 100000
for line in open(input_file_path):
    X.append(line)
    if s % shard_size == 0:
        with open((output_directory + '{}.json').format(s//shard_size), 'w') as f:
            for line in X:
                f.write("%s" % line)
        X = []
    s += 1
