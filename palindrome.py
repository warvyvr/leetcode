class Solution:
  def isPalindrome(self,x):
    l = list(str(x))
    if (len(l) <= 1):
        return True
        
    while(len(l)):
      head = l.pop(0)
      tail = l.pop(-1)
      if (head != tail):
        return False
      if (len(l) == 1):
        return True
    return True