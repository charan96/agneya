from django.shortcuts import render
from .forms import submit_form


def index(request):
	formClass = submit_form
	if request.method == 'POST':
		form = formClass(data=request.POST)

		if form.is_valid():
			sunrise_time = str(request.POST.get('sunrise-hour', '')) + str(request.POST.get('sunrise-min', '')) + \
					   str(request.POST.get('sunrise-sec', ''))
			sunset_time = str(request.POST.get('sunset-hour', '')) + str(request.POST.get('sunset-min', '')) + \
					  str(request.POST.get('sunset-sec', ''))
			return render(request, 'trial.html', {'form': submit_form})
	return render(request, 'index.html', {'form': submit_form})
