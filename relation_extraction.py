import pandas as pd
import re
import numpy as np

def nameProceeding(name):
    if '"' in name:
        temp=name.split(',"')
        for i in range(len(temp)):
            temp[i]=temp[i].strip('"').split(' ')
    else:
        temp=[name.split(' ')]
    return temp

def readVar_drug_ann(path):
    df = pd.read_csv(path,sep='\t')  # use_cols=[] low_memory
    df = df.fillna('')
    print(df.columns)
    triplets=[]

    #用pd.read_csv(path,dtype='str')方法会遇到比如ID：1816变为001816的问题，所以用下面循环来转换
    for i in df.columns:
        df[i]=df[i].astype('str')
    Sentence=df['Sentence'].values
    Chemical=df['Chemical'].values
    Variant=df['Variant'].values
    Gene=df['Gene'].values
    temp=set()
    for i in range(len(Sentence)):
        #print(i)
        matched=False
        matched2=False
        matched3=False
        matched = re.match(r'(.*?) (is|are) associated with (.*?) (to|of) (.*?) in (\S+) with(.*)',Sentence[i])
        if not matched:
            matched2 = re.match(r'(.*?) (is|are) associated with (.*?) (to|of) (.*?) in (.*)',Sentence[i])
        if not matched and not matched2:
            if 'not associated' not in Sentence[i]:
                matched3 = re.match(r'(.*?) (is|are) associated with (.*?) (to|of) (.*)', Sentence[i])
        if matched:
            relation=matched.group(3)+' '+matched.group(4)
            #print(relation)
            tailList=nameProceeding(Chemical[i])
            tailList2=nameProceeding(Gene[i])
            #print(tailList)
            head=Variant[i]
            triplets.append([head,tailList,relation])
            triplets.append([head,tailList2,'belongs to'])


            temp.add(matched.group(6))
            continue
        if matched2:
            if ' men ' in Sentence[i] or ' women ' in Sentence[i]:
                continue
                #print(i)
            #print(2,matched2.groups())

    print(temp)
    print(triplets)
    triplets=np.array(triplets,dtype=object)
    print(triplets)
    print(triplets.shape)
    print(triplets[0,1])
    tempset=set()
    for i in triplets:
        tempset.add(i[2])
    print(tempset)



readVar_drug_ann('datasets\\annotations\\var_drug_anncopy.tsv')