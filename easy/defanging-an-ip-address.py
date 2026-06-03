from unittest import result


class Solution:
    def defangIPaddr(self, address: str) -> str:
        a = ""
        for i in address:
            if i == ".":
                a = a + "[.]"
            else:
                a = a + i

        return a


if __name__ == "__main__":
    add = "1.1.1.1"

    sol = Solution()
    result = sol.defangIPaddr(add)

    print(result)
