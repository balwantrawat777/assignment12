#QUESTION 1
import pandas as pd
a=pd.DataFrame({'name':"balwant",'age':21,'email_id':'balwantrawat333@gmail.com','phone_number':[1234567890]})
b=pd.DataFrame({'name':"danish",'age':22,'email_id':'danishgupta263@gmail.com','phone_number':[9876543210]})
print(a.append(b))


#QUESTION 2

import pandas as pd
weather=pd.read_csv('weather.csv')
print(weather.head(5))
print(weather.head(10))
print(weather.mean())
print(weather.median())
print(weather.mode())
print(weather.var())
print(weather.std())
print(weather.tail(5))


w=weather['MinTemp']
print(w.mean())
print(w.tail(5))
print(w.mode())
print(w.var())
print(w.std())
