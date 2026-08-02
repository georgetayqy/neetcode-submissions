from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        all_values = self.map[key]

        if len(all_values) == 0:
            return ""

        # binary search to find timestamp or return the latest timestamp
        left, right = 0, len(all_values) - 1

        while left < right:
            mid = left + (right - left) // 2

            if all_values[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid

        if all_values[left][0] <= timestamp:
            return all_values[left][1]
        elif left - 1 >= 0 and all_values[left - 1][0] <= timestamp:
            return all_values[left - 1][1]
        else:
            return ""

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)