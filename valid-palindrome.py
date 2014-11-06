class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
      l = list(s)
      if (len(l)<=1):
        return true
      head = 0
      tail = len(l)-1
      while (head <= tail):
        while(l[head].isalpha() == False and l[head].isdigit() == False):
          head += 1
          if (head >= tail):
            return True


        while(l[tail].isalpha() == False and l[tail].isdigit() == False):
          tail -= 1
          if (head >= tail):
            return True

        hc = l[head].lower()
        tc = l[tail].lower()

        if (hc != tc):
          return False

        head += 1
        tail -= 1

      return True
