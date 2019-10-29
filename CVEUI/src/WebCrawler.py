# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 20:08
# @Author  : Jiaping Xiao
# @File    : WebCrawler.py
# -*- coding: utf-8 -*-
# @Time    : 2017/10/12 18:47
# @Author  : Jiaping Xiao
# @File    : WebCrawler.py

import sys
reload(sys)

import json
import urllib2
import cookielib
import urllib
import execjs
import re
import requests

from bs4 import BeautifulSoup


def getSoup(url):
    # GET
    tags = []
    request = urllib2.Request(url=url)
    response = urllib2.urlopen(request, timeout = 50)
    result = response.read()
    print result

    soup = BeautifulSoup(result)
    return soup


def postSoup(url, data):
    # POST
    # data = urllib.urlencode({'typeId': 28 })
    request = urllib2.Request(url=url)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(request, data)
    result = response.read()
    print result

    soup = BeautifulSoup(result)
    return soup


def getCookie(url):
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    response = opener.open(url)
    for item in cookie:
        print 'Name = ' + item.name
        print 'Value =' + item.value
    return cookie


def getCookieFile(url):
    filename = 'cookie.txt'
    cookie = cookielib.MozillaCookieJar(filename)
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    response = opener.open(url)
    cookie.save(ignore_discard=True, ignore_expires=True)


def loadCookieFile(file, url):
    cookie = cookielib.MozillaCookieJar()
    cookie.load(file, ignore_discard=True, ignore_expires=True)
    req = urllib2.Request(url)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open(req)
    print response.read()


def executejs(html):
    # 提取其中的加密函数
    js_string = ''.join(re.findall(r'(function .*?)</script>', html))
    # 提取其中执行JS函数的参数
    js_func_arg = re.findall(r'setTimeout\(\"\D+\((\d+)\)\"', html)[0]
    js_func_name = re.findall(r'function (\w+)', js_string)[0]

    # 修改JS函数，使其返回Cookie内容
    js_string = js_string.replace('eval("qo=eval;qo(po);")', 'return po')

    func = execjs.compile(js_string)
    return func.call(js_func_name, js_func_arg)


def parse_cookie(string):
    string = string.replace("document.cookie = '", "")
    clearance = string.split(';')[0]
    return {clearance.split('==')[0]: clearance.split('=')[1]}


# 定义数据威胁转换函数
def threatTransform(string):
    if string == "green":
        score = 1
    else:
        if string == "yellow":
            score = 2
        else:
            score = 3
    return score


