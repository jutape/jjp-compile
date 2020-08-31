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

# stringsSeparators = {
#     '"': '"'
# }

lexicaFile = []

for line in inputFile:

    for index in range(len(line)):
        charValue = line[index]



        if(charValue in reservedList):
            objLexica = {'type':reservedList[charValue], 'value':charValue }
            lexicaFile.append(objLexica)

        elif(charValue in especialCharacterList):
            objLexica = {'type':especialCharacterList[charValue], 'value':charValue }
            lexicaFile.append(objLexica)

        elif(charValue in separatorList):
            objLexica = {'type':separatorList[charValue], 'value':charValue }
            lexicaFile.append(objLexica)





# print(reserved)
# # print(reserved[key])
print(lexicaFile)
    
  