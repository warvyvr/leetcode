class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
      if (root == None):
          return True
      candidateList = []
      candidateList.append(root.left)
      candidateList.append(root.right)
      while (len(candidateList) > 0):
        left = candidateList.pop(0)
        right = candidateList.pop(0)
        if (left == None and right == None):
          continue
        elif ((left != None and right != None) and (left.val == right.val)):
          candidateList.append(left.left)
          candidateList.append(right.right)
          candidateList.append(left.right)
          candidateList.append(right.left)
        else:
          return False

      return True