# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import coordinator_service_pb2 as coordinator__service__pb2


class CoordinatorServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateContent = channel.unary_unary(
            "/indexify_coordinator.CoordinatorService/CreateContent",
            request_serializer=coordinator__service__pb2.CreateContentRequest.SerializeToString,
            response_deserializer=coordinator__service__pb2.CreateContentResponse.FromString,
        )
        self.GetContentMetadata = channel.unary_unary(
            "/indexify_coordinator.CoordinatorService/GetContentMetadata",
            request_serializer=coordinator__service__pb2.GetContentMetadataRequest.SerializeToString,
            response_deserializer=coordinator__service__pb2.GetContentMetadataResponse.FromString,
        )
        self.ListContent = channel.unary_unary(
            "/indexify_coordinator.CoordinatorService/ListContent",
            request_serializer=coordinator__service__pb2.ListContentRequest.SerializeToString,
            response_deserializer=coordinator__service__pb2.ListContentResponse.FromString,
        )
        self.CreateBinding = channel.unary_unary(
            "/indexify_coordinator.CoordinatorService/CreateBinding",
            request_serializer=coordinator__service__pb2.ExtractorBindRequest.SerializeToString,
            response_deserializer=coordinator__service__pb2.ExtractorBindResponse.FromString,
        )
        self.ListBindings = channel.unary_unary(
            "/indexify_coordinator.CoordinatorService/ListBindings",
            request_serializer=coordinator__service__pb2.ListBindingsRequest.SerializeToString,
            response_deserializer=coordinator__service__pb2.ListBindingsResponse.FromString,
        )
        self.CreateRepository = channel.unary_unary(
            "/indexify_coordinator.CoordinatorService/CreateRepository",
            request_serializer=coordinator__service__pb2.CreateRepositoryRequest.SerializeToString,
            response_deserializer=coordinator__service__pb2.CreateRepositoryResponse.FromString,
        )
        self.ListRepositories = channel.unary_unary(
            "/indexify_coordinator.CoordinatorService/ListRepositories",
            request_serializer=coordinator__service__pb2.ListRepositoriesRequest.SerializeToString,
            response_deserializer=coordinator__service__pb2.ListRepositoriesResponse.FromString,
        )
        self.GetRepository = channel.unary_unary(
            "/indexify_coordinator.CoordinatorService/GetRepository",
            request_serializer=coordinator__service__pb2.GetRepositoryRequest.SerializeToString,
            response_deserializer=coordinator__service__pb2.GetRepositoryResponse.FromString,
        )
        self.ListExtractors = channel.unary_unary(
            "/indexify_coordinator.CoordinatorService/ListExtractors",
            request_serializer=coordinator__service__pb2.ListExtractorsRequest.SerializeToString,
            response_deserializer=coordinator__service__pb2.ListExtractorsResponse.FromString,
        )
        self.RegisterExecutor = channel.unary_unary(
            "/indexify_coordinator.CoordinatorService/RegisterExecutor",
            request_serializer=coordinator__service__pb2.RegisterExecutorRequest.SerializeToString,
            response_deserializer=coordinator__service__pb2.RegisterExecutorResponse.FromString,
        )
        self.Heartbeat = channel.stream_stream(
            "/indexify_coordinator.CoordinatorService/Heartbeat",
            request_serializer=coordinator__service__pb2.HeartbeatRequest.SerializeToString,
            response_deserializer=coordinator__service__pb2.HeartbeatResponse.FromString,
        )
        self.ListIndexes = channel.unary_unary(
            "/indexify_coordinator.CoordinatorService/ListIndexes",
            request_serializer=coordinator__service__pb2.ListIndexesRequest.SerializeToString,
            response_deserializer=coordinator__service__pb2.ListIndexesResponse.FromString,
        )
        self.GetIndex = channel.unary_unary(
            "/indexify_coordinator.CoordinatorService/GetIndex",
            request_serializer=coordinator__service__pb2.GetIndexRequest.SerializeToString,
            response_deserializer=coordinator__service__pb2.GetIndexResponse.FromString,
        )
        self.CreateIndex = channel.unary_unary(
            "/indexify_coordinator.CoordinatorService/CreateIndex",
            request_serializer=coordinator__service__pb2.CreateIndexRequest.SerializeToString,
            response_deserializer=coordinator__service__pb2.CreateIndexResponse.FromString,
        )
        self.GetExtractorCoordinates = channel.unary_unary(
            "/indexify_coordinator.CoordinatorService/GetExtractorCoordinates",
            request_serializer=coordinator__service__pb2.GetExtractorCoordinatesRequest.SerializeToString,
            response_deserializer=coordinator__service__pb2.GetExtractorCoordinatesResponse.FromString,
        )
        self.UpdateTask = channel.unary_unary(
            "/indexify_coordinator.CoordinatorService/UpdateTask",
            request_serializer=coordinator__service__pb2.UpdateTaskRequest.SerializeToString,
            response_deserializer=coordinator__service__pb2.UpdateTaskResponse.FromString,
        )
        self.ListStateChanges = channel.unary_unary(
            "/indexify_coordinator.CoordinatorService/ListStateChanges",
            request_serializer=coordinator__service__pb2.ListStateChangesRequest.SerializeToString,
            response_deserializer=coordinator__service__pb2.ListStateChangesResponse.FromString,
        )
        self.ListTasks = channel.unary_unary(
            "/indexify_coordinator.CoordinatorService/ListTasks",
            request_serializer=coordinator__service__pb2.ListTasksRequest.SerializeToString,
            response_deserializer=coordinator__service__pb2.ListTasksResponse.FromString,
        )


class CoordinatorServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateContent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetContentMetadata(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListContent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateBinding(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListBindings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateRepository(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListRepositories(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetRepository(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListExtractors(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def RegisterExecutor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Heartbeat(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListIndexes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetIndex(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateIndex(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetExtractorCoordinates(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListStateChanges(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListTasks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_CoordinatorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateContent": grpc.unary_unary_rpc_method_handler(
            servicer.CreateContent,
            request_deserializer=coordinator__service__pb2.CreateContentRequest.FromString,
            response_serializer=coordinator__service__pb2.CreateContentResponse.SerializeToString,
        ),
        "GetContentMetadata": grpc.unary_unary_rpc_method_handler(
            servicer.GetContentMetadata,
            request_deserializer=coordinator__service__pb2.GetContentMetadataRequest.FromString,
            response_serializer=coordinator__service__pb2.GetContentMetadataResponse.SerializeToString,
        ),
        "ListContent": grpc.unary_unary_rpc_method_handler(
            servicer.ListContent,
            request_deserializer=coordinator__service__pb2.ListContentRequest.FromString,
            response_serializer=coordinator__service__pb2.ListContentResponse.SerializeToString,
        ),
        "CreateBinding": grpc.unary_unary_rpc_method_handler(
            servicer.CreateBinding,
            request_deserializer=coordinator__service__pb2.ExtractorBindRequest.FromString,
            response_serializer=coordinator__service__pb2.ExtractorBindResponse.SerializeToString,
        ),
        "ListBindings": grpc.unary_unary_rpc_method_handler(
            servicer.ListBindings,
            request_deserializer=coordinator__service__pb2.ListBindingsRequest.FromString,
            response_serializer=coordinator__service__pb2.ListBindingsResponse.SerializeToString,
        ),
        "CreateRepository": grpc.unary_unary_rpc_method_handler(
            servicer.CreateRepository,
            request_deserializer=coordinator__service__pb2.CreateRepositoryRequest.FromString,
            response_serializer=coordinator__service__pb2.CreateRepositoryResponse.SerializeToString,
        ),
        "ListRepositories": grpc.unary_unary_rpc_method_handler(
            servicer.ListRepositories,
            request_deserializer=coordinator__service__pb2.ListRepositoriesRequest.FromString,
            response_serializer=coordinator__service__pb2.ListRepositoriesResponse.SerializeToString,
        ),
        "GetRepository": grpc.unary_unary_rpc_method_handler(
            servicer.GetRepository,
            request_deserializer=coordinator__service__pb2.GetRepositoryRequest.FromString,
            response_serializer=coordinator__service__pb2.GetRepositoryResponse.SerializeToString,
        ),
        "ListExtractors": grpc.unary_unary_rpc_method_handler(
            servicer.ListExtractors,
            request_deserializer=coordinator__service__pb2.ListExtractorsRequest.FromString,
            response_serializer=coordinator__service__pb2.ListExtractorsResponse.SerializeToString,
        ),
        "RegisterExecutor": grpc.unary_unary_rpc_method_handler(
            servicer.RegisterExecutor,
            request_deserializer=coordinator__service__pb2.RegisterExecutorRequest.FromString,
            response_serializer=coordinator__service__pb2.RegisterExecutorResponse.SerializeToString,
        ),
        "Heartbeat": grpc.stream_stream_rpc_method_handler(
            servicer.Heartbeat,
            request_deserializer=coordinator__service__pb2.HeartbeatRequest.FromString,
            response_serializer=coordinator__service__pb2.HeartbeatResponse.SerializeToString,
        ),
        "ListIndexes": grpc.unary_unary_rpc_method_handler(
            servicer.ListIndexes,
            request_deserializer=coordinator__service__pb2.ListIndexesRequest.FromString,
            response_serializer=coordinator__service__pb2.ListIndexesResponse.SerializeToString,
        ),
        "GetIndex": grpc.unary_unary_rpc_method_handler(
            servicer.GetIndex,
            request_deserializer=coordinator__service__pb2.GetIndexRequest.FromString,
            response_serializer=coordinator__service__pb2.GetIndexResponse.SerializeToString,
        ),
        "CreateIndex": grpc.unary_unary_rpc_method_handler(
            servicer.CreateIndex,
            request_deserializer=coordinator__service__pb2.CreateIndexRequest.FromString,
            response_serializer=coordinator__service__pb2.CreateIndexResponse.SerializeToString,
        ),
        "GetExtractorCoordinates": grpc.unary_unary_rpc_method_handler(
            servicer.GetExtractorCoordinates,
            request_deserializer=coordinator__service__pb2.GetExtractorCoordinatesRequest.FromString,
            response_serializer=coordinator__service__pb2.GetExtractorCoordinatesResponse.SerializeToString,
        ),
        "UpdateTask": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateTask,
            request_deserializer=coordinator__service__pb2.UpdateTaskRequest.FromString,
            response_serializer=coordinator__service__pb2.UpdateTaskResponse.SerializeToString,
        ),
        "ListStateChanges": grpc.unary_unary_rpc_method_handler(
            servicer.ListStateChanges,
            request_deserializer=coordinator__service__pb2.ListStateChangesRequest.FromString,
            response_serializer=coordinator__service__pb2.ListStateChangesResponse.SerializeToString,
        ),
        "ListTasks": grpc.unary_unary_rpc_method_handler(
            servicer.ListTasks,
            request_deserializer=coordinator__service__pb2.ListTasksRequest.FromString,
            response_serializer=coordinator__service__pb2.ListTasksResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "indexify_coordinator.CoordinatorService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class CoordinatorService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateContent(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/indexify_coordinator.CoordinatorService/CreateContent",
            coordinator__service__pb2.CreateContentRequest.SerializeToString,
            coordinator__service__pb2.CreateContentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetContentMetadata(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/indexify_coordinator.CoordinatorService/GetContentMetadata",
            coordinator__service__pb2.GetContentMetadataRequest.SerializeToString,
            coordinator__service__pb2.GetContentMetadataResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ListContent(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/indexify_coordinator.CoordinatorService/ListContent",
            coordinator__service__pb2.ListContentRequest.SerializeToString,
            coordinator__service__pb2.ListContentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CreateBinding(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/indexify_coordinator.CoordinatorService/CreateBinding",
            coordinator__service__pb2.ExtractorBindRequest.SerializeToString,
            coordinator__service__pb2.ExtractorBindResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ListBindings(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/indexify_coordinator.CoordinatorService/ListBindings",
            coordinator__service__pb2.ListBindingsRequest.SerializeToString,
            coordinator__service__pb2.ListBindingsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CreateRepository(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/indexify_coordinator.CoordinatorService/CreateRepository",
            coordinator__service__pb2.CreateRepositoryRequest.SerializeToString,
            coordinator__service__pb2.CreateRepositoryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ListRepositories(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/indexify_coordinator.CoordinatorService/ListRepositories",
            coordinator__service__pb2.ListRepositoriesRequest.SerializeToString,
            coordinator__service__pb2.ListRepositoriesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetRepository(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/indexify_coordinator.CoordinatorService/GetRepository",
            coordinator__service__pb2.GetRepositoryRequest.SerializeToString,
            coordinator__service__pb2.GetRepositoryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ListExtractors(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/indexify_coordinator.CoordinatorService/ListExtractors",
            coordinator__service__pb2.ListExtractorsRequest.SerializeToString,
            coordinator__service__pb2.ListExtractorsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def RegisterExecutor(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/indexify_coordinator.CoordinatorService/RegisterExecutor",
            coordinator__service__pb2.RegisterExecutorRequest.SerializeToString,
            coordinator__service__pb2.RegisterExecutorResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Heartbeat(
        request_iterator,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            "/indexify_coordinator.CoordinatorService/Heartbeat",
            coordinator__service__pb2.HeartbeatRequest.SerializeToString,
            coordinator__service__pb2.HeartbeatResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ListIndexes(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/indexify_coordinator.CoordinatorService/ListIndexes",
            coordinator__service__pb2.ListIndexesRequest.SerializeToString,
            coordinator__service__pb2.ListIndexesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetIndex(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/indexify_coordinator.CoordinatorService/GetIndex",
            coordinator__service__pb2.GetIndexRequest.SerializeToString,
            coordinator__service__pb2.GetIndexResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CreateIndex(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/indexify_coordinator.CoordinatorService/CreateIndex",
            coordinator__service__pb2.CreateIndexRequest.SerializeToString,
            coordinator__service__pb2.CreateIndexResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetExtractorCoordinates(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/indexify_coordinator.CoordinatorService/GetExtractorCoordinates",
            coordinator__service__pb2.GetExtractorCoordinatesRequest.SerializeToString,
            coordinator__service__pb2.GetExtractorCoordinatesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UpdateTask(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/indexify_coordinator.CoordinatorService/UpdateTask",
            coordinator__service__pb2.UpdateTaskRequest.SerializeToString,
            coordinator__service__pb2.UpdateTaskResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ListStateChanges(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/indexify_coordinator.CoordinatorService/ListStateChanges",
            coordinator__service__pb2.ListStateChangesRequest.SerializeToString,
            coordinator__service__pb2.ListStateChangesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ListTasks(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/indexify_coordinator.CoordinatorService/ListTasks",
            coordinator__service__pb2.ListTasksRequest.SerializeToString,
            coordinator__service__pb2.ListTasksResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
