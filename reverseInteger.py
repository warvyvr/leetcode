class Solution:
    # @return an integer
    def reverse(self, x):
      value = str(x)
      reverseValue = ""
      if (value[0] == "-"):
        reverseValue += "-"
        value = value.replace("-","")
      reverseValue += value[::-1]
      #print "reverseValue"
      return int(reverseValue)


print "100-->", Solution().reverse(100)
print "-100-->", Solution().reverse(-100)

print "--1000000000000-->", Solution().reverse(-1000000000000)
print "--10000000000003-->", Solution().reverse(-10000000000003)