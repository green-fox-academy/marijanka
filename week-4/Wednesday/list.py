

def wc(filename):
    input_file = open('alma.txt')
    text_lines = input_file.read()
    line_count = len(text_lines.split('\n'))
    input_file.close()
    return (line_count, len(text_lines))

print(wc(filename))
