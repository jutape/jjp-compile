def removeEmpty(arrayLine):
    result = []
    for objLine in arrayLine:
        if not ('' in objLine.keys() or ' ' in objLine.keys()):
            result.append(objLine)
    return result


def isNumber(value):
    try:
        float(value)
        return True
    except:
        return False


def findAllIndexes(input_str, search_str):
    l1 = []
    length = len(input_str)
    index = 0
    while index < length:
        i = input_str.find(search_str, index)
        if i == -1:
            return l1
        l1.append(i)
        index = i + 1
    return l1
