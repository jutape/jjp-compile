# -*- coding: utf-8 -*-
import reservadas
import json

inputFile = open('./baskhara2.jjp').read().split('\n')

finish = []
for line in inputFile[:]:
    results = reservadas.getLineValues(line)
    finish.append(results)

# for index in range(len(finish)):
#     for i in range(len(finish[index])):
#         if list(finish[0][i].keys())[0] == '=':
#             finish[0][i][list(finish[0][i].keys())[0]] = 'especialCharacter'
    # for result in results:
    #     for key in result:
    #  	    print(f'<{key},{result[key]}>')


# print(finish[1])

    # objLexica = {'type':'string', 'value':stringConcat }
    # obj['lineValues'].append(objLexica)


sintatico = []
variaveisAtivas = {}
for i in range(len(finish[:])):
    # i += 1
    count = 0

    lineSintatica = ''

    antType = ''
    nameVar = ''
    valueVar = ''
    antVal = ''
    add = False

    for result in finish[i]:
        count += 1

        ''''
        Fazer uma analizador que verifica qual é o contexto da linha
        EX:
        int a = 1 ----- declaração de variavel
        write(a) ----- chamada de funcao
        int a = read() ------ declaração de variavel com chamada de função 
        ''''

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

print(variaveisAtivas)
    # print("entrou here")
    # print(i)
    # print(finish[i])
#     for value in finish[i]:


#         print(value['10'])
# print(json.dumps(finish))