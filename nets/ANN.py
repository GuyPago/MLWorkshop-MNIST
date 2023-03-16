import torch
from torch import nn


class ANN(nn.Module):
    def __init__(self, image_size, n_hidden, n_classes) -> None:
        super().__init__()

        self.fc = nn.Sequential(
            nn.Linear(image_size ** 2, n_hidden),
            nn.ReLU(),
            nn.Linear(n_hidden, n_hidden),
            nn.ReLU(),
            nn.Linear(n_hidden, n_classes)
        )

    def preprocess(self, x: torch.Tensor):
        return x.flatten(1)

    def forward(self, x):
        x = self.preprocess(x)
        x = self.fc(x)
        
        return x