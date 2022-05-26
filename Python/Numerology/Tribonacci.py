def tribonacci(signature, n):
    y = 0
    if n == 0:
        return signature
    for x in range(n):
        for signature in signature[y]:
            print(signature[y] + signature[y+1] + signature[y+2])
            y = y + 1

tribonacci([1, 1, 1], 5)