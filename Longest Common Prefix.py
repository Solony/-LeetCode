class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        else:
            strs.sort()
            tmp_st = strs[0]
            tmp_st_2 = strs[len(strs) - 1]
            ll = []
            for i in range(0, len(tmp_st)):
                if tmp_st[i] != tmp_st_2[i]:
                    break
                else:
                    ll.append(tmp_st[i])
            return ''.join(ll)

def stringToStringArray(input):
    return json.loads(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            strs = stringToStringArray(line)
            
            ret = Solution().longestCommonPrefix(strs)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
