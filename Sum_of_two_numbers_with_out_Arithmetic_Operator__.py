def add_without_plus_operator(a, b):
    while b != 0:
        data = a & b
        a = a ^ b
        b = data << 1
    return a
a,b=map(int,input().split())
print(add_without_plus_operator(a, b))