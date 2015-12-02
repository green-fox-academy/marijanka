zen_lines_file = open('reversed_zen_lines.txt', 'r')
x = open('normal_zen_lines.txt', 'w')

output = ""

for line in zen_lines_file:
    line = line.rstrip()
    new_line = line[::-1]
    output += new_line + '\n'

zen_lines_file.close()
x.write(output)
x.close()

print(output)
