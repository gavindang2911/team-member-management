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

































# Create your views here.
# def index(request):
#     # members = Member.objects.all()
#     members =  Member.objects.all().order_by('role')
#     # count_members = Member.objects.filter(role='Regular Member').count()
#     # count_admin = Member.objects.filter(role='Admin').count()

#     count_members, count_admin = member_count_helper()

#     context = {
#         'members': members,
#         'count_members': count_members,
#         'count_admin': count_admin
#     }
#     return render(request, 'membermanagementapp/index.html', context)

# def add_item(request):
#     if request.method == 'POST':
#         form = MemberForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = MemberForm()

#     # count_members = Member.objects.filter(role='Regular Member').count()
#     # count_admin = Member.objects.filter(role='Admin').count()
#     count_members, count_admin = member_count_helper()


#     context = {
#         'form': form,
#         'count_members': count_members,
#         'count_admin': count_admin
#     }
#     return render(request, "membermanagementapp/addMember.html", context)

# def edit(request, pk):
#     member_by_id =  Member.objects.get(id=pk)
#     # count_members = Member.objects.filter(role='Regular Member').count()
#     # count_admin = Member.objects.filter(role='Admin').count()
#     count_members, count_admin = member_count_helper()


#     if request.method == 'POST':
#         form = MemberForm(request.POST, instance=member_by_id)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = MemberForm(instance=member_by_id)
#     context = {
#         'form': form,
#         'count_members': count_members,
#         'count_admin': count_admin,
#         'member_by_id': member_by_id
#     }
#     return render(request, 'membermanagementapp/editMember.html', context)

# def delete(request, pk):
#     member_by_id =  Member.objects.get(id=pk)
#     count_members, count_admin = member_count_helper()

#     if request.method == 'POST':
#         member_by_id.delete()
#         return redirect('/')

#     context = {
#         'count_members': count_members,
#         'count_admin': count_admin
#     }

#     return render(request, 'membermanagementapp/deleteMember.html', context)


