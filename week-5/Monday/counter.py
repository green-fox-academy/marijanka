def count_letters(input_string):
    output = {}
    for i in input_string:
        if i not in output:
            output[i] = 1
        else:
            output[i] += 1
    return output
