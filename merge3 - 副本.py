#LCS

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
#from gensim import corpora, models
#import gensim
from simhash import Simhash,SimhashIndex
import re
import xlrd
import os
from xlutils.copy import copy
import pandas as pd
import numpy as np
import time



def LCS(str1,str2):
    len1=len(str1)
    len2=len(str2)
    matrix=np.zeros([len1+1,len2+1],dtype=int)
    for i in range(len1):
        for j in range(len2):
            if str1[i]==str2[j]:
                matrix[i+1,j+1]=matrix[i,j]+1
            else:
                matrix[i+1,j+1]=max(matrix[i+1,j],matrix[i,j+1])
    #print(matrix)
    return(matrix[len1,len2])

def idProcess(name):
    filename = name
    df = pd.read_csv(filename)
    #df=pd.read_excel(filename,sheet_name='merged')
    #sheetList=list(df.keys())
    #print(sheetList)

    data=np.array(df)
    data2=[]
    #print(data)
    print(data.shape)
    length=data.shape[0]
    temptemp=[]
    for i in range(length):#(0-64399)

        #print(data[i,1])
        temp=data[i,0].split(',')
        if len(temp)>=3:
            data[i,0]=temp[1:]
        else:
            data[i,0]=temp[1:]
            #data[i,0]=temp     #id列ID数为1时若没写1就用这个，否则用上面一行的
        syns=data[i,1][1:-1]
        syns=syns.split('],[')

        temp1=[]
        for syn in syns:
            temp=syn[3:-3]
            #print(temp)
            temp=temp.split('""","""')
            #print(temp)
            temp1.append(temp)
        data[i,1]=temp1
        #data[i]由字符串转化为列表
    for i in range(length):
        if len(data[i,0])==1:
            flag=0
            for j in range(4513):
                if data[j,2]==1:
                    if data[i,0][0] in data[j,0]:
                        flag=1
            if flag==0:
                #print(data[i])
                temptemp.append(data[i])
    temptemp=pd.DataFrame(temptemp)
    temptemp.to_csv('ID.csv')

idProcess('merged191114_10_ID.csv')




