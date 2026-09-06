class Twitter:

    def __init__(self):
        self.users = {}

    # user_schema = {
    #     'follows': set()
    #     'tweets':[(tweetId, timestamp)]
    # }

        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1

        if(userId not in self.users.keys()):
            self.users[userId] = {
                'follows': set(),
                'tweets': []
            }

        user = self.users[userId]
        user['tweets'].append((tweetId, self.timestamp))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        if(userId not in self.users.keys()):
            return []
            
        user = self.users[userId]

        feed = user['tweets'].copy()

        for followee in user['follows']:
            if(followee not in self.users.keys()):
                continue

            followee = self.users[followee]

            l = min(10, len(followee['tweets']))

            feed = feed + followee['tweets'][-l: ]

        feed.sort(key = lambda x: -x[1])

        ans = []
        for i in range(min(10, len(feed))):
            ans.append(feed[i][0])
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if(followerId not in self.users.keys()):
            self.users[followerId] = {
                'follows': set(),
                'tweets': []
            }

        follower = self.users[followerId]
        follower['follows'].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if(followerId not in self.users.keys()):
            return

        follower = self.users[followerId]
        if(followeeId not in follower['follows']):
            return

        follower['follows'].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)