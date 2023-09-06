import os, shutil, random
import numpy as np

base_path = '../dataset/labelme_dataset' # 原图片和TXT文件
dataset_path = '../dataset/custom_dataset' # 保存的目标位置
val_size, test_size = 0.1, 0.2

os.makedirs(dataset_path, exist_ok=True)
os.makedirs(f'{dataset_path}/images', exist_ok=True)
os.makedirs(f'{dataset_path}/images/train', exist_ok=True)
os.makedirs(f'{dataset_path}/images/val', exist_ok=True)
os.makedirs(f'{dataset_path}/images/test', exist_ok=True)
os.makedirs(f'{dataset_path}/labels/train', exist_ok=True)
os.makedirs(f'{dataset_path}/labels/val', exist_ok=True)
os.makedirs(f'{dataset_path}/labels/test', exist_ok=True)

path_list = np.array([i.split('.')[0] for i in os.listdir(base_path) if 'txt' in i])
random.shuffle(path_list)
train_id = path_list[:int(len(path_list) * (1 - val_size - test_size))]
val_id = path_list[int(len(path_list) * (1 - val_size - test_size)):int(len(path_list) * (1 - test_size))]
test_id = path_list[int(len(path_list) * (1 - test_size)):]

for i in train_id:
    shutil.copy(f'{base_path}/{i}.jpg', f'{dataset_path}/images/train/{i}.jpg')
    shutil.copy(f'{base_path}/{i}.txt', f'{dataset_path}/labels/train/{i}.txt')

for i in val_id:
    shutil.copy(f'{base_path}/{i}.jpg', f'{dataset_path}/images/val/{i}.jpg')
    shutil.copy(f'{base_path}/{i}.txt', f'{dataset_path}/labels/val/{i}.txt')

for i in test_id:
    shutil.copy(f'{base_path}/{i}.jpg', f'{dataset_path}/images/test/{i}.jpg')
    shutil.copy(f'{base_path}/{i}.txt', f'{dataset_path}/labels/test/{i}.txt')