import RedditClient
import unittest
from unittest.mock import Mock
import difflib



# Create a mock client
mock = Mock()

# Create a client
client = RedditClient.RedditClient()

# Before test
post0 = client.create_post(title="post0", text="post0")
comment0 = client.create_comment(text="comment0", parent_post_id=post0.post_id)
comment1 = client.create_comment(text="comment1", parent_post_id=post0.post_id, score=1)
comment2 = client.create_comment(text="comment2", parent_comment_id=comment1.comment_id, score=1)
comment3 = client.create_comment(text="comment3", parent_comment_id=comment1.comment_id)
comment4 = client.create_comment(text="comment4", parent_comment_id=comment2.comment_id, score=1)
comment5 = client.create_comment(text="comment5", parent_comment_id=comment2.comment_id)


# Test 1
result1 = client.retrieve_post_content('0').post_id
assert result1 == '0', "retrieve_post failed"

# Test 2
result2 = client.get_top_comments('0', 1).top_comment_id[0]
assert result2 == '1', "get_top_comments failed"

# Test 3
result3 = client.expand_comment_branch_depth2('1', 1).expand_comment
result31 = result3[0].expand_comment_id[0]
result32 = result3[1].expand_comment_id[0]
assert result31 == '2' and result32 == '4', "Expand the most upvoted comment failed"

# Test 4
result4 = client.expand_comment_branch_depth2('1', 1).expand_comment[0].expand_comment_id[0]
assert result4 == '2', "Return the most upvoted reply under the most upvoted comment"






    


