a=[2,5,7,8,4,6,3]
for j in range(len(a)):
    i=0
    swapped=False
    while i<len(a)-1:
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
            swapped=True
        i+=1
    if swapped==False:
        break
print(a)



#secnd code
def cont(x,list):
    return(list.count(x))
x=4
list=(1,4,4,6,7)
result=cont(x,list)
print(result)




#third code
def list1(x,a):
    for j in range(len(a)):
        if a[j]==x:
            print("found ",x,"at position",j)
            return
    print("not found")
x=7
a=[1,3,5,7,8]
list1(x,a)



#fourth code
def lists(a,b):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j]:
                print('true')
                return
    print("false")

a=[2,4,6,8,10]
b=[2,9,12,15,18]
lists(a,b)



#fifth code
def lists(a,b):
    a.sort()
    b.sort()
    print(a)
    print(b)
    combined=a+b
    combined.sort()
    print(combined)
    return
a=[4,2,6,8,10]
b=[9,3,12,15,18]
lists(a,b)
