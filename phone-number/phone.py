class Phone:
    
    number = '0000000000'

    def __init__(self, numStr):
        numStr = numStr.translate(None, ' ()-.')
        if len(numStr) == 10:
            self.number = numStr
        if len(numStr) == 11 and numStr[0] == '1':
            self.number = numStr[1:]

    def area_code(self):
        return self.number[:3]

    def pretty(self):
        return '(%s) %s-%s' % (self.number[:3], self.number[3:6], self.number[6:])
