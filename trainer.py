import torch 
from readConcepts import ConceptData

from CNNNetwork import Net

import torch.optim as optim
import torch.nn as nn
import torch.nn.functional as F

from constt import *


dataset = ConceptData(CONCEPT_NAME, transform=None, neg_limit=20)
TRAIN_RATIO = 0.8

trainsize = int(dataset.__len__()*TRAIN_RATIO)
testsize = dataset.__len__() - trainsize
train_set, val_set = torch.utils.data.random_split(dataset, [trainsize, testsize])


print (train_set.__len__(), val_set.__len__())


trainloader = torch.utils.data.DataLoader(train_set, batch_size=4,
                                          shuffle=True, num_workers=2)
testloader = torch.utils.data.DataLoader(val_set, batch_size=4,
                                         shuffle=False, num_workers=2)






net = Net()

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)



for epoch in range(2):  # loop over the dataset multiple times

    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        inputs, labels = data
        inputs = inputs.permute(0,3,1,2).float()
        labels = labels.long()

        # print (inputs.shape)

        optimizer.zero_grad()

        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()


        running_loss += loss.item()
        # if i % 2000 == 1999:    # print every 2000 mini-batches
        if True:
            print('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 2000))
            running_loss = 0.0

print('Finished Training')
# TESTING ---- 


correct = 0
total = 0
with torch.no_grad():
    for data in testloader:
        inputs, labels = data
        inputs = inputs.permute(0,3,1,2).float()
        labels = labels.long()


        outputs = net(inputs)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()


print ("DATESET -- \nTrain ", train_set.__len__(), "Test ", val_set.__len__())
print ("In Train : ", )
print('Accuracy of the network on test images: %d %%' % (
    100 * correct / total))

