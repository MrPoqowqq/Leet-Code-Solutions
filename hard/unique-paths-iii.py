from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start_r = 0
        start_c = 0
        count_0 = 0
        count_visited = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                count_visited += 1
                if val == 1:
                    start_r = r
                    start_c = c
                    count_0 += 1
                elif val == 0 or val == 2:
                    count_0 += 1

        def engine(r, c, visited_count):
            if r < 0 or r >= len(grid):
                return 0
            elif c < 0 or c >= len(grid[0]):
                return 0
            visited_val = grid[r][c]
            if visited_val == -1:
                return 0

            if visited_val == 2:
                if count_0 == visited_count:
                    return 1
                else:
                    return 0
            else:
                grid[r][c] = -1
                pathup = engine(r - 1, c, visited_count + 1)
                pathdown = engine(r + 1, c, visited_count + 1)
                pathleft = engine(r, c - 1, visited_count + 1)
                pathright = engine(r, c + 1, visited_count + 1)

                paths = pathup + pathdown + pathleft + pathright

                grid[r][c] = 0
                return paths

        return engine(start_r, start_c, 1)


if __name__ == "__main__":
    sol = Solution()

    test_grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]

    result = sol.uniquePathsIII(test_grid)
    print(f"Result: {result}")
