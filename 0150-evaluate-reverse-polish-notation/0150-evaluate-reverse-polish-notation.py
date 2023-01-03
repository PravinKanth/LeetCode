class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op=["+","-","*","/"]
        st=[]
        for i in tokens:
            if i in op:
                a=int(st.pop())
                b=int(st.pop())
                if i=="+":
                    st.append(a+b)
                if i=="-":
                    st.append(b-a)
                if i=="*":
                    st.append(a*b)
                if i=="/":
                    st.append(b/a)    
            else:
                st.append(i)         
        return int(st[0])               
