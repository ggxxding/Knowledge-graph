import pandas as pd
import numpy as np
import re

#DO
def DOProceeding(path):
    df = pd.read_csv(path)  # use_cols=[] low_memory
    df = df.fillna('')
    print(df.columns)

    #用pd.read_csv(path,dtype='str')方法会遇到比如ID：1816变为001816的问题，所以用下面循环来转换
    for i in df.columns:
        df[i]=df[i].astype('str')


    df['id'] = 'DOID:' + df['dms_id']
    #print(df['dms_id'])
    id = df['id'].values.reshape(-1, 1)
    #print(id)
    df['ids'] = ('["' + df['dms_ids.0.db'] + ':' + df['dms_ids.0.id'] + '","' + df['dms_ids.1.db'] + ':' + df['dms_ids.1.id'] +\
                 '","'+ df['dms_ids.2.db'] + ':' + df['dms_ids.2.id'] + '","'+ df['dms_ids.3.db'] + ':' + df['dms_ids.3.id'] +\
                 '","'+ df['dms_ids.4.db'] + ':' + df['dms_ids.4.id'] + '","'+ df['dms_ids.5.db'] + ':' + df['dms_ids.5.id'] +\
                 '","'+ df['dms_ids.6.db'] + ':' + df['dms_ids.6.id'] + '","'+ df['dms_ids.7.db'] + ':' + df['dms_ids.7.id'] +\
                 '","'+ df['dms_ids_extend.0.db'] + ':' + df['dms_ids_extend.0.id'] +\
                 '","'+ df['dms_ids_extend.1.db'] + ':' + df['dms_ids_extend.1.id'] +\
                 '","'+ df['dms_ids_extend.2.db'] + ':' + df['dms_ids_extend.2.id'] +\
                 '","'+ df['dms_ids_extend.3.db'] + ':' + df['dms_ids_extend.3.id'] +\
                 '","'+ df['dms_ids_extend.4.db'] + ':' + df['dms_ids_extend.4.id'] +\
                 '","'+ df['dms_ids_extend.5.db'] + ':' + df['dms_ids_extend.5.id'] +\
                 '","'+ df['dms_ids_extend.6.db'] + ':' + df['dms_ids_extend.6.id'] +\
                 '","'+ df['dms_ids_extend.7.db'] + ':' + df['dms_ids_extend.7.id'] +'"]')
    ids = df['ids'].values
    for index, i in enumerate(ids):
        templist = eval(i)
        templist = list(set(templist))
        if ':' in templist:
            templist.remove(':')
        tempchar = '["""'
        for j in templist:
            tempchar = tempchar + j + '""","""'
        tempchar = tempchar[:-4] + ']'
        ids[index] = tempchar
    ids = ids.reshape(-1, 1)

    df['name'] = df['dms_name']
    name = df['name'].values.reshape(-1, 1)

    df['syn']= '["' + df['dms_synonym.0'] + '","' + df['dms_synonym.1'] + '","' + df['dms_synonym.2']+ \
                '","' + df['dms_synonym.3']+ '","' + df['dms_synonym.4']+'","'+ df['dms_synonym_extend.0']+\
               '","'+df['dms_synonym_extend.1']+'","'+df['dms_synonym_extend.2']+ '","' + df['dms_synonym_extend.3']+\
               '","' + df['dms_synonym_extend.4']+'"]'
    syn = df['syn'].values
    for index, i in enumerate(syn):
        templist = eval(i)
        templist = list(set(templist))
        if '' in templist:
            templist.remove('')
        tempchar = '["""'
        for j in templist:
            tempchar = tempchar + j + '""","""'
        tempchar = tempchar[:-4] + ']'
        syn[index] = tempchar
    syn = syn.reshape(-1, 1)

    sum = np.concatenate((id, ids, name, syn), axis=1)
    df = pd.DataFrame(sum)
    df.columns = ['id', 'ids', 'name', 'syn']
    #df.to_excel('DO.xlsx', index=False)
    df.to_csv('DO.csv',index=False)
    return df

#ICD10
def ICD1Proceeding(path):
    df = pd.read_csv(path, dtype='str')  # use_cols=[] low_memory
    df = df.fillna('')
    print(df.columns)

    #用pd.read_csv(path,dtype='str')方法会遇到比如ID：1816变为001816的问题，所以用下面循环来转换
    for i in df.columns:
        df[i]=df[i].astype('str')

    df['id'] = 'ICD10_CM:'+df['dms_id']
    id=df['id'].values.reshape(-1,1)

    df['ids'] = ('["' + df['dms_ids.0.db']+':'+df['dms_ids.0.id'] + '","' + df['dms_ids_extend.0.db'] + ':' + df['dms_ids_extend.0.id']+\
           '","' + df['dms_ids_extend.1.db'] + ':' + df['dms_ids_extend.1.id']+\
        '","' + df['dms_ids_extend.2.db'] + ':' + df['dms_ids_extend.2.id'] + '"]')
    ids=df['ids'].values
    for index,i in enumerate(ids):
        templist=eval(i)
        templist=list(set(templist))
        if ':' in templist:
            templist.remove(':')
        tempchar='["""'
        for j in templist:
            tempchar=tempchar+j+'""","""'
        tempchar=tempchar[:-4]+']'
        ids[index] = tempchar

    ids = ids.reshape(-1, 1)

    df['name'] = df['dms_name']
    name=df['name'].values.reshape(-1,1)
    #print(name)

    df['syn']= '["""' + df['dms_synonym.0'] + '""","""' + df['dms_synonym.1'] + '""","""' + df['dms_synonym.2']+\
          df['dms_synonym_extend.0']+'""","""'+df['dms_synonym_extend.1']+'""","""'+df['dms_synonym_extend.2']+'"""]'
    #print(df['syn'])
    syn=df['syn'].values
    for index,i in enumerate(syn):
        templist=eval(i)
        templist=list(set(templist))
        if '' in templist:
            templist.remove('')
        tempchar='["""'
        for j in templist:
            tempchar = tempchar + j + '""","""'
        tempchar = tempchar[:-4] + ']'
        syn[index]=tempchar
    syn=syn.reshape(-1,1)

    sum=np.concatenate((id,ids,name,syn),axis=1)
    df=pd.DataFrame(sum)
    df.columns=['id','ids','name','syn']
    #df.to_excel('ICD10CM.xlsx',index=False)
    df.to_csv('ICD10CM.csv', index=False)
    return df

def ICD2Proceeding(path):
    df = pd.read_csv(path, dtype='str')  # use_cols=[] low_memory
    df = df.fillna('')
    print(df.columns)

    #用pd.read_csv(path,dtype='str')方法会遇到比如ID：1816变为001816的问题，所以用下面循环来转换
    for i in df.columns:
        df[i]=df[i].astype('str')

    df['id'] = 'ICD10:'+df['dms_id']
    id=df['id'].values.reshape(-1,1)

    df['ids'] = ('["' + df['dms_ids.0.db']+':'+df['dms_ids.0.id'] + '","' +\
                 df['dms_ids_extend.0.db'] + ':' + df['dms_ids_extend.0.id']+ '"]')
    ids=df['ids'].values
    for index,i in enumerate(ids):
        templist=eval(i)
        templist=list(set(templist))
        if ':' in templist:
            templist.remove(':')
        tempchar='["""'
        for j in templist:
            tempchar=tempchar+j+'""","""'
        tempchar=tempchar[:-4]+']'
        ids[index] = tempchar
    ids = ids.reshape(-1, 1)

    df['name'] = df['dms_name']
    name=df['name'].values.reshape(-1,1)
    #print(name)

    df['syn']= "['''" + df['dms_synonym.0'] + "''','''" + df['dms_synonym.1'] + "''','''"+ df['dms_synonym.2']+\
          "''','''" + df['dms_synonym.3']+"''','''" + df['dms_synonym.4']+"''','''"+ df['dms_synonym.5']+\
        "''','''"+df['dms_synonym_extend.0']+"''','''"+df['dms_synonym_extend.1']+"''','''"+df['dms_synonym_extend.2']+\
               "''','''" + df['dms_synonym_extend.3']+"''','''" + df['dms_synonym_extend.4']+"''','''" +\
               df['dms_synonym_extend.5']+"''']"
    #print(df['syn'])
    syn=df['syn'].values
    for index,i in enumerate(syn):
        templist=eval(i)
        templist=list(set(templist))
        if '' in templist:
            templist.remove('')
        tempchar="['''"
        for j in templist:
            tempchar = tempchar + j +"''','''"
        tempchar = tempchar[:-4] + ']'
        syn[index]=tempchar
    syn=syn.reshape(-1,1)

    sum=np.concatenate((id,ids,name,syn),axis=1)
    df=pd.DataFrame(sum)
    df.columns=['id','ids','name','syn']
    #df.to_excel('ICD10.xlsx',index=False)
    df.to_csv('ICD10.csv', index=False)
    return df

def MeSHProceeding(path):
    df = pd.read_csv(path, dtype='str')  # use_cols=[] low_memory
    df = df.fillna('')
    print(df.columns)

    #用pd.read_csv(path,dtype='str')方法会遇到比如ID：1816变为001816的问题，所以用下面循环来转换
    for i in df.columns:
        df[i]=df[i].astype('str')

    df['id'] = 'MeSH:'+df['dms_id']
    id=df['id'].values.reshape(-1,1)

    df['ids'] = ('["""' + df['dms_ids.0.db']+':'+df['dms_ids.0.id'] + '""","""' +\
                 df['dms_ids_extend.0.db'] + ':' + df['dms_ids_extend.0.id']+ '"""]')
    ids=df['ids'].values
    for index,i in enumerate(ids):
        templist=eval(i)
        templist=list(set(templist))
        if ':' in templist:
            templist.remove(':')
        tempchar='["""'
        for j in templist:
            tempchar=tempchar+j+'""","""'
        tempchar=tempchar[:-4]+']'
        ids[index] = tempchar
    ids = ids.reshape(-1, 1)

    df['name'] = df['dms_name']
    name=df['name'].values.reshape(-1,1)
    #print(name)

    df['syn']= '["""' + df['dms_synonym.0'] + '""","""' + df['dms_synonym.1'] + '""","""'+ df['dms_synonym.2']+\
          '""","""' + df['dms_synonym.3']+'""","""' + df['dms_synonym.4']+'""","""'+ df['dms_synonym.5']+ \
               '""","""' + df['dms_synonym.6'] + '""","""' + df['dms_synonym.7'] + '""","""' + df['dms_synonym.8'] + \
               '""","""' + df['dms_synonym.9'] + '""","""' + df['dms_synonym.10'] + '""","""'+ df['dms_synonym.11'] + \
               '""","""' + df['dms_synonym.12'] + '""","""' + df['dms_synonym.13'] + '""","""' + df['dms_synonym.14'] + \
               '""","""' + df['dms_synonym.15']+\
               '""","""'+df['dms_synonym_extend.0']+'""","""'+df['dms_synonym_extend.1']+'""","""'+df['dms_synonym_extend.2']+ \
               '""","""'+ df['dms_synonym_extend.3'] + '""","""' + df['dms_synonym_extend.4'] + \
               '""","""' + df['dms_synonym_extend.5'] + '""","""' + df['dms_synonym_extend.6']+ \
               '""","""'+ df['dms_synonym_extend.7'] +'""","""'+ df['dms_synonym_extend.8'] + \
               '""","""'+ df['dms_synonym_extend.9'] + '""","""'+ df['dms_synonym_extend.10'] + \
               '""","""' + df['dms_synonym_extend.11'] + '""","""' + df['dms_synonym_extend.12'] + \
               '""","""' + df['dms_synonym_extend.13'] + '""","""' + df['dms_synonym_extend.14'] + \
               '""","""'+ df['dms_synonym_extend.15'] +'"""]'
    #print(df['syn'])
    syn=df['syn'].values
    for index,i in enumerate(syn):
        templist=eval(i)
        templist=list(set(templist))
        if '' in templist:
            templist.remove('')
        tempchar='["""'
        for j in templist:
            tempchar = tempchar + j + '""","""'
        tempchar = tempchar[:-4] + ']'
        syn[index]=tempchar
    syn=syn.reshape(-1,1)

    sum=np.concatenate((id,ids,name,syn),axis=1)
    df=pd.DataFrame(sum)
    df.columns=['id','ids','name','syn']
    #df.to_excel('MeSH.xlsx',index=False)
    df.to_csv('MeSH.csv', index=False)
    return df

def chemicalsProceeding(path):
    df = pd.read_csv(path,sep='\t' , dtype='str')  # use_cols=[] low_memory
    df = df.fillna('')
    print(df.columns)

    #用pd.read_csv(path,dtype='str')方法会遇到比如ID：1816变为001816的问题，所以用下面循环来转换
    for i in df.columns:
        df[i]=df[i].astype('str')

    df['id'] = 'PharmGKB:'+df['PharmGKB Accession Id']
    id=df['id'].values.reshape(-1,1)

    df['name'] = df['Name']
    name = df['name'].values.reshape(-1, 1)



    Generic_Names=df['Generic Names'].values
    for index,i in enumerate(Generic_Names):
        #print(i)
        templist=i.split(',"')
        for index2,j in enumerate(templist):
            templist[index2]=j.strip('"')
        tempchar='["""'
        for k in templist:
            tempchar=tempchar+k+'""","""'
        tempchar=tempchar[:-4]+']'
        Generic_Names[index]=tempchar
    Generic_Names=Generic_Names.reshape(-1,1)
    Trade_Names=df['Trade Names'].values.reshape(-1,1)
    Type=df['Type'].values.reshape(-1,1)

    #df['ids'] = ('["""' + df['dms_ids.0.db']+':'+df['dms_ids.0.id'] + '""","""' +\
    #             df['dms_ids_extend.0.db'] + ':' + df['dms_ids_extend.0.id']+ '"""]')
    df['ids']=df['Cross-references']
    ids=df['ids'].values
    for index,i in enumerate(ids):
        templist=i.split(',')
        #print(templist)
        for index2,j in enumerate(templist):
            templist[index2]=j.strip('"')
        #print(templist)
        tempchar='["""'
        for k in templist:
            tempchar=tempchar+k+'""","""'
        tempchar=tempchar[:-4]+']'
        ids[index]=tempchar
    '''for index,i in enumerate(ids):
        templist=eval(i)
        templist=list(set(templist))
        if ':' in templist:
            templist.remove(':')
        tempchar='["""'
        for j in templist:
            tempchar=tempchar+j+'""","""'
        tempchar=tempchar[:-4]+']'
        ids[index] = tempchar'''
    ids = ids.reshape(-1, 1)

    SMILES=df['SMILES'].values.reshape(-1,1)
    InChI=df['InChI'].values.reshape(-1,1)
    Dosing_Guideline=df['Dosing Guideline'].values.reshape(-1,1)
    External_Vocabulary=df['External Vocabulary'].values
    for index,i in enumerate(External_Vocabulary):
        templist=i.split(',"')
        for index2,j in enumerate(templist):
            templist[index2]=j.strip('"').split('(')[0]
        tempchar='["""'
        for k in templist:
            tempchar=tempchar+k+'""","""'
        tempchar=tempchar[:-4]+']'
        External_Vocabulary[index]=tempchar
    External_Vocabulary=External_Vocabulary.reshape(-1,1)
    Clinical_Annotation_Count=df['Clinical Annotation Count'].values.reshape(-1,1)
    Variant_Annotation_Count=df['Variant Annotation Count'].values.reshape(-1,1)
    Pathway_Count=df['Pathway Count'].values.reshape(-1,1)
    VIP_Count=df['VIP Count'].values.reshape(-1,1)


    sum=np.concatenate((id,name,Generic_Names,Trade_Names,Type,ids,\
                        SMILES,InChI,Dosing_Guideline,External_Vocabulary,\
                        Clinical_Annotation_Count,Variant_Annotation_Count,\
                        Pathway_Count,VIP_Count),axis=1)
    df=pd.DataFrame(sum)
    df.columns=['PharmGKB_Id','Name','Generic_names','Trade_names','Type',\
                'Cross-reference','SMILES','InChI','Dosing_Guideline',\
                'External_Vocabulary','Clinical_Annotation_Count',\
                'Variant_Annotation_Count',\
                        'Pathway_Count','VIP_Count']
    #df.to_excel('MeSH.xlsx',index=False)
    df.to_csv('chemicals.csv', index=False)
    return df

def drugsProceeding(path):
    df = pd.read_csv(path,sep='\t' , dtype='str')  # use_cols=[] low_memory
    df = df.fillna('')
    print(df.columns)

    #用pd.read_csv(path,dtype='str')方法会遇到比如ID：1816变为001816的问题，所以用下面循环来转换
    for i in df.columns:
        df[i]=df[i].astype('str')

    df['id'] = 'PharmGKB:'+df['PharmGKB Accession Id']
    id=df['id'].values.reshape(-1,1)

    df['name'] = df['Name']
    name = df['name'].values.reshape(-1, 1)



    Generic_Names=df['Generic Names'].values
    for index,i in enumerate(Generic_Names):
        #print(i)
        templist=i.split(',"')
        for index2,j in enumerate(templist):
            templist[index2]=j.strip('"')
        tempchar='["""'
        for k in templist:
            tempchar=tempchar+k+'""","""'
        tempchar=tempchar[:-4]+']'
        Generic_Names[index]=tempchar
    Generic_Names=Generic_Names.reshape(-1,1)
    Trade_Names=df['Trade Names'].values.reshape(-1,1)
    Type=df['Type'].values.reshape(-1,1)

    #df['ids'] = ('["""' + df['dms_ids.0.db']+':'+df['dms_ids.0.id'] + '""","""' +\
    #             df['dms_ids_extend.0.db'] + ':' + df['dms_ids_extend.0.id']+ '"""]')
    df['ids']=df['Cross-references']
    ids=df['ids'].values
    for index,i in enumerate(ids):
        templist=i.split(',')
        #print(templist)
        for index2,j in enumerate(templist):
            templist[index2]=j.strip('"')
        #print(templist)
        tempchar='["""'
        for k in templist:
            tempchar=tempchar+k+'""","""'
        tempchar=tempchar[:-4]+']'
        ids[index]=tempchar
    ids = ids.reshape(-1, 1)

    SMILES=df['SMILES'].values.reshape(-1,1)
    InChI=df['InChI'].values.reshape(-1,1)
    Dosing_Guideline=df['Dosing Guideline'].values.reshape(-1,1)
    External_Vocabulary=df['External Vocabulary'].values
    for index,i in enumerate(External_Vocabulary):
        templist=i.split(',"')
        for index2,j in enumerate(templist):
            templist[index2]=j.strip('"').split('(')[0]
        tempchar='["""'
        for k in templist:
            tempchar=tempchar+k+'""","""'
        tempchar=tempchar[:-4]+']'
        External_Vocabulary[index]=tempchar
    External_Vocabulary=External_Vocabulary.reshape(-1,1)
    Clinical_Annotation_Count=df['Clinical Annotation Count'].values.reshape(-1,1)
    Variant_Annotation_Count=df['Variant Annotation Count'].values.reshape(-1,1)
    Pathway_Count=df['Pathway Count'].values.reshape(-1,1)
    VIP_Count=df['VIP Count'].values.reshape(-1,1)


    sum=np.concatenate((id,name,Generic_Names,Trade_Names,Type,ids,\
                        SMILES,InChI,Dosing_Guideline,External_Vocabulary,\
                        Clinical_Annotation_Count,Variant_Annotation_Count,\
                        Pathway_Count,VIP_Count),axis=1)
    df=pd.DataFrame(sum)
    df.columns=['PharmGKB_Id','Name','Generic_names','Trade_names','Type',\
                'Cross-reference','SMILES','InChI','Dosing_Guideline',\
                'External_Vocabulary','Clinical_Annotation_Count',\
                'Variant_Annotation_Count',\
                        'Pathway_Count','VIP_Count']
    #df.to_excel('MeSH.xlsx',index=False)
    df.to_csv('drugs.csv', index=False)
    return df

def phenotypesProceeding(path):
    df = pd.read_csv(path,sep='\t' , dtype='str')  # use_cols=[] low_memory
    df = df.fillna('')
    print(df.columns)

    #用pd.read_csv(path,dtype='str')方法会遇到比如ID：1816变为001816的问题，所以用下面循环来转换
    for i in df.columns:
        df[i]=df[i].astype('str')

    df['id'] = 'PharmGKB:'+df['PharmGKB Accession Id']
    id=df['id'].values.reshape(-1,1)

    df['name'] = df['Name']
    name = df['name'].values.reshape(-1, 1)



    Alternate_Names=df['Alternate Names'].values
    for index,i in enumerate(Alternate_Names):
        #print(i)
        templist=i.split(',"')
        for index2,j in enumerate(templist):
            templist[index2]=j.strip('"')
        tempchar='["""'
        for k in templist:
            tempchar=tempchar+k+'""","""'
        tempchar=tempchar[:-4]+']'
        Alternate_Names[index]=tempchar
    Alternate_Names=Alternate_Names.reshape(-1,1)
    df['ids']=df['Cross-references']
    ids=df['ids'].values
    for index,i in enumerate(ids):
        templist=i.split(',"')
        #print(templist)
        for index2,j in enumerate(templist):
            templist[index2]=j.strip('"')
        #print(templist)
        tempchar='["""'
        for k in templist:
            tempchar=tempchar+k+'""","""'
        tempchar=tempchar[:-4]+']'
        ids[index]=tempchar
    ids = ids.reshape(-1, 1)
    External_Vocabulary=df['External Vocabulary'].values
    for index,i in enumerate(External_Vocabulary):
        templist=i.split(',"')
        for index2,j in enumerate(templist):
            templist[index2]=j.strip('"').split('(')[0]
        tempchar='["""'
        for k in templist:
            tempchar=tempchar+k+'""","""'
        tempchar=tempchar[:-4]+']'
        External_Vocabulary[index]=tempchar
    External_Vocabulary=External_Vocabulary.reshape(-1,1)
    #.reshape(-1,1)


    sum=np.concatenate((id,name,Alternate_Names,ids,External_Vocabulary),axis=1)
    df=pd.DataFrame(sum)
    df.columns=['PharmGKB_Id','Name','Alternate_names','Cross-reference',\
                'External_Vocabulary']
    #df.to_excel('MeSH.xlsx',index=False)
    df.to_csv('phenotypes.csv', index=False)
    return df

def filesProceeding(nameDO,nameICDCM,nameICD,nameMeSH,\
                 nameChemicals,nameDrugs,namePhenotypes):
    pathDO = nameDO
    pathICD1 = nameICDCM
    pathICD2 = nameICD
    pathMeSH = nameMeSH
    pathChemicals=nameChemicals
    pathDrugs=nameDrugs
    pathPhenotypes=namePhenotypes

    a = DOProceeding(pathDO)
    b = ICD1Proceeding(pathICD1)
    c = ICD2Proceeding(pathICD2)
    d = MeSHProceeding(pathMeSH)
    e = chemicalsProceeding(pathChemicals)
    f = drugsProceeding(pathDrugs)
    g = phenotypesProceeding(pathPhenotypes)

    #pdWriter = pd.ExcelWriter("base3(IDfixed).xlsx")
    #b.to_excel(pdWriter, sheet_name="ICD10CM", index=False)
    #c.to_excel(pdWriter, sheet_name="ICD10", index=False)
    #d.to_excel(pdWriter, sheet_name="MeSH", index=False)
    #pdWriter.save()
    #pdWriter.close()
#filesToExcel()
'''nameDO='datasets\DiseaseOntology_20190627.csv'
nameICDCM='datasets\ICD10CM2019_20180626-USA.csv'
nameICD='datasets\ICD102016_20180704-WHO.csv'
nameMeSH='datasets\MeSH2018_20180713.csv'
nameChemicals='datasets\chemicals\chemicals.tsv'
nameDrugs='datasets\drugs\drugs.tsv'
namePhenotypes='datasets\phenotypes\phenotypes.tsv'
filesProceeding(nameDO,nameICDCM,nameICD,nameMeSH,\
                nameChemicals,nameDrugs,namePhenotypes)'''