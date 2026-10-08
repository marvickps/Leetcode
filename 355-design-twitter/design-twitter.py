class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list) # [[2,33],[2,44]]
        self.follows = defaultdict(set) #{2:(1,3,2,4) }

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        users = self.follows[userId] | {userId}
 
        candidates = []
        for u in users:
            candidates.extend(self.tweets[u][-10:])
 
        candidates.sort(reverse=True)
        feed = []
        for count, tweetId in candidates[:10]:
            feed.append(tweetId)
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)