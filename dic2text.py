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
    lines = [' Rank | Emoji | Uses ']
    line = ''
    index = 0
    rank = 1
    previousValue = next(iter(dic.values()))
    for key, value in dic.items():
        if value != previousValue:
            rank += 1
        if index < 5:
            line += ordinal_number(rank) + '\t'
        line += str(key) + '\t' + str(value).rjust(4) + '\t'
        if index < 5 or index % width == 4:
            lines.append(line)
            line = ''
        index += 1
        previousValue = value
    return lines