import pandas as pd

x=['x','y','t','AaBa', 'Baca', 'CABA', None, 'bird', 'horse', 'dog']
x=[item for item in x if item is not None]
# dic = {'upper':y, }
a = pd.Series(x)
y=[]
k=[]
lens=[]
dic = {'upper':y,'lower':k ,'length':lens}
for i in x:
    if(i==None):
        continue
    else:
        dic['upper'].append(i.upper())
uppper = pd.Series(y)
# print(uppper)
for i in x:
    if(i==None):
        continue
    else:
        dic['lower'].append(i.lower())
# print(lower)
for i in x:
    lens.append(len(i))
ans =pd.DataFrame(dic)
print(ans)