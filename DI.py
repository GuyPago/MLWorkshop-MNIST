import torch
from models.MnistModel import MnistModel
from nets.ANN import ANN
from torch import optim
from nets.CNN import CNN

from services.MnistService import MnistService

net = CNN()
net.load_state_dict(torch.load('./data/trained_mnist_cnn.pt'))
optimizer = optim.Adam(net.parameters(), lr=5e-3)
mnist_model = MnistModel(net=net, optimizer=optimizer)
mnist_service = MnistService(model=mnist_model)
