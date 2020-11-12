class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        answer = []
        while len(words)>0:
            tm = ""
            i = 0
            while i<len(words):
                if i==0:
                    tm+=words[i]
                    i+=1
                elif len(words[i])+1 <= maxWidth - len(tm):
                    tm+=" "
                    tm+=words[i]    
                    i+=1
                else:
                    break
            words = words[i:]
            answer.append(tm)
        
        for i in range(len(answer)):
            todo = maxWidth - len(answer[i])
            words = answer[i].split(" ")
            x = 0
            y = 0
            print(todo)
            if not i==len(answer)-1:
                while x<=todo+len(words)-2:
                    words[y]+=" "
                    if y<len(words)-2:
                        y+=1
                    else:
                        y=0
                    x+=1
            else:
                while x<=todo+len(words)-2:
                    if x<len(words):
                        words[x]+=" "
                    else:
                        words[-1]+=" "
                    x+=1
            tm = ""
            for x in words:
                tm+=x
            answer[i] = tm
        
        print(answer)
        return answer
        
