import time
def fib(mymax):
    a,b=0,1
    while True:
        c=a+b
        if c<mymax:
            yield c
            a=b
            b=c
        else:
            break
gen=fib(10)
time.sleep(4)
for i in gen:
    print(i)



# def simpleGenfun():
#     yield 1           
#     yield 2                    
  
# # Driver code to check above generator function
# for value in simpleGenfun():
#     print(value)

