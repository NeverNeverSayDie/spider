#!/usr/bin/env python  
# -*- encoding: utf-8 -*-  

""" 
@author: niuweidong 
@software: PyCharm 
@file: post_test.py 
@time: 2019/06/10 17:17 
"""
import requests

def func():
    headers = {'Host': 'ccdas.ipmph.com',
               'Connection': 'keep-alive',
               'Accept': '*/*',
               'Origin': 'http://ccdas.ipmph.com',
               'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
               'DNT': '1',
               'Content-Type': 'application/json',
               'Referer': 'http://ccdas.ipmph.com/rwDisease/rwDiseaseList',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cookie': 'jeesite.session.id=8e5cf904d598435696820281e17d1d94; JSESSIONID=FA5967706396AD7BF58BFF249AAA17A2; __utma=182039349.1175319252.1560157997.1560157997.1560157997.1; __utmc=182039349; __utmz=182039349.1560157997.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=182039349.1.10.1560157997; wzws_cid=124b05ec2c4e42d5beb176eae45a0b09f6dc1e3b4ed043b9737cf8aaf3cc0c9827283b0b1fc81e9188bbf179d7eb2e6be4333ac51128299c29274b7550f2a780',
               'Accept-Encoding': 'gzip, deflate',
               'Content-Length': '98'}
    
    res = requests.post(url='http://ccdas.ipmph.com/rwDisease/getRwDiseaseList',
                        json={"pageNo": 1, "pageSize": "10", "searchText": "", "icd10Code": "", "departmentCode": "",
                              "symptomsWords": ""}, headers=headers)
    print(res.text)

class Main():
    
    def __init__(self):
        pass

if __name__ == "__main__":
    func()
