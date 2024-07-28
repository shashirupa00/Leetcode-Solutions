class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        
        debts = defaultdict(int)

        for src, dst, amt in transactions:
            debts[src] -= amt
            debts[dst] += amt
        
        debtList = [debts[key] for key in debts if debts[key]]
        n = len(debtList)

        def backTrack(idx):

            while idx < n and debtList[idx] == 0:
                idx += 1
            
            if idx == n:
                return 0

            res = float("inf")

            for i in range(idx + 1, n):
                if debtList[idx] * debtList[i] < 0:
                    debtList[i] += debtList[idx]
                    res = min(res, backTrack(idx + 1) + 1)
                    debtList[i] -= debtList[idx]
            
            return res
        
        return backTrack(0)