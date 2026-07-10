class Solution:
    def isValid(self, s: str) -> bool:
        b = {"}":"{","]":"[",")":"("}
        st = []

        for a in s:
            if a in b:
                if st and st[-1] == b[a]:
                    st.pop()
                else:
                    return False
            else:
                st.append(a)

        return True if not st else False