class Solution:
    def intToRoman(self, num: int) -> str:
        sym = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        result = ""

        for i in range(13):
            if num == 0:
                break
            
            times = num // val[i]
            while times > 0:
                result += sym[i]
                times -= 1

            num = num % val[i]

        return result
