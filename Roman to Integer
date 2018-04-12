class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        sum = 0
        for i in range(0, len(s) - 1):
            if d[s[i]] < d[s[i+1]]:
                sum -= d[s[i]]
            else:
                sum += d[s[i]]
        return sum + d[s[-1]]

def stringToString(input):
    return input[1:-1].decode('string_escape')

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
            s = stringToString(line)
            
            ret = Solution().romanToInt(s)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
