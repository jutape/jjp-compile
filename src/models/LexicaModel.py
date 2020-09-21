class LexicaModel:
    def __init__(self, reservedWords, especialCharacter, stringSeparators):
        self.reserveds = reservedWords
        self.especialCharacters = especialCharacter
        self.stringSeparators = stringSeparators
    
    def getReserveds(self):
        return self.reserveds
    
    def getEspecialChars(self):
        return self.especialCharacters
    
    def GetStringSeparators(self):
        return self.stringSeparators
