class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search for the row to find

        left, right = 0, len(matrix) - 1

        while left <= right:
            mid = left + (right - left) // 2
            middle_row = matrix[mid]
            print(middle_row)

            if middle_row[0] <= target <= middle_row[-1]:
                print("huh")
                # do another binsearch here to find it

                inner_left, inner_right = 0, len(middle_row) - 1

                while inner_left <= inner_right:
                    inner_mid = inner_left + (inner_right - inner_left) // 2
                    middle_element = middle_row[inner_mid]
                    
                    if target == middle_element:
                        return True
                    elif target > middle_element:
                        inner_left = inner_mid + 1
                    else:
                        inner_right = inner_mid - 1
                
                return False
            elif target < middle_row[0]:
                # search on higher rows
                right = mid - 1
            elif target > middle_row[-1]:
                # search on the lower rows
                left = mid + 1

        return False