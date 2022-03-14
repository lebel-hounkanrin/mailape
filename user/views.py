from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "user/register.html"
    