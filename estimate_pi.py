import math

def estimate_pi():
    sum = 0
    k = 0
    error = math.pow(10, -15)
    while True:
        num = math.factorial(4*k) * (1103+26390*k)
        den = math.pow(math.factorial(k), 4) * math.pow(396, 4*k)
        term = num / den
        sum += term
        k += 1
        if term < error:
            break

    return 9801 / (2 * math.sqrt(2) * sum)

if __name__ == '__main__':
    print(estimate_pi())
