def trialfunction(x,y):
    print(x+ " "+y)




trialfunction("Yellow" , "Pussy")


### Functions as Arguments

def trial(x,y):
    print(x +""+y)

trial("hello" , "World")

list1 = ['car','bus','bike','scooter']

def loop(z):
    print(z*3)

def map_simple(crazy,list1):
    for items in list1:
        crazy(items)


map_simple(loop,list1)


