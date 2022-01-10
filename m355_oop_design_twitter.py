#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-01-07
# Question:
#       Design a simplified version of Twitter where users can post tweets, follow/unfollow another user,
#   and is able to see the 10 most recent tweets in the user's news feed.
#   Your Twitter object will be instantiated and called as such:
#       obj = Twitter()
#       obj.postTweet(userId,tweetId)
#       param_2 = obj.getNewsFeed(userId)
#       obj.follow(followerId,followeeId)
#       obj.unfollow(followerId,followeeId)
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
    '''
    1. Instantiate:
    	a. postId: Each tweet increments this number by one to track the order of posts, starts at 0
        b. post_Ids: Create dict that maps the user as key to a deque of post_Ids
        c. post_hist: Create dict that maps each postId as key to corresponding tweetId
        d. followers: Create dict that maps each user to all users they are following

    2. postTweet:
    	a. For the user that is posting, add the new postId to the list of postIds
        b. Add the postId : tweetId to the history of posts
        c. No need to keep more than 10 posts, remove extras
        c. Increment postId by 1

    3. getNewsFeed:
    	a. Build news_feed from scratch as it is only 10 numbers and not worth trying to save
        b. Iterate each followed user as well as the user itself
        c. Build a list of Ids from the posts of each iterated user
        d. Add the most recent 10 posts from the sorted Ids to a news_feed
        e. Return the newsfeed

    4. controlFollowers: follow/unfollow functions add and discard from followers set
    '''
    def __init__(self):
        self.postId = 0
        self.post_Ids = defaultdict(deque)
        self.followers = defaultdict(set)
        self.post_hist = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post_Ids[userId] += [self.postId]
        self.post_hist[self.postId] = tweetId
        if len(self.post_Ids[userId]) > 10:
            self.post_hist.pop(self.post_Ids[userId].popleft())
        self.postId += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        Ids = []
        news_feed = []
        self.followers[userId].add(userId)
        for user in self.followers[userId]:
            for Id in self.post_Ids[user]:
                Ids += [Id]
        for Id in sorted(Ids)[-1:-11:-1]:
            news_feed += [self.post_hist[Id]]
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
