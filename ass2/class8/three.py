import random

coin_value=["head","tail"]

hcount=0
tcount=0
for num in range(100):
    result=random.choice(coin_value)
    if result=="hesd":
        hcount=hcount+1
    elif result=="tail":
        tcount=tcount=1
        print("head count",hcount)
        print("tail count",tcount)  