def sum_r(ls):
    if len(ls) == 0:
        return 0
    return ls[0] + sum_r(ls[1:])

def sum_i(ls):
    sum = 0
    for num in ls:
        sum += num  
    return sum

if __name__ == '__main__':
    print(sum_i([1,2,3,4,5]))
    
if __name__ == '__main__':
    print(sum_r([1,2,3,4,5,6]))