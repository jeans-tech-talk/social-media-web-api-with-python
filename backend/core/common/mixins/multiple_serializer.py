from typing import Dict

from rest_framework import serializers


class MultipleSerializerMixin:
    action: str
    serializer_class: serializers.ModelSerializer
    serializer_classes: Dict[str, serializers.ModelSerializer]

    def get_serializer_class(self):
        serializer_class = self.get_serializer_class_by_action() or self.serializer_class
        assert serializer_class is not None, (
                "'%s' should either include a `serializer_classes` or `serializer_class` attribute, "
                "or override the `get_serializer_class()` method."
                % self.__class__.__name__
        )
        return serializer_class

    def get_serializer_class_by_action(self):
        pass
