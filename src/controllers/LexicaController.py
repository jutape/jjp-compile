from ..models.LexicaModel import LexicaModel
from ..utils import utils


class LexicaController:
    def __init__(self, confWords):
        self.lexicaModel = LexicaModel(confWords['reservedWords'], confWords['especialCharacter'],
                                       confWords['stringSeparators'], confWords['separators'])

    def processLine(self, line):
        newLine = self.getStrings(line)
        newLine = self.finderCharacter(newLine, self.lexicaModel.getEspecialChars(), 'especialCharacter')
        newLine = self.finderCharacter(newLine, self.lexicaModel.getSeparators(), 'separator')
        newLine = self.classify(newLine)
        return newLine

    def getStrings(self, line):
        result = []
        init = None
        last = 0
        for index in range(len(line)):
            if line[index] in self.lexicaModel.getStringSeparators() and init is None:
                init = index
                if not last:
                    result.append({f'{line[:init]}': None})
            elif init is not None and line[index] == self.lexicaModel.getStringSeparators()[line[init]]:
                if last:
                    result.append({f"{line[last:init]}": None})
                result.append({f"{line[init:index + 1]}": 'string'})
                init = None
                last = index + 1
        result.append({f"{line[last:]}": None})
        return utils.removeEmpty(result)

    def finderCharacter(self, arrayLine, findItens, typeName):
        result = []
        for obj in arrayLine:
            for key in obj:
                if not obj[key]:
                    lastEspecial = 0
                    allItens = []
                    for findItem in findItens:
                        positions = utils.findAllIndexes(key, findItem)
                        allItens = allItens + positions
                    allItens.sort()
                    for item in allItens:
                        result.append({f"{key[lastEspecial:item].strip()}": None})
                        lastEspecial = item + 1
                        result.append({f"{key[item]}": typeName})
                    result.append({f"{key[lastEspecial:].strip()}": None})
                else:
                    result.append(obj)
        return utils.removeEmpty(result)

    def classify(self, arrayLine):
        result = []
        for value in arrayLine:
            for key in value:
                if value[key] is not None:
                    result.append(value)
                elif key in self.lexicaModel.getReserveds():
                    result.append({f"{key}": 'reserved'})
                elif utils.isNumber(key):
                    result.append({f"{key}": 'number'})
                else:
                    result.append({f"{key}": 'variable'})
        return result
