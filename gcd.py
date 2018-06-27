def gcd(a, b):
    
    
    if b == 0:
        
        return a
    
    return gcd(b, a%b)

if __name__ == '__main__':
    
    print(gcd(0,5))
    print(gcd(10,5))
    print(gcd(16,24))
