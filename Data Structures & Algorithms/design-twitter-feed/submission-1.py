from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.time = 0
        self.data = defaultdict(list)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.data[userId].append([tweetId, self.time])
        self.followers[userId].add(userId)   # le user se suit lui-même
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followers[userId].add(userId)   # au cas où il n'a jamais posté

        tweets = []
        for follower in self.followers[userId]:
            tweets.extend(self.data[follower])

        tweets.sort(key=lambda x: x[1], reverse=True)

        return [tweetId for tweetId, _ in tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followerId)   # il se suit toujours
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followers[followerId].discard(followeeId)