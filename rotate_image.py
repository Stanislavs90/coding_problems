from typing import List

matrix = [[1,2,3],[4,5,6],[7,8,9]]
"""


[
[1,2,3]
[4,5,6]
[7,8,9]
]

[1,2,3],[4,5,6],[7,8,9]
[7,2,3],[8,5,6],[9,4,1]


Output: [[7,4,1],[8,5,2],[9,6,3]]

find length of array
find lenght of subarray

go last array
    go first element in last array

    sawp with first elemenet in first array

    go second element in last array

    swap with second array first element

"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left = 0
        right = len(matrix) - 1

        while left < right:
            # skip the last element in the array
            for i in range(right - left):
                # are the same as left and right
                top = left
                bottom = right

                # save the topleft
                topLeft = matrix[top][left + i]

                # move bottom left into top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # move bottom right into bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # move top right into bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # move top left into top right
                matrix[top + i][right] = topLeft

            right -= 1
            left += 1



answer = Solution()

answer.rotate(matrix)
print(matrix)