arr = {}
n = int(input())
for _ in range(0,n):
    x,y = input().split()
    arr[x]= int(y)

while(True):
    try:
        name = input()
        if name in arr:
            print (name +"="+ str(arr[name]))
        else:
             print("Not found")
    except:
        break
