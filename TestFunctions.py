import RedditClient
import unittest
from unittest.mock import Mock



class Test:
    def __init__(self, client):
        self.client = client

    def retrieve_post(self, post_id):
        return client.retrieve_post_content(post_id)
    
    def retrieve_most_upvoted_comments(self, post_id):
        return client.get_top_comments(post_id, 1)
    
    def expand_most_upvoted_comment(self, comment_id):
        return client.expand_comment_branch_depth2(comment_id, 1)
    
    def most_upvoted_reply(self, comment_id):
        response = client.expand_comment_branch_depth2(comment_id, 1).expand_comment
        if len(response) > 0:
            return response[0]
        else:
            return None
    


if __name__ == '__main__':
    client = RedditClient.RedditClient()
    # Before test
    post0 = client.create_post(title="post0", text="post0")
    comment0 = client.create_comment(text="comment0", parent_post_id=post0.post_id)
    comment1 = client.create_comment(text="comment1", parent_post_id=post0.post_id, score=1)
    comment2 = client.create_comment(text="comment2", parent_comment_id=comment1.comment_id, score=1)
    comment3 = client.create_comment(text="comment3", parent_comment_id=comment1.comment_id)
    comment4 = client.create_comment(text="comment4", parent_comment_id=comment2.comment_id, score=1)
    comment5 = client.create_comment(text="comment5", parent_comment_id=comment2.comment_id)

    test = Test(client)
    print("test1")
    print(test.retrieve_post('0'))
    print("test2")
    print(test.retrieve_most_upvoted_comments('0'))
    print("test3")
    print(test.expand_most_upvoted_comment('1'))
    print("test4")
    print(test.most_upvoted_reply('1'))

    # print(client.expand_comment_branch_depth2('1', 1))




    


