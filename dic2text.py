def convert(dic, width = 5):
    result = ''
    index = 0
    for key, value in dic.items():
        result += str(key) + ' : ' + str(value).rjust(4) + '    '
        if index % width == width - 1:
            result += '\n'
        index += 1
    return result