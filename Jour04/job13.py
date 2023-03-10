L = [10,20,30,20,10,50,60,40,80,50,40]
news =[]

for i in L:
    if i not in news:
        news = news + [i]

print(news)
