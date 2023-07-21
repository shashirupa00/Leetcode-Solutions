class Solution:
    def nextClosestTime(self, time: str) -> str:

        hour, minute = time.split(":")

        arr = sorted(set(hour+minute))

        possible_values = [i+j for i in arr for j in arr]
        
        cur = possible_values.index(minute)
        if cur+1 < len(possible_values) and int(possible_values[cur+1]) < 60:
            return hour + ':' + possible_values[cur+1]
        
        cur = possible_values.index(hour)
        if cur+1 < len(possible_values) and int(possible_values[cur+1]) < 24:
            return possible_values[cur+1] + ':' + possible_values[0]
        
        return possible_values[0] + ':' + possible_values[0]