class Solution:
    
    bow = {
        0: 'Zero',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen',
        20: 'Twenty',
        30: 'Thirty',
        40: 'Forty',
        50: 'Fifty',
        60: 'Sixty',
        70: 'Seventy',
        80: 'Eighty',
        90: 'Ninety',
        100: 'Hundred',
        1000: 'Thousand',
        1000000: 'Million',
        1000000000: 'Billion',
    }
    
    def numberToWords(self, num: int) -> str:
        
        n_str = [int(x) for x in str(num)][::-1]
        
        jump = 3
        
        i = 0
        
        c_group = 1
        
        n_name = ''
        while i < len(n_str):
            # Get next 3 numbers
            sub = n_str[i:i+jump]
            
            # Build an aux string
            aux_name = ''
            # For numbers of the form abc where a > 1
            if len(sub) == 3 and sub[2] > 0:
                aux_name += "{} {} ".format(Solution.bow[sub[2]], Solution.bow[100])
                
            # For numbers of the form *bc
            if len(sub) >= 2:
                # If bc in [01 ... 09] -> only guess c
                if sub[1] == 0 and sub[0] > 0:
                    aux_name += "{} ".format(Solution.bow[sub[0]])
                
                # If bc in [10 ... 19] -> Guess bc
                if sub[1] == 1:
                    aux_name += "{} ".format(Solution.bow[sub[1]*10 + sub[0]])
                    
                # If bc in [20 ... 99]
                if sub[1] >= 2:
                    # Guess b*10 first
                    aux_name += "{} ".format(Solution.bow[sub[1]*10])
                    # If c in [1 ... 9] -> Guess c
                    if sub[0] > 0:
                        aux_name += "{} ".format(Solution.bow[sub[0]])

            # For numbers of the form c -> Guess the digit alone
            if len(sub) == 1:
                aux_name += "{} ".format(Solution.bow[sub[0]])
            
            # If we are currently in the thousands, and we received something that wasn't sub=000
            # -> Append the current significance (thousands, million, billion)
            if c_group > 100 and len(aux_name) > 0:
                aux_name += "{} ".format(Solution.bow[c_group])

            # Append the result to the final name
            n_name = aux_name + n_name
            # Always jump at the end and go to the next group (thousands, millio, billion)
            c_group *= 1000
            i += jump

        # Strip the string and return
        return n_name.strip()