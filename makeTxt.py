import os
import random


trainval_percent = 0.1
train_percent = 0.9

xmlfilepath = 'data/voc2/Annotations'
txtsavepath = 'data/voc2/ImageSets'

if not os.path.exists(txtsavepath):
    os.makedirs(txtsavepath)

total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)
ftrainval = open('data/voc2/ImageSets/trainval.txt', 'w')
ftest = open('data/voc2/ImageSets/test.txt', 'w')
ftrain = open('data/voc2/ImageSets/train.txt', 'w')
fval = open('data/voc2/ImageSets/val.txt', 'w')
for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)
ftrainval.close()
ftrain.close()
fval.close()
ftest.close()