for i in range(1,10):
    for j in range(1,i+1):
        if i==1:
           print(end='        '*8) 
        formula = '{0:1}×{1:1}={2:<2}'.format(i,j,i*j)
        print(formula, end=' ')
    print()
    print(end='        '*(8-i))
