import pandas as pd
m = 10**5
asking_price = [2*m,0.5*m,3*m,0.25*m,m]

fair_price = [1.5*m,0.51*m,2.5*m,0.3*m,0.99*m]

ASK = pd.Series(asking_price)
FAIR = pd.Series(fair_price)

dic = {'ask':ASK , 'fair':FAIR}
data = pd.DataFrame(dic)
data['GDEAL'] = (data['fair'] - data['ask']) > 0

l=[]
for i in range(len(data['GDEAL'])):
    if data['GDEAL'][i]==False:
        l.append(i)

print(l)