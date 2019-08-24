import random
print('당신의 ㄱㅊ 길이는?',end='')
d=input()
if d=='':
    print(' ♤')
    P=random.choice([' ll',' ll',' ll',' ll',' ll',' ll',' OO'])
    if P==' OO':
        print(' ll')
        print(P)
    while P==' ll':
        r=random.choice([' ll',' ll',' ll',' ll',' ll',' ll',' OO'])
        print(r)
        if r==' OO':
            break
