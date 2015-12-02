def Xbonacci(signature,n):
    x = len(signature)
    if n <= x:
        return signature[:n]
    else:
        while n > x:
            xibon_num = 0
            for i in signature[len(signature)-x:]:
                xibon_num = xibon_num + i
            signature.append(xibon_num)
            n -= 1
        return signature

# def Xbonacci(signature,n):
#     output, x = signature[:n], len(signature)
#     while len(output) < n:
#         output.append(sum(output[-x:]))
#     return output
