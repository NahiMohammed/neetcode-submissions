class Twitter:

    def __init__(self):
        self.followers=defaultdict(set)
        self.time=0
        self.posts=defaultdict(list)


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.followers[userId]:
            self.followers[userId].add(userId)
        self.time+=1
        self.posts[userId].append([tweetId,self.time])
        

            

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        res=[]

        for f in self.followers[userId] :
            post=self.posts[f]
            for i in range(len(post)): 
                heapq.heappush(heap,(-post[i][1],post[i][0]))
        for _ in range(min(10,len(heap))) : 
            _ , id = heapq.heappop(heap)
            res.append(id)
        return res

        

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers[followerId]:
            self.followers[followerId].add(followerId)


        self.followers[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)

