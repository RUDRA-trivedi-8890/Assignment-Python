import pandas as pd

data = {
    'John': [True, False, True, False, True, True, False, False, True, True],
    'Judy': [False, True, True, True, False, True, False, True, False, True]
}

df = pd.DataFrame(data)

df['days_till_party'] = df['John'] & df['Judy']

print(df['days_till_party'])

k=[]
m=0
for i in range(len(df['days_till_party'])):
     if(df['days_till_party'][i]==True):
         k.append(m)
         m=0
     else:
         m-=1
i=0
p=0
while(i<len(k)):
    if(k[i]==0):
        df['days_till_party'][p] = 0
        p+=1
        i+=1
    else:
        df['days_till_party'][p] = (k[i]*-1)
        k[i]+=1
        p+=1
        
print(df)
        
     