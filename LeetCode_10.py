# 10. Regular Expression Matching
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == p:
            return True
        # if p[1] not equal to '*', just need to check if s[0] == p[0]
        # if p[1] is '*' and s[0] matches p[0], 2 choices, * in p matches 0 times, or multiple times.
        # if p[1] is '*' and s[0] doesn't match p[0], * in p matches 0 times
        if len(p) > 1 and p[1] == '*':
            if s and p and (s[0] == p[0] or p[0] == '.'):
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
            else:
                return self.isMatch(s, p[2:])
        elif s and p and (s[0] == p[0] or p[0] == '.'):
            return self.isMatch(s[1:], p[1:])
        return False