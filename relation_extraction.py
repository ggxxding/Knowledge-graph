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
    temptail=set()
    temp6=set()
    for i in range(len(Sentence)):
        #print(i)
        matched=False
        matched2=False
        matched3=False
        matched = re.match(r'(.*?) (is|are) associated with (.*?) (to|of) (.*)',Sentence[i])
        if matched:
            relation = matched.group(3) + ' ' + matched.group(4)
            # +' '+matched.group(5)+' in '+matched.group(6)+' with '+matched.group(7)

            temp6.add(matched.group(5))

            tailList = nameProceeding(Chemical[i])
            tailList2 = nameProceeding(Gene[i])
            note = ''
            for j in tailList2:
                if matched.group(5).split(' ')[0] in j:
                    tailList = tailList2
                    note = matched.group(5).split(' ')[1:]

            # print(tailList)
            head = Variant[i]
            if tailList != [['']]:
                triplets.append([head, tailList, relation, note])
            if tailList2 != [['']]:
                triplets.append([head, tailList2, 'belongs to', note])

            continue
        if 'not associated with' not in Sentence[i]:
            print(Sentence[i])
        head = Variant[i]
        tailList2 = nameProceeding(Gene[i])
        note = ''
        if tailList2 != [['']]:
            triplets.append([head, tailList2, 'belongs to', note])


    '''print(temp)
    print(temptail)
    print(temp6)'''
    triplets=np.array(triplets,dtype=object)
    print(triplets.shape)
    tempset=set()
    for i in triplets:
        tempset.add(i[2])
        if i[3]!='':
            print(1)
    print(tempset)
    print(len(tempset))
    triplets=pd.DataFrame(triplets,columns=['head','tail','relation','note'])
    triplets.to_csv('triplets_var_drug.csv',index=False)

def readVar_fa_ann(path):
    df = pd.read_csv(path, sep='\t')  # use_cols=[] low_memory
    df = df.fillna('')
    print(df.columns)
    triplets = []

    # 用pd.read_csv(path,dtype='str')方法会遇到比如ID：1816变为001816的问题，所以用下面循环来转换
    for i in df.columns:
        df[i] = df[i].astype('str')
    Sentence = df['Sentence'].values
    Chemical = df['Chemical'].values
    Variant = df['Variant'].values
    Gene = df['Gene'].values
    temp = set()
    temptail = set()
    temp6 = set()
    for i in range(len(Sentence)):

        # print(i)
        matched = False
        matched2 = False
        matched3 = False
        matched = re.match(r'(.*?) (is|are) associated with (.*?) (to|of) (.*)', Sentence[i])
        if matched:
            relation = matched.group(3) + ' ' + matched.group(4)
            # +' '+matched.group(5)+' in '+matched.group(6)+' with '+matched.group(7)

            temp6.add(matched.group(5))

            tailList = nameProceeding(Chemical[i])
            tailList2 = nameProceeding(Gene[i])
            note=''
            for j in tailList2:
                if matched.group(5).split(' ')[0] in j:
                    tailList=tailList2
                    note=matched.group(5).split(' ')[1:]

            # print(tailList)
            head = Variant[i]
            if tailList != [['']]:
                triplets.append([head, tailList, relation,note])
            if tailList2 != [['']]:
                triplets.append([head, tailList2, 'belongs to',note])

            continue
        if 'not associated with' not in Sentence[i]:
            print(Sentence[i])
        head = Variant[i]
        tailList2 = nameProceeding(Gene[i])
        note=''
        if tailList2 != [['']]:
            triplets.append([head, tailList2, 'belongs to',note])

    '''print(temp)
    print(temptail)
    print(temp6)'''
    triplets = np.array(triplets, dtype=object)
    print(triplets.shape)
    tempset = set()
    for i in triplets:
        tempset.add(i[2])

    print(tempset)
    print(len(tempset))
    triplets = pd.DataFrame(triplets, columns=['head', 'tail', 'relation','note'])
    triplets.to_csv('triplets_var_fa.csv', index=False)

def readVar_pheno_ann(path):
    df = pd.read_csv(path, sep='\t')  # use_cols=[] low_memory
    df = df.fillna('')
    print(df.columns)
    triplets = []

    # 用pd.read_csv(path,dtype='str')方法会遇到比如ID：1816变为001816的问题，所以用下面循环来转换
    for i in df.columns:
        df[i] = df[i].astype('str')
    Sentence = df['Sentence'].values
    Chemical = df['Chemical'].values
    Variant = df['Variant'].values
    Gene = df['Gene'].values
    temp = set()
    temptail = set()
    temp6 = set()
    for i in range(len(Sentence)):

        # print(i)
        matched = False
        matched2 = False
        matched3 = False
        matched = re.match(r'(.*?) (is|are) associated with (.*?) (to|of) (.*)', Sentence[i])
        if matched:
            relation = matched.group(3) + ' ' + matched.group(4)
            # +' '+matched.group(5)+' in '+matched.group(6)+' with '+matched.group(7)

            temp6.add(matched.group(5))

            tailList = nameProceeding(Chemical[i])
            tailList2 = nameProceeding(Gene[i])
            note = ''
            for j in tailList2:
                if matched.group(5).split(' ')[0] in j:
                    tailList = tailList2
                    note = matched.group(5).split(' ')[1:]

            # print(tailList)
            head = Variant[i]
            if tailList != [['']]:
                triplets.append([head, tailList, relation, note])
            if tailList2 != [['']]:
                triplets.append([head, tailList2, 'belongs to', note])

            continue
        '''if 'not associated with' not in Sentence[i]:
            print(Sentence[i])'''
        head = Variant[i]
        tailList2 = nameProceeding(Gene[i])
        note = ''
        if tailList2 != [['']]:
            triplets.append([head, tailList2, 'belongs to', note])

    '''print(temp)
    print(temptail)
    print(temp6)'''
    triplets = np.array(triplets, dtype=object)
    print(triplets.shape)
    tempset = set()
    for i in triplets:
        tempset.add(i[2])

    print(tempset)
    print(len(tempset))
    for i in tempset:
        print(i)
    triplets = pd.DataFrame(triplets, columns=['head', 'tail', 'relation','note'])
    triplets.to_csv('triplets_var_pheno.csv', index=False)

def readChemicals(path):
    df = pd.read_csv(path, sep='\t')  # use_cols=[] low_memory
    df = df.fillna('')
    print(df.columns)
    triplets = []

    # 用pd.read_csv(path,dtype='str')方法会遇到比如ID：1816变为001816的问题，所以用下面循环来转换
    for i in df.columns:
        df[i] = df[i].astype('str')

    #Chemical = df['Chemical'].values
    PharmGKB_Accession_Id=df['PharmGKB Accession Id'].values
    Name=df['Name'].values
    Generic_Names=df['Generic Names'].values
    for i in range(len(Generic_Names)):
        if Generic_Names[i]!='':
            temp=Generic_Names[i].split(',"')
            for j in range(len(temp)):
                temp[j]=temp[j].strip('"')
            Generic_Names[i]=temp

    Cross_references=df['Cross-references'].values
    for i in range(len(Cross_references)):
        if Cross_references[i]!='':
            temp=Cross_references[i].split(',"')
            for j in range(len(temp)):
                temp[j]=temp[j].strip('"')
            Cross_references[i]=temp

    External_vocabulary=df['External Vocabulary'].values
    for i in range(len(External_vocabulary)):
        if External_vocabulary[i]!='':
            temp=External_vocabulary[i].split(',"')
            for j in range(len(temp)):
                temp[j]=temp[j].strip('"').split('(')[0]
            External_vocabulary[i]=temp


    for i in range(len(PharmGKB_Accession_Id)):
        triplets.append([Name[i],PharmGKB_Accession_Id[i],'Name-PharmGKB_Id(Chemicals)'])
        triplets.append([PharmGKB_Accession_Id[i],Name[i],'PharmGKB_Id-Name(Chemicals)'])
        if Generic_Names[i]!='':
            for names in Generic_Names[i]:
                triplets.append([Name[i],names,'Synonym(Chemicals)'])
        if Cross_references[i]!='':
            for ids in Cross_references[i]:
                triplets.append([PharmGKB_Accession_Id[i],ids,'Cross_reference(Chemicals)'])
        if External_vocabulary[i]!='':
            for ids2 in External_vocabulary[i]:
                triplets.append([PharmGKB_Accession_Id[i],ids2,'External_vocabulary(Chemicals)'])

    triplets=np.array(triplets,dtype=object)
    triplets=pd.DataFrame(triplets, columns=['head', 'tail', 'relation'])
    triplets.to_csv('triplets_chemicals.csv', index=False)

def readGenes(path):
    df = pd.read_csv(path, sep='\t')  # use_cols=[] low_memory
    df = df.fillna('')
    print(df.columns)
    triplets = []

    for i in df.columns:
        df[i] = df[i].astype('str')

    PharmGKB_Accession_Id=df['PharmGKB Accession Id'].values
    NCBI_Gene_Id=df['NCBI Gene ID'].values
    HGNC_Id=df['HGNC ID'].values
    Ensembl_Id=df['Ensembl Id'].values
    Name=df['Name'].values
    Symbol=df['Symbol'].values
    Alternate_Names=df['Alternate Names'].values
    for i in range(len(Alternate_Names)):
        if Alternate_Names[i]!='':
            temp=Alternate_Names[i].split(',"')
            for j in range(len(temp)):
                temp[j]=temp[j].strip('"').split('(')[0]
            Alternate_Names[i]=temp
    Alternate_Symbols=df['Alternate Symbols'].values
    for i in range(len(Alternate_Symbols)):
        if Alternate_Symbols[i]!='':
            temp=Alternate_Symbols[i].split(',"')
            for j in range(len(temp)):
                temp[j]=temp[j].strip('"').split('(')[0]
            Alternate_Symbols[i]=temp
    Cross_references=df['Cross-references'].values
    for i in range(len(Cross_references)):
        if Cross_references[i]!='':
            temp=Cross_references[i].split(',"')
            for j in range(len(temp)):
                temp[j]=temp[j].strip('"').split('(')[0]
            Cross_references[i]=temp

    for i in range(len(PharmGKB_Accession_Id)):
        triplets.append([PharmGKB_Accession_Id[i],Name[i],'PharmGKB_Id-Name(Genes)'])
        triplets.append([PharmGKB_Accession_Id[i],Symbol[i],'PharmGKB_Id-Symbol(Genes)'])
        triplets.append([Name[i],PharmGKB_Accession_Id[i],'Name-PharmGKB_Id(Genes)'])
        triplets.append([Name[i], Symbol[i], 'Name-Symbol(Genes)'])
        triplets.append([Symbol[i],PharmGKB_Accession_Id[i],'Symbol-PharmGKB_Id(Genes)'])
        triplets.append([Symbol[i],Name[i],'Symbol-Name(Genes)'])

        triplets.append([PharmGKB_Accession_Id[i],NCBI_Gene_Id[i],'NCBI_Gene_Id(Genes)'])
        triplets.append([PharmGKB_Accession_Id[i],HGNC_Id[i],'HGNC_Id(Genes)'])
        triplets.append([PharmGKB_Accession_Id[i],Ensembl_Id[i],'Ensembl_Id(Genes)'])
        if Cross_references[i]!='':
            for ids in Cross_references[i]:
                triplets.append([PharmGKB_Accession_Id[i],ids,'Cross_reference(Genes)'])
        if Alternate_Names[i]!='':
            for names in Alternate_Names[i]:
                triplets.append([Name[i],names,'Alternate_name(Genes)'])
        if Alternate_Symbols[i]!='':
            for symbols in Alternate_Symbols[i]:
                triplets.append([Symbol[i],symbols,'Alternate_symbol(Genes)'])
    triplets = np.array(triplets, dtype=object)
    triplets = pd.DataFrame(triplets, columns=['head', 'tail', 'relation'])
    triplets.to_csv('triplets_genes.csv', index=False)

def readPhenotypes(path):
    df = pd.read_csv(path, sep='\t')  # use_cols=[] low_memory
    df = df.fillna('')
    print(df.columns)
    triplets = []

    for i in df.columns:
        df[i] = df[i].astype('str')
    PharmGKB_Accession_Id = df['PharmGKB Accession Id'].values
    Name = df['Name'].values
    Alternate_Names = df['Alternate Names'].values
    for i in range(len(Alternate_Names)):
        if Alternate_Names[i] != '':
            temp = Alternate_Names[i].split(',"')
            for j in range(len(temp)):
                temp[j] = temp[j].strip('"')
            Alternate_Names[i] = temp

    Cross_references = df['Cross-references'].values
    for i in range(len(Cross_references)):
        if Cross_references[i] != '':
            temp = Cross_references[i].split(',"')
            for j in range(len(temp)):
                temp[j] = temp[j].strip('"')
            Cross_references[i] = temp

    External_vocabulary = df['External Vocabulary'].values
    for i in range(len(External_vocabulary)):
        if External_vocabulary[i] != '':
            temp = External_vocabulary[i].split(',"')
            for j in range(len(temp)):
                temp[j] = temp[j].strip('"').split('(')[0]
            External_vocabulary[i] = temp

    for i in range(len(PharmGKB_Accession_Id)):
        triplets.append([Name[i],PharmGKB_Accession_Id[i],'Name-PharmGKB_Id(Phenotypes)'])
        triplets.append([PharmGKB_Accession_Id[i],Name[i],'PharmGKB_Id-Name(Phenotypes)'])
        if Alternate_Names[i]!='':
            for names in Alternate_Names[i]:
                triplets.append([Name[i],names,'Synonym(Phenotypes)'])
        if Cross_references[i]!='':
            for ids in Cross_references[i]:
                triplets.append([PharmGKB_Accession_Id[i],ids,'Cross_reference(Phenotypes)'])
        if External_vocabulary[i]!='':
            for ids2 in External_vocabulary[i]:
                triplets.append([PharmGKB_Accession_Id[i],ids2,'External_vocabulary(Phenotypes)'])

    triplets=np.array(triplets,dtype=object)
    triplets=pd.DataFrame(triplets, columns=['head', 'tail', 'relation'])
    triplets.to_csv('triplets_phenotypes.csv', index=False)

def readOccurrences(path):
    df = pd.read_csv(path, sep='\t')  # use_cols=[] low_memory
    df = df.fillna('')
    print(df.columns)
    triplets = []

    for i in df.columns:
        df[i] = df[i].astype('str')

    Source_Type=df['Source Type'].values
    Source_ID=df['Source ID'].values
    Source_Name=df['Source Name'].values
    Object_Type=df['Object Type'].values
    Object_ID=df['Object ID'].values
    Object_Name=df['Object Name'].values
    for i in range(len(Source_ID)):
        triplets.append([Source_ID[i], Object_ID[i], 'Contains(Occurrences)'])
        triplets.append([Object_ID[i], Source_ID[i], 'Source(Occurrences)'])
        triplets.append([Source_ID[i],Source_Name[i],'Id-Name(Occurrences)'])
        triplets.append([Source_Name[i],Source_ID[i],'Name-Id(Occurrences)'])
        triplets.append([Object_ID[i],Object_Name[i],'Id-Name(Occurrences)'])
        triplets.append([Object_Name[i],Object_ID[i],'Name-Id(Occurrences)'])

    triplets = np.array(triplets, dtype=object)
    triplets = pd.DataFrame(triplets, columns=['head', 'tail', 'relation'])
    triplets.to_csv('triplets_occurrences.csv', index=False)

def final_proceeding():
    df = pd.read_csv('triplets_chemicals.csv', sep=',')  # use_cols=[] low_memory
    for i in df.columns:
        df[i] = df[i].astype('str')
    arr=df.values
    print(arr.shape)
    for path in ['triplets_genes.csv','triplets_occurrences.csv','triplets_phenotypes.csv','triplets_var_drug.csv','triplets_var_fa.csv']:
        tempdf=pd.read_csv(path,sep=',')
        for i in tempdf.columns:
            tempdf[i]=tempdf[i].astype('str')
        if path in ['triplets_var_drug.csv','triplets_var_fa.csv']:
            arr=np.concatenate([arr,tempdf[['head','tail','relation']].values],axis=0)
            print(arr.shape)
            continue
        arr=np.concatenate([arr,tempdf.values],axis=0)
        print(arr.shape)
    entitySet=set()
    relSet=set()
    for i in range(len(arr)):
        entitySet.add(arr[i,0])
        entitySet.add(arr[i,1])
        relSet.add(arr[i,2])
    entitySet=list(entitySet)
    relSet=list(relSet)
    entityArr=np.array(entitySet).reshape(-1,1)
    tempList=range(len(entityArr))
    tempList=np.array(tempList).reshape(-1,1)
    entityArr=np.concatenate([entityArr,tempList],axis=1)
    entityArr=pd.DataFrame(entityArr,columns=['Name','Id'])
    entityArr.to_csv('triplets_entities.csv',index=False)

    relArr=np.array(relSet).reshape(-1,1)
    tempList = range(len(relArr))
    tempList = np.array(tempList).reshape(-1, 1)
    relArr = np.concatenate([relArr, tempList], axis=1)
    relArr=pd.DataFrame(relArr,columns=['Name','Id'])
    relArr.to_csv('triplets_relations.csv',index=False)

    for i in range(len(arr)):
        print(arr[i])

        arr[i,0]=entitySet.index(arr[i,0])
        arr[i, 1] = entitySet.index(arr[i, 1])
        arr[i, 2] = relSet.index(arr[i, 2])
        print(arr[i])
        print(i)
    arr=pd.DataFrame(arr,columns=['head','tail','relation'])
    arr.to_csv('triplets.csv',index=False)


readVar_drug_ann('datasets\\annotations\\var_drug_anncopy.tsv')
readVar_fa_ann('datasets\\annotations\\var_fa_ann.tsv')
readVar_pheno_ann('datasets\\annotations\\var_pheno_ann.tsv')
readChemicals('datasets\\chemicals\\chemicals.tsv')
readGenes('datasets\\genes\\genes.tsv')
readPhenotypes('datasets\\phenotypes\\phenotypes.tsv')
readOccurrences('datasets\\occurrences\\occurrences.tsv')
final_proceeding()