import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset


class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size, batch_size):
        """

        :param input_size:
        :param hidden_size:
        :param num_layers:
        :param output_size:
        :param batch_size:
        """
        super().__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.output_size = output_size
        self.num_directions = 1  # 双向LSTM
        self.batch_size = batch_size
        self.device = 'cpu'
        self.lstm = nn.LSTM(self.input_size, self.hidden_size, self.num_layers, batch_first=True)
        self.linear = nn.Linear(self.hidden_size, self.output_size)

    def forward(self, input_seq, h0=None, c0=None):
        batch_size, seq_len = input_seq.shape[0], input_seq.shape[1]
        if h0 is None:
            h_0 = torch.randn(self.num_directions * self.num_layers, self.batch_size, self.hidden_size).to(self.device)
        if c0 is None:
            c_0 = torch.randn(self.num_directions * self.num_layers, self.batch_size, self.hidden_size).to(self.device)

        output, _ = self.lstm(input_seq, (h_0, c_0))  # output(5, 30, 64)
        pred = self.linear(output)  # (5, 30, 1)
        pred = pred[:, -1, :]  # (5, 1)
        return pred

class BiLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size, batch_size):
        """

        :param input_size:
        :param hidden_size:
        :param num_layers:
        :param output_size:
        :param batch_size:
        """
        super().__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.output_size = output_size
        self.num_directions = 2  # 双向LSTM
        self.batch_size = batch_size
        self.device = 'cpu'
        self.lstm = nn.LSTM(self.input_size, self.hidden_size, self.num_layers, batch_first=True, bidirectional=True)
        self.linear = nn.Linear(self.hidden_size, self.output_size)

    def forward(self, input_seq, h0=None, c0=None):
        batch_size, seq_len = input_seq.shape[0], input_seq.shape[1]
        if h0 is None:
            h_0 = torch.randn(self.num_directions * self.num_layers, self.batch_size, self.hidden_size).to(self.device)
        if c0 is None:
            c_0 = torch.randn(self.num_directions * self.num_layers, self.batch_size, self.hidden_size).to(self.device)

        output, _ = self.lstm(input_seq, (h_0, c_0))  # output(5, 30, 64)
        out =  torch.split(output, 30,dim=-1)
        print(len(out))
        pred = self.linear(output)  # (5, 30, 1)
        pred = pred[:, -1, :]  # (5, 1)
        return pred




if __name__ == '__main__':
    a = torch.randn((1, 30, 1))
    model = LSTM(1, 30, 4, 10, 1)
    print(model(a).shape)
