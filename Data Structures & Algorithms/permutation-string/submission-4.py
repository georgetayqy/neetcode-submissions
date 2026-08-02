class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = self.get_counter(s1)
        
        # start is the starting index to begin the sliding window search
        start = 0
        while start < len(s2):
            starting_char = s2[start]
            print(f"STARTING: POSITION {start} @ {starting_char}")
            
            # if it is not even in s1, then don't bother searching
            if starting_char not in counter:
                start += 1
                continue
            
            for end in range(start, len(s2)):
                iterating_character = s2[end]
                print(f"\tITERATING: POSITION {end} @ {iterating_character}")
                if iterating_character in counter and counter[iterating_character] > 0:
                    counter[iterating_character] -= 1
                else:
                    print(f"\t\tBROKE")
                    break
            
            if self.is_counter_fulfilled(counter):
                return True
            
            for iterator in range(start, end):
                reversing_character = s2[iterator]
                counter[reversing_character] += 1
            
            start = start + 1

        return self.is_counter_fulfilled(counter)

    def is_counter_fulfilled(self, counter: dict) -> bool:
        for char in counter:
            if counter[char] != 0:
                return False
        
        return True
    
    def get_counter(self, s1: str) -> dict:
        d = {}

        for char in s1:
            d[char] = d.get(char, 0) + 1
        
        return d
