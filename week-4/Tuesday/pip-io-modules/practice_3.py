duplicated_chars_file = open('duplicated_chars.txt', 'r')
x = open('normal_zen_chars.txt', 'w')
a = '\n'

lines = duplicated_chars_file.readlines()
output = ''

for line in lines:
    if line == a:
        output += line
    else:
        output += line[::2]

duplicated_chars_file.close()
x.write(output)
x.close()

print(output)
