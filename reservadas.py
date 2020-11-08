reserved = [
    "float",
    "int",
    "void",
    "boolean",
    "str",
    "if",
    "repeat",
    "write",
    "read"
    "in"
    "jjSqr"
    "else"
    "#rep#",
    "#if#"
]

especialCharacters = [
    '&',
    '*',
    '-',
    '+',
    '<',
    '>'
    "=",
    "#",
    "."
]

separators = [
    ' ',
    ',',
    ';',
    '{',
    '}',
    '(',
    ')'
]

stringsSeparators = {
    '"': '"',
    '\'': '\''
}


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


def removeEmpty(arrayLine):
    result = []
    for objLine in arrayLine:
        if not ('' in objLine.keys() or ' ' in objLine.keys()):
            result.append(objLine)
    return result


def getStrings(line):
    result = []
    init = None
    last = 0
    for index in range(len(line)):
        if line[index] in stringsSeparators and init == None:
            init = index
            if not last:
                result.append({f'{line[:init]}': None})
        elif init != None and line[index] == stringsSeparators[line[init]]:
            if last:
                result.append({f"{line[last:init]}": None})
            result.append({f"{line[init:index + 1]}": 'string'})
            init = None
            last = index + 1
    result.append({f"{line[last:]}": None})
    return removeEmpty(result)


def finderCharacter(arrayLine, findItens, typeName):
    result = []
    for obj in arrayLine:
        for key in obj:
            if not obj[key]:
                lastEspecial = 0
                allItens = []
                for findItem in findItens:
                    positions = findAllIndexes(key, findItem)
                    allItens = allItens + positions
                allItens.sort()
                for item in allItens:
                    result.append({f"{key[lastEspecial:item].strip()}": None})
                    lastEspecial = item + 1
                    result.append({f"{key[item]}": typeName})
                result.append({f"{key[lastEspecial:].strip()}": None})

            else:
                result.append(obj)
    return removeEmpty(result)


def classify(arrayLine):
    result = []
    for value in arrayLine:
        for key in value:
            if value[key] != None:
                result.append(value)
            elif key in reserved:
                result.append({f"{key}": 'reserved'})
            elif isNumber(key):
                result.append({f"{key}": 'number'})
            else:
                result.append({f"{key}": 'variable'})
    return result


def getLineValues(line):
    newLine = getStrings(line)
    newLine = finderCharacter(newLine, especialCharacters, 'especialCharacter')
    newLine = finderCharacter(newLine, separators, 'separator')
    newLine = classify(newLine)
    return newLine
