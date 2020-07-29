import numpy as np
import pandas as pd
from random import randint
import json

class LoadData:

    def __init__(self):
        self._load_root()
        self._load_vocab()

    def _load_root(self):
        data = pd.read_excel(r'vocab_data.xlsx', sheet_name='root_words')
        root_matrix = pd.DataFrame(data, columns=["root_word", "definition", "example"]).to_numpy()

        rand_root_num = randint(0, len(root_matrix))
        self.rand_root = root_matrix[rand_root_num, 0]
        self.rand_root_def = root_matrix[rand_root_num, 1]
        self.rand_root_eg = root_matrix[rand_root_num, 2]

    def _load_vocab(self):
        data = pd.read_excel(r'vocab_data.xlsx', sheet_name='vocabulary')
        vocab_matrix = pd.DataFrame(data, columns=["word", "definition"]).to_numpy()

        rand_vocab_num = randint(0, len(vocab_matrix))
        self.rand_vocab = vocab_matrix[rand_vocab_num, 0]
        self.rand_vocab_def = vocab_matrix[rand_vocab_num, 1]
