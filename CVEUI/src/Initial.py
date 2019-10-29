# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 15:06
# @Author  : Jiaping Xiao
# @File    : Initial.py

import pprint
import scipy.io as scio

import LeakAutoDetection

# 数据库文件
dataFile = 'CVEurl.txt'
#component = ['Meter', 'PowerSCADA','AMI', 'WebAccess','SQL','Controller','PowerHMI','PLC','RTU']
component = ['Cisco','Oracle', 'Linux', 'MS', 'WebAccess','SQL']
#自动输出漏洞数组对
vulVec = LeakAutoDetection.vulnerabilityAnalysis(component, dataFile)
pprint.pprint(vulVec)

#绘制统计图
def drawResults():
    labels = []
    quants = []
    for vulnerabilityDict in vulVec:
        labels.append(vulnerabilityDict['element'])
        leakvec = vulnerabilityDict['vulnerability']
        quants.append(int(len(leakvec)))

    statValue = {'labels':labels,'quants':quants}
    dataMat = 'statValue.mat'
    scio.savemat(dataMat, statValue)

    LeakAutoDetection.drawBar(labels, quants)
    LeakAutoDetection.drawPie(labels, quants)

#创建威胁库
def createThreats():
    threatsVec = LeakAutoDetection.createThreats(dataFile)
    print threatsVec
    return threatsVec

# 由威胁输出定义威胁库
threats = ['拒绝服务', '权限提升', '修改', '泄露', '注入', '溢出', '验证绕过', '未授权访问', '未授权操作', '未知']

def matchThreats():
    VBThreatDB = LeakAutoDetection.matchThreats(dataFile, threats)
    CThreatDBList, g1 = LeakAutoDetection.VBThreatsDBMatch(vulVec, VBThreatDB)
    pprint.pprint(CThreatDBList)
    print(g1.source)
    g1.render('g1')
    return g1







