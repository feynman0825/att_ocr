# In[]

with open('data/ch_train.txt', 'r') as f:
    lines = f.read().split('\n')

lines = [line.split(' ')[0].split('/')[-1] + ' ' + line.split(' ')[1] + '\n'  for line in lines]

with open('data/ch_train2.txt', 'w') as f:
    f.writelines(lines)

# In[]
print(len(lines))

# In[]
import os
with open('./data/ch_train.txt') as fp:
    lines = fp.readlines()
BASE_PATH = '/Users/feynman/Dropbox/work/PWC/ocr_model/data/AttentionData/AttentionData'
index = 0
line_splits = lines[index].strip().split(' ')
imgpath = os.path.join(BASE_PATH, line_splits[0])

# In[]
imgpath