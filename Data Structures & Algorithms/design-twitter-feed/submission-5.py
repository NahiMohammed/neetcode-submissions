class Twitter:

    def __init__(self):
        self.followers=defaultdict(set)
        self.time=0
        self.posts=defaultdict(list)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.posts[userId].append([tweetId,self.time])
        

            

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        post=self.posts[userId]
        res=[]
        for i in range(min(10,len(post))): 
            heapq.heappush(heap,(-post[i][1],post[i][0]))
        for f in self.followers :
            post=self.posts[f]
            for i in range(min(10,len(post))): 
                heapq.heappush(heap,(-post[i][1],post[i][0]))
        for _ in range(10) : 
            _ , id = heapq.heappop(heap)
            res.append(id)
            return res

        

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)

