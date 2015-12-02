def reverse(in_list):
    output = []
    i = 0
    while i < len(in_list):
        output.append(in_list[-i-1])
        i += 1
    return output

output = reverse([1, 2, 3, 4])
print(output)
