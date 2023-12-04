from concurrent import futures
import grpc
import time

# Import the generated classes from protobuf
import Reddit_pb2
import Reddit_pb2_grpc

# In-memory storage for posts and comments
posts = {}
comments = {}

def TopComments(id, N):
        comment_lib = []
        for comment in comments[id].comment_replies:
            comment_lib.append(comment)
        # Fetch all comments and sort them based on the score
        score = {}
        for comment in comment_lib:
            score[comment] = comments[comment].score
        sorted_comments = sorted(score.items(), key=lambda x: x[1], reverse=True)
        top_comments = sorted_comments[:N]
        return top_comments

# Server implementation
class ParallelRedditServicer(Reddit_pb2_grpc.ParallelRedditServicer):

    def CreatePost(self, request, context):
        post_id = str(len(posts))
        request.post_id = post_id
        posts[post_id] = request
        return request

    def UpvotePost(self, request, context):
        if request.upvote_post in posts.keys():
            posts[request.upvote_post].score += 1
            return posts[request.upvote_post]
        else:
            context.abort(grpc.StatusCode.NOT_FOUND, "Post not found")

    def DownvotePost(self, request, context):
        if request.downvote_post in posts.keys():
            posts[request.downvote_post].score -= 1
            return posts[request.downvote_post]
        else:
            context.abort(grpc.StatusCode.NOT_FOUND, "Post not found")


    def RetrievePostContent(self, request, context):
        if request.retrieve_post in posts.keys():
            return posts[request.retrieve_post]
        else:
            context.abort(grpc.StatusCode.NOT_FOUND, "Post not found")

    def CreateComment(self, request, context):
        comment_id = str(len(comments))
        request.comment_id = comment_id
        comments[comment_id] = request

        if request.HasField('parent_post_id'):
            if request.parent_post_id in posts:
                posts[request.parent_post_id].post_replies.append(request.comment_id)
                # print("postsid")
                # print(request.comment_id)
            else:
                context.abort(grpc.StatusCode.NOT_FOUND, "Parent post not found")

        elif request.HasField('parent_comment_id'):
            if request.parent_comment_id in comments:
                comments[request.parent_comment_id].comment_replies.append(request.comment_id)
            else:
                context.abort(grpc.StatusCode.NOT_FOUND, "Parent comment not found")
        
        # print("comments")
        # print(comments)
        # print("posts")
        # print(posts)

        return request

    def UpvoteComment(self, request, context):
        if request.upvote_comment in comments.keys():
            comments[request.upvote_comment].score += 1
            return comments[request.upvote_comment]
        else:
            context.abort(grpc.StatusCode.NOT_FOUND, "Comment not found")

    def DownvoteComment(self, request, context):
        if request.downvote_comment in comments.keys():
            comments[request.downvote_comment].score -= 1
            return comments[request.downvote_comment]
        else:
            context.abort(grpc.StatusCode.NOT_FOUND, "Comment not found")

        
    def GetTopComments(self, request, context):
        # print("comments")
        # print(comments)
        # print("posts")
        # print(posts)
        # print(request.post_branch)
        comment_lib = []
        for post in posts[request.post_branch].post_replies:
            comment_lib.append(post)
        # Fetch all comments and sort them based on the score
        score = {}
        for comment in comment_lib:
            score[comment] = comments[comment].score
        sorted_comments = sorted(score.items(), key=lambda x: x[1], reverse=True)
        top_comments = sorted_comments[:request.N]
        # print(top_comments)
        response = Reddit_pb2.GetTopCommentsResponse()
        for comment in top_comments:
            response.top_comment_id.append(comment[0])
            response.replied.append(len(comments[comment[0]].comment_replies) > 0)
        return response
    
    


    def ExpandCommentBranchDepth2(self, request, context):
        expanded_comments = Reddit_pb2.ExpandCommentBranchResponse()
        first_level_comments = TopComments(request.comment_branch, request.N)
        for comment in first_level_comments:
            subcomment1 = Reddit_pb2.IDList()
            subcomment1.expand_comment_id.append(comment[0])
            expanded_comments.expand_comment.append(subcomment1)
            second_level_comments = TopComments(comment[0], request.N)
            subcomment2 = Reddit_pb2.IDList()
            for subcomment in second_level_comments:
                subcomment2.expand_comment_id.append(subcomment[0])
            expanded_comments.expand_comment.append(subcomment2)
        return expanded_comments
        # for comment in comments[request.comment_branch].comment_replies:
        #     comment_lib.append(comment)
        # comment_score = {}
        # for comment in comment_lib:
        #     comment_score[comment] = comments[comment].score
        # sorted_comments = sorted(comment_score.items(), key=lambda x: x[1], reverse=True)
        # top_level_comments = sorted_comments[:request.N]

        # all_comments = []
        # for comment in top_level_comments:
        #     all_comments.append(comment[0])
        #     # Check if the comment has replies and include top N replies
        #     if comment.comment_id in comments:
        #         # replies = [comments[reply_id] for reply_id in comments[comment.comment_id].comment_replies]
        #         replies = []
        #         for reply in comments[comment.comment_id].comment_replies:
        #             replies.append(reply)
        #         sorted_replies = sorted(replies, key=lambda x: x.score, reverse=True)
        #         all_comments.extend(sorted_replies[:request.N])

        # return Reddit_pb2.CommentList(comments=all_comments)

# Function to run the gRPC server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Reddit_pb2_grpc.add_ParallelRedditServicer_to_server(ParallelRedditServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)  # Server sleeps for a day
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
