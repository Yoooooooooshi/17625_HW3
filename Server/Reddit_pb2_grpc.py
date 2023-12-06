# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Reddit_pb2 as Reddit__pb2


class ParallelRedditStub(object):
    """API endpoints for actions related to posts and comments
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreatePost = channel.unary_unary(
                '/ParallelReddit/CreatePost',
                request_serializer=Reddit__pb2.Post.SerializeToString,
                response_deserializer=Reddit__pb2.Post.FromString,
                )
        self.UpvotePost = channel.unary_unary(
                '/ParallelReddit/UpvotePost',
                request_serializer=Reddit__pb2.UpvotePostRequest.SerializeToString,
                response_deserializer=Reddit__pb2.Post.FromString,
                )
        self.DownvotePost = channel.unary_unary(
                '/ParallelReddit/DownvotePost',
                request_serializer=Reddit__pb2.DownvotePostRequest.SerializeToString,
                response_deserializer=Reddit__pb2.Post.FromString,
                )
        self.RetrievePostContent = channel.unary_unary(
                '/ParallelReddit/RetrievePostContent',
                request_serializer=Reddit__pb2.RetrievePostContentRequest.SerializeToString,
                response_deserializer=Reddit__pb2.Post.FromString,
                )
        self.CreateComment = channel.unary_unary(
                '/ParallelReddit/CreateComment',
                request_serializer=Reddit__pb2.Comment.SerializeToString,
                response_deserializer=Reddit__pb2.Comment.FromString,
                )
        self.UpvoteComment = channel.unary_unary(
                '/ParallelReddit/UpvoteComment',
                request_serializer=Reddit__pb2.UpvoteCommentRequest.SerializeToString,
                response_deserializer=Reddit__pb2.Comment.FromString,
                )
        self.DownvoteComment = channel.unary_unary(
                '/ParallelReddit/DownvoteComment',
                request_serializer=Reddit__pb2.DownvoteCommentRequest.SerializeToString,
                response_deserializer=Reddit__pb2.Comment.FromString,
                )
        self.GetTopComments = channel.unary_unary(
                '/ParallelReddit/GetTopComments',
                request_serializer=Reddit__pb2.GetTopCommentsRequest.SerializeToString,
                response_deserializer=Reddit__pb2.GetTopCommentsResponse.FromString,
                )
        self.ExpandCommentBranchDepth2 = channel.unary_unary(
                '/ParallelReddit/ExpandCommentBranchDepth2',
                request_serializer=Reddit__pb2.ExpandCommentBranchDepth2Request.SerializeToString,
                response_deserializer=Reddit__pb2.ExpandCommentBranchResponse.FromString,
                )


class ParallelRedditServicer(object):
    """API endpoints for actions related to posts and comments
    """

    def CreatePost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpvotePost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownvotePost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrievePostContent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpvoteComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownvoteComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTopComments(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExpandCommentBranchDepth2(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ParallelRedditServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreatePost': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePost,
                    request_deserializer=Reddit__pb2.Post.FromString,
                    response_serializer=Reddit__pb2.Post.SerializeToString,
            ),
            'UpvotePost': grpc.unary_unary_rpc_method_handler(
                    servicer.UpvotePost,
                    request_deserializer=Reddit__pb2.UpvotePostRequest.FromString,
                    response_serializer=Reddit__pb2.Post.SerializeToString,
            ),
            'DownvotePost': grpc.unary_unary_rpc_method_handler(
                    servicer.DownvotePost,
                    request_deserializer=Reddit__pb2.DownvotePostRequest.FromString,
                    response_serializer=Reddit__pb2.Post.SerializeToString,
            ),
            'RetrievePostContent': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrievePostContent,
                    request_deserializer=Reddit__pb2.RetrievePostContentRequest.FromString,
                    response_serializer=Reddit__pb2.Post.SerializeToString,
            ),
            'CreateComment': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateComment,
                    request_deserializer=Reddit__pb2.Comment.FromString,
                    response_serializer=Reddit__pb2.Comment.SerializeToString,
            ),
            'UpvoteComment': grpc.unary_unary_rpc_method_handler(
                    servicer.UpvoteComment,
                    request_deserializer=Reddit__pb2.UpvoteCommentRequest.FromString,
                    response_serializer=Reddit__pb2.Comment.SerializeToString,
            ),
            'DownvoteComment': grpc.unary_unary_rpc_method_handler(
                    servicer.DownvoteComment,
                    request_deserializer=Reddit__pb2.DownvoteCommentRequest.FromString,
                    response_serializer=Reddit__pb2.Comment.SerializeToString,
            ),
            'GetTopComments': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTopComments,
                    request_deserializer=Reddit__pb2.GetTopCommentsRequest.FromString,
                    response_serializer=Reddit__pb2.GetTopCommentsResponse.SerializeToString,
            ),
            'ExpandCommentBranchDepth2': grpc.unary_unary_rpc_method_handler(
                    servicer.ExpandCommentBranchDepth2,
                    request_deserializer=Reddit__pb2.ExpandCommentBranchDepth2Request.FromString,
                    response_serializer=Reddit__pb2.ExpandCommentBranchResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ParallelReddit', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ParallelReddit(object):
    """API endpoints for actions related to posts and comments
    """

    @staticmethod
    def CreatePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ParallelReddit/CreatePost',
            Reddit__pb2.Post.SerializeToString,
            Reddit__pb2.Post.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpvotePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ParallelReddit/UpvotePost',
            Reddit__pb2.UpvotePostRequest.SerializeToString,
            Reddit__pb2.Post.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DownvotePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ParallelReddit/DownvotePost',
            Reddit__pb2.DownvotePostRequest.SerializeToString,
            Reddit__pb2.Post.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetrievePostContent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ParallelReddit/RetrievePostContent',
            Reddit__pb2.RetrievePostContentRequest.SerializeToString,
            Reddit__pb2.Post.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ParallelReddit/CreateComment',
            Reddit__pb2.Comment.SerializeToString,
            Reddit__pb2.Comment.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpvoteComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ParallelReddit/UpvoteComment',
            Reddit__pb2.UpvoteCommentRequest.SerializeToString,
            Reddit__pb2.Comment.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DownvoteComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ParallelReddit/DownvoteComment',
            Reddit__pb2.DownvoteCommentRequest.SerializeToString,
            Reddit__pb2.Comment.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTopComments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ParallelReddit/GetTopComments',
            Reddit__pb2.GetTopCommentsRequest.SerializeToString,
            Reddit__pb2.GetTopCommentsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExpandCommentBranchDepth2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ParallelReddit/ExpandCommentBranchDepth2',
            Reddit__pb2.ExpandCommentBranchDepth2Request.SerializeToString,
            Reddit__pb2.ExpandCommentBranchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
