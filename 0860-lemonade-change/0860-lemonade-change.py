class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        fiveBills, tenBills = 0, 0

        for i, bill in enumerate(bills):
            
            if bill == 5:
                fiveBills += 1
            
            else:

                if not fiveBills:
                    return False

                if bill == 10:
                    tenBills += 1
                    fiveBills -= 1
                
                if bill == 20:
                    if tenBills:
                        tenBills -= 1
                        fiveBills -= 1
                    elif fiveBills >= 3:
                        fiveBills -= 3
                    else:
                        return False
        
        return True