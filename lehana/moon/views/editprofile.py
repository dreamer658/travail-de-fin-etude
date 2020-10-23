from django.http import HttpResponseRedirect
from django.views.generic import FormView, UpdateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from moon.forms.userRegisterForm import UserRegisterForm
from moon.models.profile import UserProfile

class EditProfileView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = 'userRegister.html'
    fields = ('birthday',)

    def get_object(self, queryset=None):
        return self.request.user.userprofile
