from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, DeletionMixin
from django.urls import reverse_lazy
from .models import Member
from .forms import MemberForm
from django.http import HttpResponseRedirect

class MemberList(ListView):
    model = Member
    template_name = 'team_management/index.html'
    context_object_name = 'members'


class MemberCreate(CreateView):
    model = Member
    form_class = MemberForm
    template_name = "team_management/create.html"
    success_url = reverse_lazy('index')

class MemberEdit(UpdateView, DeletionMixin):
    model = Member
    form_class = MemberForm
    template_name = "team_management/edit.html"
    context_object_name = 'member'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('index')

    def post(self, request, id, *args, **kwargs):
        if "confirm_delete" in self.request.POST:
            return self.delete(request, *args, **kwargs)
        else:
            return super(MemberEdit, self).post(request)

    

    


class MemberDelete(DeleteView):
    model = Member
    context_object_name = 'member'
    template_name = "team_management/edit.html"
    success_url = reverse_lazy('index')