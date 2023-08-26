from typing import Dict, Any


class RequestUserSerializerMixin:
    context: Dict[str, Any]

    def get_request_user(self):
        return getattr(self.context.get('request'), 'user', None)
