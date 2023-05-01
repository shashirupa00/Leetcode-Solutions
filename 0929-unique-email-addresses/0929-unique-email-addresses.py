class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        def filterLocal(local):

            finalLocal = ""
            for char in local:
                if char == "+":
                    break
                elif char.isalpha():
                    finalLocal += char
            
            return finalLocal

        
        uniqEmails = set()

        for email in emails:
            local, domain = email.split("@")
            local = filterLocal(local)
            uniqEmails.add(local+"@"+domain)
            
        return len(uniqEmails)
            



        
                
                
            
            
            
        
        
            
            
        
        
        