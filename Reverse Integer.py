class Solution:
   def reverse(self, x):
       """
       :type x: int
       :rtype: int
       """
       r = 0
       if x < 0:
           flag = True
           a = -x
           if x < -2147483648:
               return 0
       else:
           flag = False
           a = x
           if x > 2147483648:
               return 0
       while 1:
           r += a % 10
           #r = r*10
           a = a//10
           if not a:
               break
           r = r*10
           
       ret = r*-1 if flag else r
       return ret if r<2147483648 else 0

def stringToInt(input):
    return int(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            x = stringToInt(line)
            
            ret = Solution().reverse(x)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
