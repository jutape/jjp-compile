class LexicaModel:
    def __init__(self, reservedWords, especialCharacter, stringSeparators, separators):
        self.reserveds = reservedWords
        self.especialCharacters = especialCharacter
        self.stringSeparators = stringSeparators
        self.separators = separators
    
    def getReserveds(self):
        return self.reserveds
    
    def getEspecialChars(self):
        return self.especialCharacters
    
    def getStringSeparators(self):
        return self.stringSeparators
    
    def getSeparators(self):
        return self.separators
