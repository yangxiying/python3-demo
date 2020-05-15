#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, paddlehub as hub

# 把图片中的人物给抠出来
# 参考  https://mp.weixin.qq.com/s/0K1YiR_tCnfg65ZoN8QUqQ
huseg = hub.Module(name='deeplabv3p_xception65_humanseg') # 加载模型
path = './imgs/' # 文件目录
files = [path + i for i in os.listdir(path)] # 获取文件列表
print("=====================================")
files.remove('./imgs/.DS_Store')
print(files)
# results = huseg.segmentation(data={'image': files}) # 抠图 yxy：原是这样的，运行发现没有保存，查看api发现visualization=False
results = huseg.segmentation(data={'image': files},visualization=True)

# or
# results = huseg.segmentation(paths=files,visualization=True) # 抠图


