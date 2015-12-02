input_string = 'EBG13 rknzcyr.'
output = ''

for word in input_string:
    for char in word:
        if ord(char) < 65:
            output += char
        else:
            if ('A' <= char and char < 'M') or ('a' <= char and char < 'm'):
                output += chr(ord(char) + 13)
            else:
                output += chr(ord(char) - 13)

print(output)
