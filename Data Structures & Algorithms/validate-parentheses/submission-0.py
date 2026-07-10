class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {'}' : '{' ,']' : '[' , ')':'('}


        st = []

        for a in s:
            if a in hashMap:
                if st and st[-1] == hashMap[a]:
                    st.pop()
                else:
                    return False
            else:
                st.append(a)
        return True if not st else False