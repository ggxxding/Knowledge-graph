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
    drugs=pd.read_csv('datasets/drugs/drugs.tsv',sep='\t').fillna('')
    phenotypes=pd.read_csv('datasets/phenotypes/phenotypes.tsv',sep='\t').fillna('')

    phenotypesAlt=phenotypes['Alternate Names'].values
    arr1=drugs.values
    arr2=chemicals.values
    count=0
    for i in range(len(drugs)):
        for j in range(len(chemicals)):
            if arr1[i,0]==arr2[j,0]:
                count+=1
        print(i)
    print(count,len(arr1),len(arr2))
process()