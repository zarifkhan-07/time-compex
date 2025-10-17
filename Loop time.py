def myfunction(n):
    iteration=0
    for i in range(0,n+1):
        iteration+=1
    print("First loop")
    print("\n For",n,"the iteration is:",iteration)

    j=1
    while(j<=n+1):
        j=j*2
        iteration+=1
    print("Second loop",j)
    
    for i in range(0,100):
        iteration+=1
    print("Third loop")

myfunction(23)
myfunction(256)
myfunction(230)