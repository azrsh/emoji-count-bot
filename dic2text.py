def convert(dic, width = 5):
    result = ''
    index = 0
    for key, value in dic.items():
        result += str(key) + ' : ' + str(value).rjust(4) + '    '
        if index % width == width - 1:
            result += '\n'
        index += 1
    return result

def ordinal_number(i):
    return {1:"1 st", 2:"2 nd", 3:"3 rd"}.get(i) or str(i) + " th"

def convert_to_ranking(dic, width=5):
    result = '  Rank  |  Emoji  |    Uses    \n'
    index = 1
    for key, value in dic.items():
        if index <= 5:
            result += ordinal_number(index) + '\t'
        result += str(key) + '\t' + str(value).rjust(4) + '\t'
        if index <= 5 or index % width == 0:
            result += '\n'
        index += 1
    return result