x = int(input())

for _ in range(x):
    
    s = input()
    for i in range(len(s)):
        if i%2 == 0:
            print(s[i],end='')

    print(' ',end ='')
    for i in range(len(s)):
        if i%2 != 0:
            print(s[i],end='')
    print('')
