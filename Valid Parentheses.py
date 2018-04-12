class Solution(object):
    def isValid(self, s):
        stk = []
        for item in s:
            if item == '(' or item == '[' or item == '{':
                stk.append(item)
            if not stk:
                return False
            else:
                if item == ')':
                    if stk.pop() != '(':
                        return False
                if item == ']':
                    if stk.pop() != '[':
                        return False
                if item == '}':
                    if stk.pop() != '{':
                        return False
        if stk:
            return False
        else:
            return True

def stringToString(input):
    return input[1:-1].decode('string_escape')

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            s = stringToString(line)
            
            ret = Solution().isValid(s)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
