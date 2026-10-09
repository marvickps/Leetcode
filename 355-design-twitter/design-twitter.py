class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list) #{1: [[0, 5], [4, 9]], 2: [[1, 6]]}
        self.follows = defaultdict(set) #{2:(1,3,2,4) }

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        users = []
        users.append(userId)
        for followeeId in self.follows[userId]:
            if followeeId != userId:
                users.append(followeeId)
        
        heap = []
        for u in users:
            user_tweets = self.tweets[u]
        
            if len(user_tweets)>0:
                newest_index = len(user_tweets)-1
                newest_tweet = user_tweets[newest_index]

                tweet_time = newest_tweet[0]
                tweet_id = newest_tweet[1]

                heapq.heappush_max(heap, [tweet_time,tweet_id,u,newest_index])
            
        feed = []
        while len(heap)>0 and len(feed) < 10:
            top = heapq.heappop_max(heap)
            tweet_id = top[1]
            user = top[2]
            index = top[3]

            feed.append(tweet_id)

            if index>0:
                older_index = index-1
                older_tweet = self.tweets[user][older_index]

                older_time = older_tweet[0]
                older_id = older_tweet[1]

                heapq.heappush_max(heap,[older_time,older_id,user,older_index])
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