def reverse_r(ls):
    
    if len(ls) == 0:
        
        return []
    
    return reverse_r(ls[1:]) + ls[0:1]


def reverse_i(ls):
    
    rev = []
    
    for elem in ls:
        
        rev = [elem] + rev
        
    return rev

if __name__ == '__main__':
    
    print(reverse_r([1,2,3,4,5]))
    print(reverse_i([1,2,3,4,5,6]))
