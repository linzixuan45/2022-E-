from torch.utils.data import Dataset, DataLoader
import numpy as np
import torch
from lstm_model import LSTM, BiLSTM
import torch.nn as nn
from torch.optim import Adam, RMSprop
from torch.optim.lr_scheduler import StepLR
from tqdm import tqdm
import copy
import parser
from sklearn.preprocessing import MinMaxScaler


class MyDataset(Dataset):
    def __init__(self, data):
        self.data = data.astype('float32')
        scaler = MinMaxScaler(feature_range=(0, 1))


    def __getitem__(self, item):
        return self.data[item]

    def __len__(self):
        return len(self.data)



def mean_absolute_percentage_error(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

