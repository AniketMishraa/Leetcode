#Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        ls,ls1 = [], []
        
        if x >= -2**31 and x <= 2**31-1:
            x = str(x)
            for i in x:
                ls.append(i)
            for i in ls:
                ls1.append(i)

            print(ls)
            if(ls[0] == '-'):
                ls.pop(0)
            print(ls1)
            a = "".join(ls[::-1])
            print(a)

            if ls1[0] == '-':
                b = int(a)
                
                if(b >= -2**31 and b <= 2**31-1):
                    return b - b - b
                else:
                    return 0
            
            else:
                if(int(a) >= -2**31 and int(a) <= 2**31-1):
                    return int(a)
                else: 
                    return 0
        else:
            return 0