import toExcel
import merge1
import time
import merge2
import merge3

nameDO='datasets\DiseaseOntology_20190627.csv'
nameICDCM='datasets\ICD10CM2019_20180626-USA.csv'
nameICD='datasets\ICD102016_20180704-WHO.csv'
nameMeSH='datasets\MeSH2018_20180713.csv'
nameChemicals='datasets\chemicals\chemicals.tsv'
nameDrugs='datasets\drugs\drugs.tsv'
namePhenotypes='datasets\phenotypes\phenotypes.tsv'
toExcel.filesProceeding(nameDO,nameICDCM,nameICD,nameMeSH,\
                nameChemicals,nameDrugs,namePhenotypes)


'''start=time.perf_counter()
dur=[]
for i in [0,3,5,6,7,8,9,10]:
    merge1.contrast(i)
    merge2.idProcess('merged191114_' + str(i) + '.csv')
    merge3.idProcess('merged191114_' + str(i) + '_ID.csv')
    dur.append(time.perf_counter())

print("time:",dur[0]-start,'\n',
      dur[1]-dur[0],'\n',
      dur[2]-dur[1],'\n',
      dur[3]-dur[2],'\n',
      dur[4]-dur[3],'\n',
      dur[5]-dur[4],'\n',
      dur[6]-dur[5],'\n',
      dur[7]-dur[6])'''
merge1.contrast(0)
merge2.idProcess('merged191114_' + str(i) + '.csv')
merge3.idProcess('merged191114_' + str(i) + '_ID.csv')