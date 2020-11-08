# -*- coding: utf-8 -*-
import reservadas
import json

inputFile = open('./baskhara2.jjp').read().split('\n')

finish = []
for line in inputFile[:]:
    results = reservadas.getLineValues(line)
    finish.append(results)

def declarationWithAssignment(linha):
    count = 0
    lineSintatica = ''
    antType = ''
    nameVar = ''
    valueVar = ''
    antVal = ''
    add = False
    for result in linha:
        count += 1
        for key in result:
            typeLexica = result[key]
            valueLexica = key

            ''' GAMBIARRA '''
            if(key == '='):
                typeLexica = 'especialCharacter'
            ''' GAMBIARRA '''

            if(count == 1 and typeLexica != 'variable' and  typeLexica != 'reserved' and  key == '#' ):
                raise Exception('Erro de sintatica')
                # print('Erro de sintatica')

            if(antType == 'reserved' and typeLexica != 'variable'):
                raise Exception('Erro de sintatica, falta variavel!')
                # print('Erro de sintatica, falta variavel!')

            if(antType == 'variable'  and typeLexica != 'especialCharacter'):
                print(result)
                raise Exception('Erro de sintatica,  especial character  esperado!')
                # print('Erro de sintatica,  especial character  esperado!')

            if(antType == 'especialCharacter' and typeLexica != 'variable' and typeLexica != 'number' and typeLexica != 'string'):
                raise Exception('Erro de sintatica, esperava outro tipo ')
                # print('Erro de sintatica, esperava outro tipo ')

            if((antType == 'number' or antType == 'string') and  typeLexica != 'especialCharacter'):
                raise Exception('Erro de sintatica, esperava especial character')
                # print('Erro de sintatica, esperava especial character')
            
            if(valueLexica != '=' and nameVar != '' and typeLexica != 'variable'):
                variaveisAtivas[str(nameVar)]['value'] += valueLexica

            if(typeLexica == 'variable'):
                if(valueLexica in variaveisAtivas):
                    variaveisAtivas[str(nameVar)]['value'] +=  variaveisAtivas[valueLexica]['value']
                else:
                    nameVar = valueLexica
                    variaveisAtivas[str(nameVar)] = {}
                    variaveisAtivas[str(nameVar)]['type'] = antVal
                    variaveisAtivas[str(nameVar)]['value'] = ''

            antVal = valueLexica
            antType = typeLexica

def teste(arr1, arr2):
    for num in range(len(arr1)):
        if arr1[num] in arr2:
            return True
    return False

sintatico = []
variaveisAtivas = {}
for i in range(len(finish[:])):
    # i += 1
    

   

    # objAnalizer= {
    #     'especialCharacter': 0,
    #     'separator': 0,
    #     'reserved': 0,
    #     'variable': 0,
    #     'number': 0,
    #     'string': 0,
    #     'haveEqual': False  
    # }
    objAnalizer = []
    logicNames = ['if', 'repeat']
    logicEnds = ["#rep#", "#if#", "else"]
    isLogicEnd = False
    line = ''
    for result in finish[i]:
        for key in result:
            typeLexica = result[key]
            ''' GAMBIARRA '''
            if(key == '='):
                typeLexica = 'especialCharacter'
            ''' GAMBIARRA '''
            objAnalizer.append(typeLexica)
            if key == '=' or key in logicNames:
                objAnalizer.append(key)
            line += key
            if line in logicEnds:
                isLogicEnd = True

    if(isLogicEnd):
        print('Fim função condicional')
    elif ('reserved' in objAnalizer and objAnalizer[0] == 'reserved') and 'variable' in objAnalizer and '=' in objAnalizer: 
        print('declaração com atribuição!')
        declarationWithAssignment(finish[i])
    elif ('reserved' in objAnalizer and objAnalizer[0] == 'reserved') and 'variable' in objAnalizer and not 'separator' in objAnalizer:
        print('Declaração de variavel')
        declarationWithAssignment(finish[i])
    elif 'variable' in objAnalizer and '=' in objAnalizer:
        print('atribuição!')
        declarationWithAssignment(finish[i])
    elif ('reserved' in objAnalizer and teste(logicNames, objAnalizer)):
        print('Funcão condicional')
    elif ('reserved' in objAnalizer and objAnalizer[0] == 'reserved') and 'separator' in objAnalizer:
        print('chamada de função')
    

    
exit()



# print(variaveisAtivas)
    # print("entrou here")
    # print(i)
    # print(finish[i])
#     for value in finish[i]:


#         print(value['10'])
# print(json.dumps(finish))