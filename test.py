import pandas as pd
import numpy as np
def process():

    relationships=pd.read_csv('datasets/relationships/relationships.tsv',sep='\t').fillna('')
    clinical_ann=pd.read_csv('datasets/annotations/clinical_ann.tsv',sep='\t').fillna('')
    clinical_ann_metadata=pd.read_csv('datasets/annotations/clinical_ann_metadata.tsv',sep='\t').fillna('')
    var_drug_ann=pd.read_csv('datasets/annotations/var_drug_anncopy.tsv',sep='\t').fillna('')
    var_fa_ann=pd.read_csv('datasets/annotations/var_fa_ann.tsv',sep='\t').fillna('')
    var_pheno_ann=pd.read_csv('datasets/annotations/var_pheno_ann.tsv',sep='\t').fillna('')

    variants=pd.read_csv('datasets/variants/variants.tsv',sep='\t').fillna('')
    chemicals=pd.read_csv('datasets/chemicals/chemicals.tsv',sep='\t').fillna('')
    #chemicals 6 10
    phenotypes=pd.read_csv('datasets/phenotypes/phenotypes.tsv',sep='\t').fillna('')

    phenotypesAlt=phenotypes['Alternate Names'].values
    print(phenotypesAlt)
    for index,i in enumerate(phenotypesAlt):
        if i!='':
            print(i)
            temp=i.split(',"')
            if len(temp)>1:
                for j in range(1,len(temp)):
                    temp[j]=temp[j].rstrip('"')
            print(temp)
            phenotypesAlt[index]=temp
    print(phenotypes['Alternate Names'])
    #phenotypes['ii']='"""'+phenotypes['Name']+'""","""'+phenotypes['Alternate Names']+'"""'
    #print(phenotypes.values[9])

process()