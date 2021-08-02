from user.models import Customer

class PossessionQuerySetMixin:

    def get_queryset(self): 

        customer = self.request.user

        if customer.is_admin:
            return self.model.objects.all()

        if self.model == Customer:
            return self.model.objects.filter(id = customer.id)

        return self.model.objects.filter(user = customer.id)


