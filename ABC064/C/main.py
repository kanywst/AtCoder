N = int(input())
a = list(map(int,input().split()))

d = {}
cnt = 0
for i in range(N):
    if 1<=a[i]<=399:
        if 'gray' in d.keys():
            d['gray'] += 1
        else:
            d['gray'] = 1
    elif 400<=a[i]<=799:
        if 'brown' in d.keys():
            d['brown'] += 1
        else:
            d['brown'] = 1
    elif 800<=a[i]<=1199:
        if 'green' in d.keys():
            d['green'] += 1
        else:
            d['green'] = 1
    elif 1200<=a[i]<=1599:
        if 'light_blue' in d.keys():
            d['light_blue'] += 1
        else:
            d['light_blue'] = 1
    elif 1600<=a[i]<=1999:
        if 'blue' in d.keys():
            d['blue'] += 1
        else:
            d['blue'] = 1
    elif 2000<=a[i]<=2399:
        if 'yellow' in d.keys():
            d['yellow'] += 1
        else:
            d['yellow'] = 1
    elif 2400<=a[i]<=2799:
        if 'orange' in d.keys():
            d['orange'] += 1
        else:
            d['orange'] = 1
    elif 2800<=a[i]<=3199:
        if 'red' in d.keys():
            d['red'] += 1
        else:
            d['red'] = 1
    else:
        cnt += 1
if len(d) == 0:
    print(1,len(d)+cnt)
else:
    print(len(d),len(d)+cnt)
