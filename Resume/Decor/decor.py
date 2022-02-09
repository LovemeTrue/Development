def decor(func):
    try:
        func()
    except:
        print("Error in function")

@decor
def thefunc(listData):
    return (listData[4])
