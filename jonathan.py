import json
inputFile = open('./baskhara.jjp').read().split('\n')

reservedList = {
    '#':'reserved',
    '=':'reserved'
}
    
especialCharacterList = {
    '&':'especial',
}

separatorList = {
    ',':'separator'
}

stringsSeparators = {
    '"': 'stringSeparator'
}

lexicaFile = []
obj = {  'lineValues': [] }

inString = False
inNumber = False

stringConcat = ""
stringNumber = ""

def checkInString(character):
    if(inString):
        global stringConcat
        stringConcat +=  character

def checkInNumber(character):
    if(inString):
        global stringConcat
        stringConcat +=  character

def setLexicaObjList(listLexicaR,charValue):
    global obj

    objLexica = {'type':listLexicaR[charValue], 'value':charValue }
    obj['lineValues'].append(objLexica)


def isNumber(value):
    try:
        float(value)
        print("ddd")
        return True
    except:
        return False

def setObjString():
    global inString
    global obj

    inString = False
    print("dfsdfsfs")
    objLexica = {'type':'string', 'value':stringConcat }
    obj['lineValues'].append(objLexica)

def basicTokens(charValue):
    global inString
    global stringConcat
    global inString
    global inNumber

    # if(inString):
    #     return

    if(charValue in stringsSeparators):
        if(not inString):
            stringConcat = ""
            inString = True
        setLexicaObjList(stringsSeparators,charValue)
    elif(charValue in reservedList):
        setLexicaObjList(reservedList,charValue)
    elif(charValue in especialCharacterList):
        setLexicaObjList(especialCharacterList,charValue)
    elif(charValue in separatorList):
        setLexicaObjList(separatorList,charValue)


for line in inputFile:

    for index in range(len(line)):
        charValue = line[index]
        isNotEnd = index + 1 < len(line)

        # if(isNumber(charValue)):
        #     if(isNotEnd):
        #         if(isNumber(line[index + 1])):
        #             stringNumber += charValue
        #         else:
        #             objLexica = {'type':'number', 'value':stringNumber}
        #             obj['lineValues'].append(objLexica)
        print( inString)
        if(isNumber(charValue) and (not inString)):
            print("entrou aqui")
            objLexica = {'type':'number', 'value':charValue }
            obj['lineValues'].append(objLexica)
        else:
            checkInString(charValue)
            basicTokens(charValue)

        if(isNotEnd):
            if(line[index + 1] in stringsSeparators and inString):
                setObjString()
                           

    if(len(obj['lineValues']) > 0):    
        lexicaFile.append(obj)
        obj = {  'lineValues': [] }
    


# print(json.dumps(lexicaFile))

    
