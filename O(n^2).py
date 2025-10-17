def test(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            print("#",end="")
            iteration+=1
        print("")
    print("When n is",n,"Iteration=",iteration)

test(5)
test(4)
test(3)

print("\n With every n the time taken= n^2")
