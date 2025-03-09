class SuccessMessageMixin:
    success_message = "Operation succeeded!"

    def form_valid(self, form):
        response = super().form_valid(form)
        print(self.success_message)
        return response
