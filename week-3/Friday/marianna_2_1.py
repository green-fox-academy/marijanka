def search_palindromes(string):
    words_list = string.split(' ')
    return search_list(words_list)

def search_list(list):
    result_list = []
    for i in list:
        if i == i[::-1] and len(i) >= 3:
            result_list.append(i)
    return print(result_list)
