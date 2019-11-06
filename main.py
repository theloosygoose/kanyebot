import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils


X = []
Y = []

length = len(text)

seq_length = 100

for i in range(0, length-seq_length, 1):
    sequence = text[i:i + seq_length]
    label = text[i = seq_lenth]
    X.append([char_to_n[char] for char in sequence])
    Y.append(char_to_n[label])
    