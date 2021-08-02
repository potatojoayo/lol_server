class CreateBySelfMixin:

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)
