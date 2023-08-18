#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) ==1: 
            return False
        sum = [0,0,0]
        dict_val = {"(" : 1 , ")" : -1, "{" : 1 , "}" : -1, "[" : 1 , "]" : -1}
        dict_bracket = {"(" : ")", ")" : "(", "{" : "}", "}" : "{", "[" : "]", "]" : "[",}
        dict = {}
        pos = 0
        valid = True
        for i in s:
            if dict.get(i) != None:
                if dict_val.get(i) == -1:
                    if dict.get(i) == 0:
                        if sum[1] == 0 and sum[2] == 0: 
                            sum[dict.get(i) ] +=dict_val.get(i)
                            if sum[dict.get(i) ] == 0:
                                sum.pop(dict.get(i))
                                sum.append(0)
                                pos -=1
                                dict.pop(i)
                                dict.pop(dict_bracket.get(i))
                        else:
                            valid = False
                            break
                    elif dict.get(i) == 1:
                        if sum[2] == 0: 
                            sum[dict.get(i) ] +=dict_val.get(i)
                            if sum[dict.get(i) ] == 0:
                                sum.pop(dict.get(i))
                                sum.append(0)
                                pos -=1
                                dict.pop(i)
                        else:
                            valid = False
                            break
                    else:
                        sum[dict.get(i) ] +=dict_val.get(i)
                        if sum[dict.get(i) ] == 0:
                            sum.pop(dict.get(i))
                            sum.append(0)
                            pos -=1
                            dict.pop(i)
                        
                else:
                    sum[dict.get(i) ] +=dict_val.get(i)
                    

                
            else:
                dict[i] = pos
                dict[dict_bracket.get(i)] = pos
                sum[pos] += dict_val.get(i)
                if sum[pos]<0 :
                    valid = False
                    break
                pos +=1
              
        #print(sum)
        if sum[0] + sum[1] + sum[2] !=0:
            return False
        else:
            return valid 
    
parenth = Solution()
s = "{}[({})]"
s = "((()))()()()"
s = "[({(())}[()])]"
print(parenth.isValid(s))