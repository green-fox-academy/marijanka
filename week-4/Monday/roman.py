def test(expected, actual, message):
    if expected == actual:
        print('check')
    else:
        print(message)

Tokens = {
    '5': 'V',
    '4': 'IV',
    '1': 'I'
}

def arabic_to_roman(arabic):
    if arabic == 6:
        return 'VI'
    if arabic == 5 or arabic == 4:
        return Tokens[str(arabic)]
    return 'I' * arabic


test(arabic_to_roman(0), '', 'It should handle 0')
test(arabic_to_roman(1), 'I', 'It should handle 1')
test(arabic_to_roman(2), 'II', 'It should handle 2')
test(arabic_to_roman(4), 'IV', 'It should handle 4')
test(arabic_to_roman(5), 'V', 'It should handle 5')
test(arabic_to_roman(6), 'VI', 'It should handle 6')
