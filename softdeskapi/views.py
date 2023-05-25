class MultipleSerializerMixin:

    detail_serializer_class = None
    create_serializer_class= None
    modify_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'create' and self.create_serializer_class is not None:
            return self.create_serializer_class
        elif self.action in ['update', 'partial_update'] and self.modify_serializer_class is not None:
            return self.modify_serializer_class
        elif self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()