import pandas as pd
import numpy as np


def sample_(threshold_list):
    for threshold in threshold_list:
        df=pd.read_csv('merged191114_'+str(threshold)+'_ID_LCS.csv')
        df=df.values #[4513:-1]
        length=0
        for i in range(4513,len(df)):
            if len(df[i,0].split(','))>2:
                length+=1

        templist=set()
        temparray=np.array(['0','0','0'],dtype=str).reshape(1,3)
        while len(templist)<0.05*length:
            ran=np.random.randint(4513,len(df))
            if len(df[ran,0].split(','))>2 and len(df[ran,0].split(','))<10:
                templist.add(ran)
                #print(len(templist))
        for i in templist:
            temparray=np.concatenate((temparray,df[i].reshape(1,3)),axis=0)

        temparray=temparray[1:,0:2]
        #print(temparray)
        final_list=np.array(['0','0'],dtype=object).reshape(1,2)
        for i in range(len(temparray)):
            #print(temparray[i])
            id_list=[]
            syn_list=[]
            ids=temparray[i,0].split(',')[1:]
            for id in ids:
                id_list.append(id)
            syns=temparray[i,1][1:-1].split('],[')
            for syn in syns:
                syn_list.append('['+syn+']')
            for j in range(len(id_list)):
                final_list=np.concatenate((final_list,np.array([str(i)+','+str(id_list[j]),syn_list[j]]).reshape(1,2)),axis=0)
                #print(np.array([str(i) + ',' + str(id_list[j]), syn_list[j]]).reshape(1, 2))

        #temparray=pd.DataFrame(temparray,columns=['ID','Syn'])
        final_list=final_list[1:]
        final_list=pd.DataFrame(final_list,columns=['ID','Syn'])

        final_list.to_csv('sample_'+str(threshold)+'.csv',index=False)


sample_([0,3,5,6,7,8,9,10])