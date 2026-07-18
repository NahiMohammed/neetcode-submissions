from collections import defaultdict
from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)      # user -> [(time, tweetId)]
        self.following = defaultdict(set)    # user -> {followees}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.following[userId].add(userId)
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.following[userId].add(userId)

        heap = []

        # Ajouter le dernier tweet de chaque utilisateur suivi
        for followee in self.following[userId]:
            if self.tweets[followee]:
                idx = len(self.tweets[followee]) - 1
                time, tweetId = self.tweets[followee][idx]
                heapq.heappush(heap, (-time, tweetId, followee, idx))

        res = []

        while heap and len(res) < 10:
            negTime, tweetId, followee, idx = heapq.heappop(heap)
            res.append(tweetId)

            # Ajouter le tweet précédent du même utilisateur
            if idx > 0:
                idx -= 1
                time, tweetId = self.tweets[followee][idx]
                heapq.heappush(heap, (-time, tweetId, followee, idx))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followerId)
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].discard(followeeId)