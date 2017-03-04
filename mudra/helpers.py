import datetime, sys


def convertStringToDatetime(time_string):
	return datetime.datetime.strptime(time_string, '%H-%M-%S')


def convertDatetimeToString(datetime_object):
	return datetime.datetime.strftime(datetime_object, '%H-%M-%S')


def convertTimeDeltaToString(timedelta_object):
	return datetime.time(0, 0, timedelta_object.seconds).strftime('%H-%M-%S')


def sanitizeTimes(sunrise, sunset):
	sunrise = convertStringToDatetime(sunrise)
	sunset = convertStringToDatetime(sunset)

	if (sunset - sunrise) > datetime.timedelta(hours=4) and sunset > sunrise:
		pass
	else:
		# TODO: redirect to error page
		sys.exit(0)


def getDayHoaraTime(sunrise, sunset):
	sunrise = convertStringToDatetime(sunrise)
	sunset = convertStringToDatetime(sunset)

	day_hoara = (sunset - sunrise) / 12
	day_hoara = day_hoara - datetime.timedelta(microseconds=day_hoara.microseconds)

	return day_hoara


def getNightHoaraTime(sunrise, sunset):
	sunrise = convertStringToDatetime(sunrise)
	sunset = convertStringToDatetime(sunset)

	night_hoara = (datetime.timedelta(hours=24) - (sunset - sunrise)) / 12
	night_hoara = night_hoara - datetime.timedelta(microseconds=night_hoara.microseconds)

	return night_hoara


def makeHoaraTimesList(sunrise, sunset):
	day_hoara = getDayHoaraTime(sunrise, sunset)
	night_hoara = getNightHoaraTime(sunrise, sunset)
	hoara_list = [sunrise, ]

	for i in range(0, 11):
		hoara_list.append(convertDatetimeToString(convertStringToDatetime(hoara_list[-1]) + day_hoara))
	hoara_list.append(sunset)

	for i in range(0, 11):
		hoara_list.append(convertDatetimeToString(convertStringToDatetime(hoara_list[-1]) + night_hoara))
	hoara_list.append(sunrise)

	return hoara_list


def getWeekHoaraList():
	sun_hoaras = ['Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon',
			  'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun',
			  'Venus', 'Mercury']
	mon_hoaras = ['Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars',
			  'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon',
			  'Saturn', 'Jupiter']
	tue_hoaras = ['Mars', 'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury',
			  'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars',
			  'Sun', 'Venus']
	wed_hoaras = ['Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn',
			  'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus',
			  'Mercury', 'Moon', 'Saturn']
	thu_hoaras = ['Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus',
			  'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'ercury', 'Moon', 'Saturn',
			  'Jupiter', 'Mars', 'Sun']
	fri_hoaras = ['Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon',
			  'Saturn',
			  'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus',
			  'Mercury', 'Moon']
	sat_hoaras = ['Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun',
			  'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon',
			  'Saturn',
			  'Jupiter', 'Mars']

	hoara_dict = {'Sun': 'Neutral', 'Venus': 'Good', 'Mercury': 'Good', 'Moon': 'Good', 'Saturn': 'Bad',
			  'Jupiter': 'Good', 'Mars': 'Bad'}

	week_hoaras = [sun_hoaras, mon_hoaras, tue_hoaras, wed_hoaras, thu_hoaras, fri_hoaras, sat_hoaras]

	return week_hoaras, hoara_dict
