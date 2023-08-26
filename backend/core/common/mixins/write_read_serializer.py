from core.common.mixins.multiple_serializer import MultipleSerializerMixin


class WriteReadSerializerMixin(MultipleSerializerMixin):
    def get_serializer_class_by_action(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return self.serializer_classes.get('write')
        if self.action in ['list', 'retrieve']:
            return self.serializer_classes.get('read')
        return self.serializer_class
