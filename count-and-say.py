class Solution:
    # @return a string
    def countAndSay(self, n):
      seq = []
      seq.append(1)
      result = []
      pre_number = -1
      counting = 0
      if (n == 1):
        result = ""
        return result.join(str(x) for x in seq)

      n -= 1
      while(n > 0):
        pre_number = -1
        countAndSay = 0
        while(len(seq)):
          number = seq.pop(0)
          if(pre_number == -1):
            pre_number = number
            counting = 1
          elif (pre_number ==  number):
            counting += 1
          else:
            result.append(counting)
            result.append(pre_number)
            pre_number = number
            counting = 1

        if (pre_number != -1):
          result.append(counting)
          result.append(pre_number)
          pre_number = number
          counting = 1

        if (result == [2,1]):
          y= 100
        n -= 1
        seq = result
        result = []

      result = ""
      return result.join(str(x) for x in seq)
