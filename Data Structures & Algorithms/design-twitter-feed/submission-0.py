class Twitter:

    def __init__(self):
        self.time=0
        self.follower=defaultdict(set)
        self.feeds=defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feeds[userId].append((self.time,tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweetfeed=self.feeds[userId][:]
        for followId in self.follower[userId]:
            tweetfeed.extend(self.feeds[followId])
        tweetfeed.sort(key=lambda x:-x[0])
        return [tweetid for _,tweetid in tweetfeed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.follower[followerId].discard(followeeId)
        
