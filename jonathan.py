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



inString = False

stringConcat = ""
def checkInString(character):
    if(inString):
        global stringConcat
        stringConcat +=  character


obj = {  'lineValues': [] }
def setLexicaObjList(listLexicaR,charValue):
    objLexica = {'type':listLexicaR[charValue], 'value':charValue }
    obj['lineValues'].append(objLexica)


def basicTokens(charValue):
    global inString
    global stringConcat
    global inString

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

        if(index + 1 < len(line)):
            if(line[index + 1] in stringsSeparators and inString):
                checkInString(charValue)
                inString = False
                objLexica = {'type':'string', 'value':stringConcat }
                obj['lineValues'].append(objLexica)
                
        checkInString(charValue)
        basicTokens(charValue)

    if(len(obj['lineValues']) > 0):    
        lexicaFile.append(obj)
        obj = {  'lineValues': [] }
    

def isNumber(n):
    try:  
        return type(float(n)) == float 
    except:
        return False


#dasdsad
print(json.dumps(lexicaFile))

    
