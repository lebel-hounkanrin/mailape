from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "user/register.html"
    def get_success_url(self):
        return reverse("mailinglist:mailinglist_list")
    