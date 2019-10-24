#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   make_test_test_set.py    
@Contact :   625711951@qq.com
@License :   (C)Copyright 2019-2020, Zyf-FT

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/10/23 20:18   zyfei      1.0         None
'''
import os
import pandas as pd
import numpy as np
# from .check_data import housing

housing_path = "datasets/housing"
csv_path = os.path.join(housing_path, 'housing.csv')
housing = pd.read_csv(csv_path)

def split_train_test(data=housing, test_ratio=0.2):
    '''
    分割数据集为 训练集，测试集
    :param data: 原始数据
    :param test_ratio: 分割系数，测试集占多少
    :return: 训练集，测试集
    '''
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(int(len(data)) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


# 创建训练集，测试集
train_set, test_set = split_train_test(housing, 0.2)
print(len(train_set), 'train +', len(test_set), 'test')

# 使用sklearn实现分割数据集
from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
print(len(train_set), 'train +', len(test_set), 'test')