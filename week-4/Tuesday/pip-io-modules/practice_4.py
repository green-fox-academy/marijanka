encoded_lines_file = open("encoded_zen_lines.txt", "r")
x = open('normal_coded_chars.txt', 'w')

lines = encoded_lines_file.readlines()

output = ""
for line in lines:
    for char in line:
        if char == ' ' or char == '\n':
            output += char
        else:
            output += chr(ord(char) - 1)

encoded_lines_file.close()
x.write(output)
x.close()

print(output)
