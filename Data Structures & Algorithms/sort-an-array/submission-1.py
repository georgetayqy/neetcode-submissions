class Solution:
    def bubble_sort(self, small_list):
        list_length = len(small_list)

        for i in range(list_length):
            for j in range(i, list_length):
                if small_list[i] > small_list[j]:
                    small_list[i], small_list[j] = small_list[j], small_list[i]

        return small_list

    def partition(self, array, pivot) -> List[List[int]]:
        less, equal, more = [], [], []
        for num in array:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                more.append(num)

        return less, equal, more

    def sortArray(self, nums: List[int]) -> List[int]:
        import random

        def inner_helper(array):
            if len(array) <= 5:
                return self.bubble_sort(array)
            
            results = []
            random_pivot = random.randint(0, len(array) - 1)
            less, equal, more = self.partition(array, array[random_pivot])

            results.extend(inner_helper(less))
            results.extend(inner_helper(equal))
            results.extend(inner_helper(more))

            return results
        
        return inner_helper(nums)