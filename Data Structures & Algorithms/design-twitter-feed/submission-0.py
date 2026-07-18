class Twitter:

    def __init__(self):
        self.time=0
        self.data=defaultdict(list)
        self.followers=defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        self.data[userId].append([tweetId,self.time])
        self.followers[userId].append(userId)
        self.time+=1

        

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets=[]
        for follower in self.followers[userId]:
            tweets.extend(self.data[follower])

        tweets.sort(key=lambda x: x[1], reverse=True)

        return [tweetId for tweetId, _ in tweets[:10]]
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].remove(followeeId)
        
