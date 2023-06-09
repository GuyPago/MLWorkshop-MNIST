from typing import Any
import torch
from torch import nn, optim
from utils.BaseModel import BaseModel

class MnistModel(BaseModel):
    net: nn.Module
    optimizer: optim.Optimizer
    criterion = torch.nn.CrossEntropyLoss()

    def predict(self, image):
        self.net.eval()
        with torch.no_grad():
            pred = self.net(image).argmax()

        return pred