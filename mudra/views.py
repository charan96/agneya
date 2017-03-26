from django.shortcuts import render
from .forms import submit_form
import helpers


def index(request):
	formClass = submit_form
	if request.method == 'POST':
		form = formClass(data=request.POST)

		if form.is_valid():
			# %H-%M-%S formatted time
			sunrise_time = ':'.join([str(request.POST.get('sunrise_hour', '')),
							 str(request.POST.get('sunrise_min', '')),
							 str(request.POST.get('sunrise_sec', ''))])

			sunset_time = ':'.join([str(request.POST.get('sunset_hour', '')),
							str(request.POST.get('sunset_min', '')),
							str(request.POST.get('sunset_sec', ''))])

			# check if input times are valid i.e, sunset atleast 4 hrs after sunrise
			if not helpers.validateInputTimes(sunrise_time, sunset_time):
				return render(request, 'error.html', {})

			return hoara(request, sunrise_time, sunset_time)

	return render(request, 'index.html', {'form': submit_form})


def hoara(request, sunrise, sunset):
	hoara_list = helpers.makeHoaraTimesList(sunrise, sunset)
	start_times = hoara_list[:-1]
	end_times = hoara_list[1:]

	week_hoaras, hoara_dict, telugu_hoaras = helpers.getWeekHoaraList()

	zipped_list = [(helpers.convert24HourTimeStringTo12HourTimeString(start_times[x]),
			    helpers.convert24HourTimeStringTo12HourTimeString(end_times[x]), week_hoaras[0][x],
			    week_hoaras[1][x], week_hoaras[2][x],
			    week_hoaras[3][x], week_hoaras[4][x], week_hoaras[5][x], week_hoaras[6][x]) for x in range(0, 24)]

	return render(request, 'hoara.html', {'sunrise_time': sunrise, 'sunset_time': sunset,
							  'zipped_list': zipped_list, 'hoara_dict': hoara_dict,
							  'telugu_hoaras': telugu_hoaras})
