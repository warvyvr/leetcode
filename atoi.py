class Solution:
    # @return an integer
    def atoi(self, str):
        if (str == None):
            return 0
            
        str=str.strip()
        if (len(str) == 0):
            return 0
        value = 0
        negative = False
        if (str[0] == "-"):
            negative = True
            str = str[1:]
        elif (str[0] == "+"):
            str = str[1:]

        for i,char in enumerate(str):
            if (ord(char) > ord('9') or ord(char) < ord('0')):
                break
            number = ord(char) - ord('0')
            value = value*10 + number
            
        if (negative == True):
            value -= 2*value
            
        if (value > (2**(32-1)-1)):
            return 2**(32-1)-1
        elif (value < (-(2**(32-1)))):
            return -(2**(32-1))
        
        return value