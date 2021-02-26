class Solution:
    def numberToWords(self, num: int) -> str:
        num = str(num)
        if num=='0':
            return "Zero"
        def get_sub(s):
            result = []
            keys_1 = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven',
                     '8': 'Eight', '9': 'Nine', '0': None}
            keys_2 = {'10': 'Ten', '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', '14': 'Fourteen', 
                      '15': 'Fifteen', '16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen', '19': 'Nineteen',
                     '2': 'Twenty', '3': 'Thirty', '4': 'Forty', '5': 'Fifty', '6': 'Sixty', '7': 'Seventy', 
                     '8': 'Eighty', '9': 'Ninety', '0': None}
            if len(s)==1:
                result += [keys_1[s]]
            elif len(s)==2:
                if s in keys_2:
                    result+=[keys_2[s]]
                else:
                    result += [keys_2[s[0]],keys_1[s[1]]]
            else:
                result += [keys_1[s[0]]]
                if s[0]!='0':
                    result+=['Hundred']
                result += get_sub(s[1:])
            return result
        
        subs = [None, 'Thousand', 'Million', 'Billion']
        answer_builder = []
        if not len(num)%3==0:
            answer_builder += [num[:len(num)%3]]
            num = num[len(num)%3:]
        while num!="":
            answer_builder += [num[:3]]
            num = num[3:]
        
        x = 0
        answer = []
        while x<len(answer_builder):
            answer += get_sub(answer_builder[x]) 
            if answer_builder[x]!='000':
                answer += [subs[len(answer_builder)-x-1]]
            x+=1
        string_result = ""
        for i in range(len(answer)-1):
            if answer[i]:
                string_result += answer[i] + " "
        return string_result[:-1]
        
