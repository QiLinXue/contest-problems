greatestSize = 0
def recursiveCalculate(string,index=0,size=2):
  global greatestSize
  cutString = string.lower()[index:index+size]

  if len(string) == 1:
    return 1 # If string is only one character
  if size > len(string):
    return 0 # Base Case
  if index+size > len(string):
    return recursiveCalculate(string,0,size+1) # Reloop with greater substring size
  if cutString == cutString[::-1]:
    if len(cutString) > greatestSize:
      greatestSize = len(cutString)
    return recursiveCalculate(string,index+1,size) + 1 # Next substring if palindrome
  else:
    return recursiveCalculate(string,index+1,size) # Next substring if no palindrome

recursiveCalculate(input())
print(greatestSize)