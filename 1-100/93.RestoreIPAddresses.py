class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def works (s):
            return s == str(int(s)) and int(s) <= 255

        n = len(s)
        ans = []
        for i in range(1, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a, b, c, d = s[:i], s[i:j], s[j:k], s[k:]
                    if works(a) and works(b) and works(c) and works(d):
                        ans.append(f'{a}.{b}.{c}.{d}')
        return ans