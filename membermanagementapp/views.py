from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Member
from .forms import MemberForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

class MemberList(ListView):
    model = Member
    context_object_name = 'members'
    template_name = 'membermanagementapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] =  Member.objects.all().order_by('role')
        context['count_members'] =  Member.objects.filter(role='Regular Member').count()

        return context


class MemberCreate(CreateView):
    model = Member
    context_object_name = 'form'
    fields = '__all__'
    success_url = reverse_lazy('membermangement-index')
    template_name = 'membermanagementapp/addMember.html'



class MemberUpdate(UpdateView):
    model = Member
    context_object_name = 'form'
    fields = '__all__'
    success_url = reverse_lazy('membermangement-index')
    template_name = 'membermanagementapp/editMember.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member_by_id'] =  Member.objects.get(id=self.kwargs['pk'])

        return context


class MemberDelete(DeleteView):
    model = Member
    context_object_name = 'form'
    success_url = reverse_lazy('membermangement-index')
    template_name = 'membermanagementapp/deleteMember.html'
