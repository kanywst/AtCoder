weathers =['Sunny','Cloudy','Rainy']

S = input()

pos = (weathers.index(S) + 1) % 3
print(weathers[pos])
