class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # catch all to return quickly if not equal length
        if (len(s) != len(t)):
            return False
        
        # create hashmap of char in s to char in t
        # if this mapping ever needs to change
        # then must not be iso
        m = {}
        for i in range(0, len(s)):
            # check if s[i] char in the map already
            if s[i] in m:
                # now check if t[i] is equal to previously mapped s[i] char
                if t[i] != m[s[i]]:
                    # if not then we have a problem as we have mapped s[i] to something else
                    return False
            elif t[i] in m.values():
                # else if t[i] is in the values of the map for another char in s[i]
                # then we also have a problem
                # as it should only be mapped as a value to s[i]
                return False
            else:
                # else let's add the mapping for future checking
                m[s[i]] = t[i]
        # if we made it through then must be iso
        return True
if __name__ == "__main__":
    s = Solution()
    print(s.isIsomorphic("egg","add"))