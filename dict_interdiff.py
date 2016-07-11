d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
# Output Example:
# dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
def dict_interdiff(d1, d2):
    f = lambda a, b: a+b # == def f(a,b): return a+b
    output01 = dict()
    output02 = dict()
    print('D1:', d1)
    print('D2: ', d2)
    num = 0
    for i in d1:
        for j in d2:
            if i == j:
                num +=1
                #print(f(d1[i],d2[j]))
                output01[i] = f(d1[i],d2[j]) 

    print('Output01: ', output01)
    return False

print(dict_interdiff(d1, d2))
