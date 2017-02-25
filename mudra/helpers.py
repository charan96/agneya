import datetime


def convertStringToDatetime(time_string):
	return datetime.datetime.strptime(time_string, '%H-%M-%S')


def convertDatetimeToString(datetime_object):
	return datetime.datetime.strftime(datetime_object, '%H-%M-%S')


def convertTimeDeltaToString(timedelta_object):
	return datetime.time(0, 0, timedelta_object.seconds).strftime('%H-%M-%S')


def getHoaraTime(sunrise, sunset):
	sunrise = convertStringToDatetime(sunrise)
	sunset = convertStringToDatetime(sunset)

	day_hoara = (sunset - sunrise) / 12
	day_hoara = day_hoara - datetime.timedelta(microseconds=day_hoara.microseconds)

	return day_hoara


def makeHoaraList(sunrise, sunset):
	day_hoara = getHoaraTime(sunrise, sunset)
	hoara_list = [sunrise, ]

	for i in range(0, 24):
		hoara_list.append(convertDatetimeToString(convertStringToDatetime(hoara_list[-1]) + day_hoara))

	return hoara_list
