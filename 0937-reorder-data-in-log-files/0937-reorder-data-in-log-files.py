class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letterLogs = []
        digitLogs = []

        def checkLog(log):
            
            if log[-1].isalpha():
                return 'letter'
            
            return 'digit'
        
        for log in logs:
            
            logType = checkLog(log)
            
            if logType == 'letter':
                letterLogs.append(log)
            else:
                digitLogs.append(log)

        def sortKeys(log):
            identifier, content = log.split(maxsplit=1)
            return (0, content, identifier) if content[0].isalpha() else (1,)
        
        letterLogs = sorted(letterLogs, key=sortKeys)

        return letterLogs + digitLogs