from ..models.LexicaModel import LexicaModel

class LexicaController:
    def __init__(self, confWords):
        self.lexicaModel = LexicaModel(confWords['reservedWords'], confWords['especialCharacter'], confWords['stringSeparators'])
    
    
    