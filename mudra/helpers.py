import datetime, sys


def convertStringToDatetime(time_string):
	return datetime.datetime.strptime(time_string, '%H:%M:%S')


def convertDatetimeToString(datetime_object):
	return datetime.datetime.strftime(datetime_object, '%H:%M:%S')


def convertTimeDeltaToString(timedelta_object):
	return datetime.time(0, 0, timedelta_object.seconds).strftime('%H:%M:%S')


def convert24HourTimeStringTo12HourTimeString(time_string):
	temp = datetime.datetime.strptime(time_string, '%H:%M:%S')
	temp = datetime.datetime.strftime(temp, '%I:%M %p')

	return temp


def formChoicesHourList():
	temp_list = ['12 AM', ]
	for x in range(1, 12):
		temp_list.append(str(x) + " AM")

	temp_list.append('12 PM')

	for x in range(1, 12):
		temp_list.append(str(x) + " PM")

	return temp_list


def validateInputTimes(sunrise, sunset):
	sunrise = convertStringToDatetime(sunrise)
	sunset = convertStringToDatetime(sunset)

	if (sunset - sunrise) > datetime.timedelta(hours=4) and sunset > sunrise:
		return True
	else:
		return False


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


def getTeluguHoaraDict():
	telugu_hoaras = {'Sun': u'\u0C38\u0C42', 'Venus': u'\u0C36\u0C41', 'Mercury': u'\u0C2C\u0C41',
			     'Moon': u'\u0C1A\u0C02', 'Saturn': u'\u0C36', 'Jupiter': u'\u0C17\u0C41',
			     'Mars': u'\u0C15\u0C41'}

	return telugu_hoaras


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
			  'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn',
			  'Jupiter', 'Mars', 'Sun']
	fri_hoaras = ['Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon',
			  'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars',
			  'Sun', 'Venus', 'Mercury', 'Moon']
	sat_hoaras = ['Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun',
			  'Venus', 'Mercury', 'Moon', 'Saturn', 'Jupiter', 'Mars', 'Sun', 'Venus', 'Mercury', 'Moon',
			  'Saturn', 'Jupiter', 'Mars']

	hoara_dict = {'Sun': 'Neutral', 'Venus': 'Good', 'Mercury': 'Good', 'Moon': 'Good', 'Saturn': 'Bad',
			  'Jupiter': 'Good', 'Mars': 'Bad'}

	week_hoaras = [sun_hoaras, mon_hoaras, tue_hoaras, wed_hoaras, thu_hoaras, fri_hoaras, sat_hoaras]

	telugu_hoaras = getTeluguHoaraDict()

	return week_hoaras, hoara_dict, telugu_hoaras
