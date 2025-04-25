import pandas as pd
import datetime

dt1 = pd.to_datetime('2012-01-15')
print("a) DateTime for Jan 15 2012:", dt1)

dt2 = pd.to_datetime('2012-01-15 21:20')
print("b) Specific date and time 9:20 PM:", dt2)

dt3 = pd.Timestamp.now()
print("c) Local date and time:", dt3)

dt4 = pd.to_datetime('2025-04-12').date()
print("d) Date without time:", dt4)

dt5 = pd.Timestamp.now().date()
print("e) Current date:", dt5)

dt6 = pd.Timestamp.now().time()
print("f) Time from current datetime:", dt6)

dt7 = datetime.datetime.now().time()
print("g) Current local time:", dt7)
