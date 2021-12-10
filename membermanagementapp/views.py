from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Member
from .forms import MemberForm

# Create your views here.
def index(request):
    members = Member.objects.all()

    context = {
        'members': members
    }
    return render(request, 'membermanagementapp/index.html', context)

# def add_item(request):
#     return render(request, 'membermanagementapp/addItem.html')

# def add_item(request):
# 	form = MemberForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
#         # return redirect('/')
# 	context = {
# 		"form": form,
# 	}
# 	return render(request, "membermanagementapp/addItem.html", context)
def add_item(request):
	if request.method == 'POST':
		form = MemberForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = MemberForm()
	context = {
		'form': form
	}
	return render(request, "membermanagementapp/addItem.html", context)