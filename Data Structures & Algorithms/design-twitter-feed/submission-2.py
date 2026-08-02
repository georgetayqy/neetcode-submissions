import heapq
from collections import deque

class Twitter:
    def __init__(self):
        self.followers = {}
        self.tweets = []
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets, ((-self.time, -tweetId), userId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        results = deque()

        def traverse(heap):
            if not heap:
                return

            times, postUser = heapq.heappop(heap)
            time, tweetId = -times[0], -times[1]

            if postUser in self.followers.get(userId, set()) or postUser == userId:
                results.appendleft(tweetId)

                if len(results) > 10:
                    results.pop()

            traverse(heap)
            heapq.heappush(heap, ((-time, -tweetId), postUser))
    
        traverse(self.tweets)
        return list(results)

    def follow(self, followerId: int, followeeId: int) -> None:
        followers = self.followers.get(followerId, set())
        followers.add(followeeId)
        self.followers[followerId] = followers

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers or followeeId not in self.followers[followerId]:
            return

        self.followers[followerId].remove(followeeId) 
