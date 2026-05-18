class Solution:
    def romanToInt(self, s: str) -> int:
        z = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        output = 0
        for i in range(len(s)):
            current = z[s[i]]
            if i + 1 < len(s) and current < z[s[i + 1]]:
                output = output - current
            else:
                output = output + current
        return output


def main():
    converter = Solution()
    print("=====CONVERTER=========")

    while True:
        user_input = input("\n Enter roman number or exit to leave: ").upper()

        if user_input == "EXIT":
            print("Bye Bye! ")
            break
        if user_input == "":
            print("Input is empty.")

        try:
            result = converter.romanToInt(user_input)
            print(f"Result: {result}")
        except KeyError:
            print("You have to use roman numbers: I, V, X, L, C, D, M.")


if __name__ == "__main__":
    main()
