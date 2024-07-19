#https://leetcode.com/problems/letter-combinations-of-a-phone-number/

mapping={
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

def backTrack(index, digits, _str, result)->None:
    if index == len(digits):
        result.append(_str)
        return
    for i in mapping[digits[index]]:
        backTrack(index+1, digits, _str+i, result)
    return result
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if len(digits) == 0:
            return result
        backTrack(0, digits, "", result)
        return result
        