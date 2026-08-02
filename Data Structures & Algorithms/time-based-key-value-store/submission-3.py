from collections import defaultdict

class TimeMap:

    def __init__(self):
        # each tmap entry stores ([value, timestamp])
        # timestamp is sorted as strictly increasing order
        self.tmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tmap:
            return ""
        
        requested = self.tmap[key]

        # do a binary search to find the timestamp
        left, right = 0, len(requested) - 1
        results = ""

        # we need to do this left <= right as we need to check
        # the final middle value at the end of the binary search as well
        while left <= right:
            mid = left + (right - left) // 2
            value, entry_timestamp = requested[mid]

            if entry_timestamp <= timestamp:
                # middle is greater than the target, search left
                results = value
                left = mid + 1
            else:
                right = mid - 1

        return results
