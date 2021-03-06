#!/usr/bin/python3
# _*_ coding: UTF-8 _*_
import configparser
import os
import re
conf = configparser.ConfigParser()                                                  # 创建管理对象
conf_list = {
        'section1': {'name': '^[a-zA-Z]*$', 'sex': '^(male|female)$', 'age': '^([1-9]\\d{0,1}|100)$'},
        'section2': {'call': '^[a-zA-Z]*$', 'gender': '^(male|female)$'},
        'section3': {'say': '^[a-zA-Z]*$', 'age': '^([1-9]\\d{0,1}|100)$'}
       }
conf_file_name = 'Yangcheng.ini'
if os.path.exists(conf_file_name):                                                  # 判断'Yangcheng.ini'是否存在
    try:                                                                            # 存在，进行异常判断
        conf.read(conf_file_name)                                                   # 无异常（读取）
    except (configparser.MissingSectionHeaderError, configparser.ParsingError):     # 存在异常（清空文件）
        conf.clear()
    for section in conf.sections():                                                 # 循环ini文件中的section变量
        if section not in conf_list:                                                # 判断section是否在列表里
            print('section %s  is deleted' % section)
            conf.remove_section(section)                                            # 不存在（删除）
        else:
            for item in conf.options(section):                                      # 循环ini文件中section内部的option
                if item not in conf_list[section]:                                  # 判断section是否在列表的section中
                    print('item %s in section %s is deleted' % (item, section))
                    conf.remove_option(section, item)                               # 不存在（删除）
pass
for section in conf_list:                                                           # 循环字典中的section变量
    if not os.path.exists(conf_file_name) or not conf.has_section(section):         # 判断文件和section是否存在
        conf.add_section(section)                                                   # 不存在（添加section）
    for item in conf_list[section]:                                                 # 循环字典中嵌套的item变量
        raw = conf.get(section, item, fallback='')                                  # 获取原文件item变量的值并输出
        print('raw %s:%s' % (item, raw))                                             # 输入item的值
        value = input('new %s:' % item)
        if value == '':                                                             # 当value不存在时，返回原文件中item的值
            value = raw
        while not re.match(conf_list[section][item], value):                        # 判断输入是否满足正则条件，不满足则重新输入
            value = input('pls input again:')
            print(value)
        conf.set(section, item, value)                                              # 设置字典中section,item的值
pass
with open(conf_file_name, 'w') as fw:                                               # 用写的方式打开‘Yangcheng.ini’，并写入
    conf.write(fw)
for section in conf_list:                                                           # 循环section
    items = conf.items(section)                                                     # 遍历
    print(items)
