# def adder(array):
#     list_output = []
#     for i in array:
#         list_output.append(i + 1)
#     return list_output

# def adder(list_output):
#     def add(n):
#         return n + 1
#     return list(map(add, list_output))

def adder(array):
    return list(map(lambda x: x + 1, array))

# def divider(array):
#   list_output = []
#       for i in array:
#           if i % 3 == 0:
#               list_output.append(i)
#       return list_output

def divider(array):
    return list(filter(lambda x: x % 3 == 0, array))
