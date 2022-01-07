#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-01-07
# Question:
#       Design a simplified version of Twitter where users can post tweets, follow/unfollow another user,
#   and is able to see the 10 most recent tweets in the user's news feed.
# Example:
#       Input
#       ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
#       [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
#       Output
#       [null, null, [5], null, null, [6, 5], null, [5]]
# Constraints:
#       1 <= userId, followerId, followeeId <= 500
#       0 <= tweetId <= 104
#       All the tweets have unique IDs.
#       At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
##

class Twitter:
    def __init__(self):
        self.post_nums = defaultdict(list)
        self.post_hist = defaultdict(list)
        self.followers = defaultdict(list)
        self.postId = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post_nums[userId] += [self.postId]
        self.post_hist[self.postId] = tweetId
        self.postId += 1

        
    def getNewsFeed(self, userId: int) -> List[int]:
        ids = []
        news_feed = []

        for user in self.followers[userId] + [userId]:
            for i in self.post_nums[user][-1:-11:-1]:
                ids += [i]

        for i in sorted(ids)[-1:-11:-1]:
            news_feed += [self.post_hist[i]]

        return news_feed


    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers[followerId]:
            self.followers[followerId] += [followeeId]


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
