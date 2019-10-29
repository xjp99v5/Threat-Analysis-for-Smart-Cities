# -*- coding: utf-8 -*-
# @Time    : 2017/10/25 15:37
# @Author  : Jiaping Xiao
# @File    : LeakAutoDetection.py

import numpy as np
import re
import itertools
import matplotlib.pyplot as plt
import graphviz as gv

import WebCrawler
import gvFunc


def createVulDatabase():
    # 自动采集得到数据库
    f = open("CVEurlMain.txt", "wb")
    # 定义网页加载的最大错误数
    max_errors = 5
    # 当前连续网页加载的错误数
    num_errors = 0

    for i in range(1,3):
        print (i)
        for page in itertools.count(0, 20):
            # if ((i == 1) and (page <= 1560)):
            if(i == 1):
                Mainurl = 'http://ics.cnvd.org.cn/?max=20&offset=%d' % page
                if page == 1560:
                    break
            else:
                # elif((i == 2) and (page <= 6160)):
                Mainurl = 'http://telecom.cnvd.org.cn/?max=20&offset=%d' % page
            if page == 6160:
                break
            # else: break

            sp = WebCrawler.getSoup(Mainurl)
            # pprint.pprint(sp.head.contents)
            if sp is None:
                # 接受一个错误
                num_errors += 1
                if (num_errors == max_errors):
                    # 错误数达到最大值
                    break
            else:
                num_errors = 0
                tbody = sp.find(attrs={'id': 'tr'})
                trs = tbody.find_all('tr')
                for tr in trs:
                    zzr = tr.find_all('a')
                    for a in zzr:
                        suburl = a['href']
                        title = a['title']
                        print (suburl)
                        print (title)
                    tds = tr.find_all(attrs={'class': 'denle'})
                    for td in tds:
                        span = td.find('span')
                        if (span == None):
                            continue
                        else:
                            threatLevel = span['class'][0]
                        print (threatLevel)
                        score = WebCrawler.threatTransform(threatLevel)
                    # td = tr.find(attrs={'class': 'denle'}
                    # if not score: break
                    f.write((suburl).encode('UTF-8'))
                    f.write('\t')
                    f.write((title).encode('UTF-8'))
                    f.write('\t')
                    f.write(str(score))
                    # f.write(urllib.urlencode(a['href']))
                    f.write('\r\n')
    f.close()


def loadLeakDatabase(dataFile):
    dataList = []
    for line in open(dataFile, 'r').readlines():
        lineArr = line.split('\t')
        dataList.append([str(lineArr[0]), str(lineArr[1]), float(lineArr[2])])
    dataMat = np.mat(dataList)
    return dataMat


# leak autonomous detection
def vulnerabilityAnalysis(component, dataFile):
    vulnerabilityVec = []
    for element in component:
        pa = re.compile(element)
        vulnerabilityDict = {}
        with open(dataFile, 'r') as f:
            vulnerability = []
            for line in f:
                if re.findall(element, line):
                    print line
                    vulnerability.append(line)
        vulnerabilityDict['element'] = element
        vulnerabilityDict['vulnerability'] = vulnerability
        vulnerabilityVec.append(vulnerabilityDict)
    return vulnerabilityVec


# 创建漏洞威胁库
def createThreats(dataFile):
    vulnerabilityList = []
    for line in open(dataFile, 'r').readlines():
        lineArr = line.split('\t')
        # threatsList = str(lineArr[1]).find('a-z')
        threatsList = re.findall('[^A-Za-z0-9]', str(lineArr[1]))
        threatsList = ''.join(threatsList)
        threatsList = re.findall('[\S]', threatsList)
        threatsList = ''.join(threatsList)
        # print threatsList.decode('utf-8')
        vulnerabilityList.append([str(lineArr[1]), str(threatsList), float(lineArr[2])])
    dataMat = np.mat(vulnerabilityList)
    return dataMat


# 匹配漏洞威胁库
def matchThreats(dataFile, threats):
    vulnerabilityList = []
    for line in open(dataFile, 'r').readlines():
        lineArr = line.split('\t')
        # threatsList = str(lineArr[1]).find('a-z')
        for iterm in threats:
            if str(lineArr[1]).find(iterm) != -1:  # 包含指定威胁
                threatsList = iterm
                break
            else:
                threatsList = '其他'
        # print threatsList.decode('utf-8')
        vulnerabilityList.append([str(lineArr[1]), str(threatsList), float(lineArr[2])])
    dataMat = vulnerabilityList
    return dataMat


########绘图得到统计值#################################
# 添加数据标签
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, height, ha='center', va='bottom')
        # 柱形图边缘用白色填充，为了美观
        rect.set_edgecolor('white')


def drawBar(labels, quants):
    fig = plt.figure(1)
    width = 0.4
    ind = np.linspace(0.5, (len(labels) - 0.5), len(labels))
    # make a square figure
    ax = fig.add_subplot(111)
    # Bar Plot
    rects = ax.bar(ind - width / 2, quants, width, color='green')
    # Set the ticks on x-axis
    ax.set_xticks(ind)
    ax.set_xticklabels(labels)
    # labels
    ax.set_xlabel('Component')
    ax.set_ylabel('Vulnerability Number (#)')
    # title
    # ax.set_title('Vulnerabilities in System', bbox={'facecolor': '0.8', 'pad': 5})
    ax.set_title('Vulnerabilities in System')
    # plt.grid(True)
    add_labels(rects)
    # plt.show()
    plt.savefig("bar.png")
    plt.close()


def drawPie(labels, quants):
    # # 饼状图
    # plot.figure(figsize=(8,8))
    fig = plt.figure(2)
    labels = labels
    sizes = quants
    # colors = ['red', 'yellow', 'blue', 'green']
    #explode = (0.1, 0.1, 0.1,  0, 0, 0, 0, 0, 0.1)
    explode = np.zeros(len(labels))
    #explode = (0.1, 0.1, 0.1, 0, 0, 0, 0)
    patches, l_text, p_text = plt.pie(sizes, labels=labels, explode = explode,
                                      labeldistance=1.2, autopct='%2.0f%%', shadow=False,
                                      startangle=90, pctdistance=0.6)

    # labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
    # autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
    # shadow，饼是否有阴影
    # startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
    # pctdistance，百分比的text离圆心的距离
    # patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本
    # 改变文本的大小
    # 方法是把每一个text遍历。调用set_size方法设置它的属性
    for t in l_text:
        t.set_size = 30
    for t in p_text:
        t.set_size = 20
    # 设置x，y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    plt.legend(loc='upper left', bbox_to_anchor=(-0.10, 1.15))
    # loc: 表示legend的位置，包括'upper right','upper left','lower right','lower left'等
    # bbox_to_anchor: 表示legend距离图形之间的距离，当出现图形与legend重叠时，可使用bbox_to_anchor进行调整legend的位置
    # 由两个参数决定，第一个参数为legend距离左边的距离，第二个参数为距离下面的距离

    # plt.title('Vulnerabilities in System')
    plt.grid()
    #plt.show()
    plt.savefig("pie.png")
    plt.close()


# 进行漏洞和威胁匹配
def VBThreatsDBMatch(vulVec, VBThreatDB):
    g1 = gv.Digraph("G", format="svg")
    root = 'Smart Power Grid'
    g1.node(root, shape='Mdiamond')
    # for vulVecList in vulVec:
    #    g1 = gvFunc.add_edges(gvFunc.add_nodes(g1, [CThreatDB['element']]), [(root, CThreatDB['element'])])
    g1 = gvFunc.add_edges(g1, [(vulVec[3]['element'], vulVec[4]['element']),
                               (vulVec[3]['element'], vulVec[1]['element']),
                               # (vulVec[3]['element'], vulVec[6]['element']),
                               (vulVec[4]['element'], vulVec[1]['element'])])

    CThreatDBList = []
    for vulVecList in vulVec:
        CThreatDB = {}
        CThreatDB['element'] = vulVecList['element']
        g1 = gvFunc.add_edges(gvFunc.add_nodes(g1, [CThreatDB['element']]), [(root, CThreatDB['element'])])
        VTDB = []
        for vulList in vulVecList['vulnerability']:
            vulArr = vulList.split('\t')
            # g1 = gvFunc.add_edges(gvFunc.add_nodes(g1, [vulArr[1].decode('utf-8')]),
            #                     [(CThreatDB['element'], vulArr[1].decode('utf-8'))]) #漏洞层
            VTList = {}
            for iterms in VBThreatDB:
                if vulArr[1] == iterms[0]:
                    VTList['url'] = vulArr[0]
                    VTList['name'] = iterms[0]
                    VTList['threat'] = iterms[1]
                    VTList['score'] = iterms[2]
                    VTDB.append(VTList)
                else:
                    continue
            # g1 = gvFunc.add_edges(gvFunc.add_nodes(g1, [VTList['threat'].decode('utf-8')]),
            #                    [(vulArr[1].decode('utf-8'), VTList['threat'].decode('utf-8'))]) #漏洞层
            g1 = gvFunc.add_edges(gvFunc.add_nodes(g1, [VTList['threat'].decode('utf-8')]),
                                  [(CThreatDB['element'], VTList['threat'].decode('utf-8'))])
        CThreatDB['vulnerability'] = VTDB
        CThreatDBList.append(CThreatDB)
    return CThreatDBList, g1

# 构建relationship 数
'''
def createRelationship(C1,C2):
    for iterms in C1:
        if C1
'''

