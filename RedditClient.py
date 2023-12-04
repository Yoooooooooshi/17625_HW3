import grpc
import Reddit_pb2
import Reddit_pb2_grpc
from datetime import datetime

class RedditClient:
    def __init__(self, host='localhost', port=50051):
        # Initialize gRPC channel and stub
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = Reddit_pb2_grpc.ParallelRedditStub(self.channel)

    def create_post(self, title=None, text=None, video_url=None, image_url=None, state=Reddit_pb2.Post.NORMAL, score=0, user_id=None, publication_date=datetime.now().isoformat(), post_replies=None):
        # Create a new post
        new_post = Reddit_pb2.Post(
            title=title,
            text=text,
            state=state,
            publication_date=publication_date,
            post_replies=post_replies,
            score=score
        )
        if user_id:
            new_post.author = Reddit_pb2.User(user_id = user_id)
        if video_url is not None and image_url is not None:
            raise Exception("Cannot have both video and image")
        if video_url:
            new_post.video_url = video_url
        if image_url:
            new_post.image_url = image_url
        created_post = self.stub.CreatePost(new_post)
        return created_post

    def upvote_post(self, post_id):
        # Upvote a post
        upvote_request = Reddit_pb2.UpvotePostRequest(upvote_post=post_id)
        upvoted_post = self.stub.UpvotePost(upvote_request)
        return upvoted_post

    def downvote_post(self, post_id):
        # Downvote a post
        downvote_request = Reddit_pb2.DownvotePostRequest(downvote_post=post_id)
        downvoted_post = self.stub.DownvotePost(downvote_request)
        return downvoted_post

    def retrieve_post_content(self, post_id):
        # Retrieve the content of a post
        retrieve_request = Reddit_pb2.RetrievePostContentRequest(retrieve_post=post_id)
        retrieved_post = self.stub.RetrievePostContent(retrieve_request)
        return retrieved_post

    def create_comment(self, text=None, score=0, user_id=None, publication_date=datetime.now().isoformat(), state=Reddit_pb2.Comment.NORMAL, parent_post_id=None, parent_comment_id=None, comment_replies=None):
        # Create a new comment
        new_comment = Reddit_pb2.Comment(
            text=text,
            score=score,
            publication_date=publication_date,
            state=state,
            comment_replies=comment_replies
        )
        if parent_comment_id is not None and parent_post_id is not None:
            raise Exception("Cannot have both parent comment and parent post")
        if parent_post_id:
            new_comment.parent_post_id = parent_post_id
        if parent_comment_id:
            new_comment.parent_comment_id = parent_comment_id
        if user_id:
            new_comment.author = Reddit_pb2.User(user_id=user_id)

        created_comment = self.stub.CreateComment(new_comment)
        return created_comment

    def upvote_comment(self, comment_id):
        # Upvote a comment
        upvote_request = Reddit_pb2.UpvoteCommentRequest(upvote_comment=comment_id)
        upvoted_comment = self.stub.UpvoteComment(upvote_request)
        return upvoted_comment

    def downvote_comment(self, comment_id):
        # Downvote a comment
        downvote_request = Reddit_pb2.DownvoteCommentRequest(downvote_comment=comment_id)
        downvoted_comment = self.stub.DownvoteComment(downvote_request)
        return downvoted_comment

    def get_top_comments(self, post_id, N):
        # Get top N comments under a post
        top_comments_request = Reddit_pb2.GetTopCommentsRequest(post_branch=post_id, N=N)
        top_comments = self.stub.GetTopComments(top_comments_request)
        return top_comments

    def expand_comment_branch_depth2(self, comment_id, N):
        # Expand a comment branch with depth 2
        expand_request = Reddit_pb2.ExpandCommentBranchDepth2Request(comment_branch=comment_id, N=N)
        expanded_branch = self.stub.ExpandCommentBranchDepth2(expand_request)
        return expanded_branch

    def close(self):
        # Close the gRPC channel
        self.channel.close()
