#!/usr/bin/env python
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
from .get_data import housing_path


def load_housing_data(housing_path=housing_path):
    '''

    :param housing_path:
    :return:
    '''
    csv_path = os.path.join(housing_path, 'housing.csv')
    return pd.read_csv(csv_path)


housing = load_housing_data()
housing.head()