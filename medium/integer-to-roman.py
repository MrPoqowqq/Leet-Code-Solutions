# Slowest - 3ms
class Solution1:
    def intToRoman(self, num: int) -> str:
        answer = ""
        dict_index = 0
        roman = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        while num:
            current_dust = roman[dict_index][0]
            current_letter = roman[dict_index][1]
            if num >= current_dust:
                num = num - current_dust
                answer = answer + current_letter
            else:
                dict_index += 1

        return answer


# Faster - <3ms
class Solution2:
    def intToRoman(self, num: int) -> str:
        answer = []
        roman_dict = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        for val, roman in roman_dict:
            quant = num // val
            answer.append(roman * quant)
            num = num % val

        return "".join(answer)


# Fastest - 0ms
class Solution3:
    def intToRoman(self, num: int) -> str:
        answer = []
        answer_append = answer.append
        roman_dict = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        for val, roman in roman_dict:
            if num == 0:
                break
            quant = num // val

            if quant:
                answer_append(roman * quant)
                num %= val

        return "".join(answer)
