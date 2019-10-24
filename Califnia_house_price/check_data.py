#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   check_data.py    
@Contact :   625711951@qq.com
@License :   (C)Copyright 2019-2020, Zyf-FT

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/10/23 20:02   zyfei      1.0         None
'''

import os
import pandas as pd
import matplotlib as mp
import matplotlib.gridspec as mg
# from .get_data import housing_path

housing_path = "datasets/housing"

def load_housing_data(housing_path=housing_path):
    '''

    :param housing_path:
    :return:
    '''
    csv_path = os.path.join(housing_path, 'housing.csv')
    return pd.read_csv(csv_path)


housing = load_housing_data()
print(housing.head())


# 快四查看数据描述
# print(housing.info())

# print(housing.describe())

# 绘制各个属性的柱状图分布
# print(housing.columns)

housing.columns = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income','median_house_value', 'ocean_proximity']

def make_bar_graph(data=housing):
    '''

    :param data:
    :return:
    '''
    data = data
    mp.figure('Bar', facecolor='lightgray')
    mp.title('Bar', fontsize=20)
    gs = mg.GridSpec(3, 4)
    i, j = 0, 0
    for column in housing.columns:
        # 创建子图
        mp.subplot(gs[i, j])
        # 在图形内部添加文字，设置位置，内容，对齐方式，字号，颜色，透明度
        mp.text(0.5, 0.5, str(i) + '+' +  str(j), ha='center', va='center', size=35, color='red', alpha=0.5)
        # 删除边界刻度
        mp.xticks(())
        mp.yticks(())
        # 绘制柱状图
        single_data = housing[column]
        min_data, max_data = min(single_data), max(single_data)
        mp.xlim(min(min_data, max_data))
        step = (max_data - min_data) / 10
        for x in range(min_data, max_data, step):
            sum_num = sum(x <= single_data <= x + step)
            y.append(sum_num)
        x = np.range(len(y))
        mp.bar(x, y, 0.4, color='dodgerblue', label=column, alpha=0.75)
        # 调整子图位置
        j += 1
        j = j % 4
        i = i + j // 4
            
    # 改变布局形式，改为紧凑布局
    mp.tight_layout()
    pass

make_bar_graph(housing)

