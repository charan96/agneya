from django.shortcuts import render
from .forms import submit_form
import helpers


def index(request):
	formClass = submit_form
	if request.method == 'POST':
		form = formClass(data=request.POST)

		if form.is_valid():
			# %H-%M-%S formatted time
			sunrise_time = '-'.join([str(request.POST.get('sunrise_hour', '')),
							 str(request.POST.get('sunrise_min', '')),
							 str(request.POST.get('sunrise_sec', ''))])

			sunset_time = '-'.join([str(request.POST.get('sunset_hour', '')),
							str(request.POST.get('sunset_min', '')),
							str(request.POST.get('sunset_sec', ''))])

			helpers.sanitizeTimes(sunrise_time, sunset_time)

			return hoara(request, sunrise_time, sunset_time)

	return render(request, 'index.html', {'form': submit_form})


def hoara(request, sunrise, sunset):
	hoara_list = helpers.makeHoaraList(sunrise, sunset)

	return render(request, 'hoara.html', {'sunrise_time': sunrise, 'sunset_time': sunset, 'hoara_list': hoara_list})
