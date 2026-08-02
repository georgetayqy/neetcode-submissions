import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        results = []

        # consider self as well
        self.followers[userId].add(userId)

        for follower in self.followers[userId]:
            tweet_from_follower = self.tweets[follower]
            num_tweets = len(tweet_from_follower)

            if num_tweets > 0:
                time, tweetId = tweet_from_follower[-1]
                heap.append((-time, tweetId, follower, num_tweets - 2))

        heapq.heapify(heap)

        while heap and len(results) < 10:
            time, tweetId, followerId, index = heapq.heappop(heap)
            results.append(tweetId)

            if index >= 0:
                new_time, new_tweetId = self.tweets[followerId][index]
                heapq.heappush(heap, (-new_time, new_tweetId, followerId, index - 1))
            
        return results

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
