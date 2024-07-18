#https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = 0
        for customer in accounts:
            wealth = 0
            for bank in customer:
                wealth += bank
            result = max(result, wealth)

        return result
    
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(customer) for customer in accounts])