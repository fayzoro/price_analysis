#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   get_data.py    
@Contact :   625711951@qq.com
@License :   (C)Copyright 2019-2020, Zyf-FT

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/10/23 19:54   zyfei      1.0         None
'''

import os
import tarfile
import urllib
import urllib.request

download_root = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
housing_path = "datasets/housing"
housing_url = download_root + housing_path + "/housing.tgz"

def fetch_housing_data(housing_url=housing_url, housing_path=housing_path):
    '''

    :param housing_url:
    :param housing_path:
    :return:
    '''
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, 'housing.tgz')
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


if __name__ == '__main__':
    fetch_housing_data()
