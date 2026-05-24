class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        s = "L" + dominoes + "R"
        arr = list(s)

        i = 0

        for j in range(1, len(arr)):
            if arr[j] == '.':
                continue

            middle = j - i - 1

            # Case 1: same direction
            if arr[i] == arr[j]:
                for k in range(i + 1, j):
                    arr[k] = arr[i]

            # Case 2: R ... L
            elif arr[i] == 'R' and arr[j] == 'L':
                left = i + 1
                right = j - 1

                while left < right:
                    arr[left] = 'R'
                    arr[right] = 'L'
                    left += 1
                    right -= 1

            # Case 3: L ... R -> do nothing

            i = j

        return "".join(arr[1:-1])