# Time: O(n)
# Space: O(n)


class Solution:
    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""

        seperator = list()
        returnstring = ""

        returnstring = strs[0]
        currentlength = len(strs[0]) - 1
        seperator.append(currentlength)

        for i in range(1, len(strs), 1):
            returnstring += strs[i]
            currentlength += len(strs[i])
            seperator.append(currentlength)

        start = ""
        for i in range(len(seperator)):
            start += str(seperator[i]) + "$"

        start = str(len(seperator)) + "!" + start
        return start + returnstring

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        numsep = ""
        pos = 0
        for i in range(len(s)):
            if s[i] == "!":
                numsep = int(s[0:i])
                pos = i + 1
                break

        seperator = list()
        while len(seperator) < numsep:
            for i in range(pos, len(s)):
                if s[i] == "$":
                    seperator.append(int(s[pos:i]))
                    pos = i + 1
                    break

        returnlist = list()
        returnlist.append(s[pos : pos + seperator[0] + 1])
        for i in range(1, len(seperator), 1):
            returnlist.append(s[pos + seperator[i - 1] + 1 : pos + seperator[i] + 1])

        return returnlist
