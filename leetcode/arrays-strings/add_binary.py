class Solution:
    
    def binarySumHelper(self, cx, cy):
        if cx == "0" and cy == "0":
            return "0", "0"
        if cx == "0" and cy == "1":
            return "1", "0"
        if cx == "1" and cy == "0":
            return "1", "0"
        if cx == "1" and cy == "1":
            return "0", "1"
    
    def binarySum(self, x, y):
        diff = len(x) - len(y)
        y = '0'*diff + y  # Make them the same lenght
        
        res = ""
        car = "0"
        for cx, cy in zip(x[::-1], y[::-1]):  # Iterating in reverse order
            # 1. Add carriage
            sumres, car = self.binarySumHelper(cx, car)
            
            # Second step
            sumres, car2 = self.binarySumHelper(sumres, cy)
            
            if car2 == "1":
                car = car2

            res = sumres + res
                 
        if car == "0":
            return res
        
        return car + res
    
    def addBinary(self, a: str, b: str) -> str:
        if len(a) >= len(b):
            return self.binarySum(a, b)

        return self.binarySum(b, a)


# TODO: improve to use less memory