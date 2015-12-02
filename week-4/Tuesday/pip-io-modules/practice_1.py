zen_order_file = open('reversed_zen_order.txt', 'r')
x = open('normal_zen_order.txt', 'w')

lines = zen_order_file.readlines()
reversed_lines = lines[::-1]

output = ' '.join(reversed_lines)

zen_order_file.close()
x.write(output)
x.close()

print(output)
