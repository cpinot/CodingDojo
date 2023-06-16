class   MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, *num):
        for i in num:
            self.result += i
        print(self.result)
        return self    
    
    def subtract(self, *num):
        for i in num:
            self.result -= i
        print(self.result)
        return self

suma = MathDojo().add(2,2).add(2,5,1).add(3,2,1,1)
resta = MathDojo().subtract(2,2).subtract(2,5,1).subtract(3,2,1,1)


