import math
import datetime

stars = {
    'Alpheratz': '357d41.7,29d10.9',
    'Ankaa': '353d14.1,-42d13.4',
    'Schedar': '349d38.4,56d37.7',
    'Diphda':'348d54.1,-17d54.1',
    'Achernar':	'335d25.5,-57d09.7',
    'Hamal': '327d58.7,23d32.3',
    'Polaris':'316d41.3,89d20.1',
    'Akamar':'315d16.8,-40d14.8',
    'Menkar':'314d13.0,4d09.0',
    'Mirfak':'308d37.4,49d55.1',
    'Aldebaran':	'290d47.1,16d32.3',
    'Rigel':	'281d10.1,-8d11.3',
    'Capella':	'280d31.4,46d00.7',
    'Bellatrix':	'278d29.8,6d21.6',
    'Elnath':	'278d10.1,28d37.1',
    'Alnilam':	'275d44.3,-1d11.8',
    'Betelgeuse':'270d59.1,7d24.3',
    'Canopus':	'263d54.8,-52d42.5',
    'Sirius':	'258d31.7,-16d44.3',
    'Adara':	'255d10.8,-28d59.9',
    'Procyon':	'244d57.5,5d10.9',
    'Pollux':	'243d25.2,27d59.0',
    'Avior':	'234d16.6,-59d33.7',
    'Suhail':'222d50.7,-43d29.8',
    'Miaplacidus':	'221d38.4,-69d46.9',
    'Alphard':	'217d54.1,-8d43.8',
    'Regulus':	'207d41.4,11d53.2',
    'Dubhe':	'193d49.4,61d39.5',
    'Denebola':	'182d31.8,14d28.9',
    'Gienah':	'175d50.4,-17d37.7',
    'Acrux':	'173d07.2,-63d10.9',
    'Gacrux':	'171d58.8,-57d11.9',
    'Alioth':'166d19.4,55d52.1',
    'Spica':	'158d29.5,-11d14.5',
    'Alcaid':	'152d57.8,49d13.8',
    'Hadar':	'148d45.5,-60d26.6',
    'Menkent':'148d05.6,-36d26.6',
    'Arcturus':	'145d54.2,19d06.2',
    'Rigil Kent.':'139d49.6,-60d53.6',
    'Zubenelg.':	'137d03.7,-16d06.3',
    'Kochab':	'137d21.0,74d05.2',
    'Alphecca':'126d09.9,26d39.7',
    'Antares':	'112d24.4,-26d27.8',
    'Atria':	'107d25.2,-69d03.0',
    'Sabik':	'102d10.9,-15d44.4',
    'Shaula'	:'96d20.0,-37d06.6',
    'Rasalhague':	'96d05.2,12d33.1',
    'Etamin'	:'90d45.9,51d29.3',
    'Kaus Aust.':	'83d41.9,-34d22.4',
    'Vega'	:'80d38.2,38d48.1',
    'Nunki'	:'75d56.6,-26d16.4',
    'Altair'	:'62d06.9,8d54.8',
    'Peacock'	:'53d17.2,-56d41.0',
    'Deneb'	:'49d30.7,45d20.5',
    'Enif'	:'33d45.7,9d57.0',
    'Alnair'	:'27d42.0,-46d53.1',
    'Fomalhaut'	:'15d22.4,-29d32.3',
    'Scheat'	:'13d51.8,28d10.3',
    'Markab'	:'13d36.7,15d17.6'
}

def predict(values):
    output = values.copy()

    if 'lat' in values or 'long' in values:
        output['error'] = 'lat or long already exists in the input'
        return output

    # body
    if 'body' not in values:
        output['error'] = 'mandatory information is missing'
        return output

    # date (this will default to the correct time also)
    # Always use actual types within code; use the correct format to output
    dateAndTime = datetime.datetime.strptime('2001-01-01', '%Y-%m-%d')

    if 'date' in values:
        try:
            date = values['date'].split('-')

            if len(date) != 3:
                output['error'] = 'date is invalid'
                return output

            # validate year (length of 4)
            year = date[0]
            if len(year) is not 4 or int(year) < 2001:
                output['error'] = 'date is invalid'
                return output

            # validate month (no need to check if valid month - strptime does it)
            month = date[1]
            if len(month) is not 2:
                output['error'] = 'date is invalid'
                return output

            # validate day
            day = date[2]
            if len(day) is not 2:
                output['error'] = 'date is invalid'
                return output

            dateAndTime = datetime.datetime.strptime(values['date'], '%Y-%m-%d')
        except ValueError:
            output['error'] = 'date is invalid'
            return output

    # time
    if 'time' in values:
        try:
            time = values['time'].split(':')

            if len(time) != 3:
                output['error'] = 'time is invalid'
                return output

            # validate hour (length of 2)
            hour = time[0]
            if len(hour) is not 2:
                output['error'] = 'time is invalid'
                return output

            # validate min
            min = time[1]
            if len(min) is not 2:
                output['error'] = 'time is invalid'
                return output

            # validate sec
            sec = time[2]
            if len(sec) is not 2:
                output['error'] = 'time is invalid'
                return output

            dateAndTime = dateAndTime.replace(hour=int(hour), minute=int(min), second=int(sec))
        except ValueError:
            output['error'] = 'time is invalid'
            return output

    # lat, sha
    star = values['body'][0].upper() + values['body'].lower()[1:]
    if star not in stars:
        output['error'] = 'star is invalid'
        return output
    lat = stars[star].split(',')[1]
    sha = stars[star].split(',')[0]

    # greenwich hour angle of aries
    ghaAries = degreesFromFormattedAlt('100d42.6')
    refDateAndTime = datetime.datetime.strptime('2001', '%Y')
    refYear = refDateAndTime.year

    cumulativeProgression = -1*(degreesFromFormattedAlt('0d14.31667') * (dateAndTime.year - refYear))
    print('cumulativeProgression', formatAlt(cumulativeProgression))
    leapYears = numOfLeapYears(refYear, dateAndTime.year)
    earthRotation = 86164.1
    earthClock = 86400
    earthDegrees = degreesFromFormattedAlt('360d0.00')
    dailyRotation = abs(earthDegrees - earthRotation / earthClock * earthDegrees)
    leapProgression = leapYears * dailyRotation
    print('total/leap progression', formatAlt(leapProgression))

    newGhaghaAries = ghaAries + cumulativeProgression + leapProgression
    print('newGHA', formatAlt(newGhaghaAries))

    # get dateAndTime - refDateAndTime in seconds
    delta = (dateAndTime-datetime.datetime.strptime(str(dateAndTime.year), '%Y')).total_seconds()
    print('delta', delta)
    # rotation = earthRotation / delta * degreesFromFormattedAlt('360d0.00')
    rotation = delta / 86164.1 * degreesFromFormattedAlt('360d0.00')
    print('rotation', formatAndNormalizeAlt(rotation))

    totalGHA = newGhaghaAries + rotation
    print('final gha of aries', formatAlt(totalGHA))

    # star's GHA
    ghaStar = totalGHA + degreesFromFormattedAlt(sha)
    ghaStar = formatAlt(ghaStar)

    output['lat'] = lat
    output['long'] = ghaStar

    return output

def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False

def numOfLeapYears(year1, year2):
    num = 0
    for year in range(year1, year2):
        if isLeapYear(year):
            num = num + 1
    return num

def degreesFromFormattedAlt(f):
    degreesAndMinutes = f.split('d')
    degrees = int(degreesAndMinutes[0])
    # print('degrees', degrees)
    minutesStr = degreesAndMinutes[1]
    minutes = float(minutesStr)
    # if degrees <= 0:
    #     return degrees - arcminToDegrees(minutes)
    return  degrees + arcminToDegrees(minutes)


def formatAlt(alt):
    print(alt)
    print(math.floor(alt))
    degrees = math.floor(alt)
    if alt < 0:
        degrees = math.ceil(alt)
    print('fa', degrees)
    arcmin = abs(round(degreesToArcmin(alt - degrees), 1))
    return '%dd%.1f' % (degrees, arcmin)

def formatAndNormalizeAlt(alt):
    degrees = math.floor(alt)
    if alt < 0:
        degrees = math.ceil(alt)
    normalizedDegrees = degrees % 360
    print('fa', degrees)
    arcmin = abs(round(degreesToArcmin(alt - degrees), 1))
    return '%dd%.1f' % (normalizedDegrees, arcmin)

def calcAltitude(totalDegrees, dip, refraction):
    return totalDegrees + dip + refraction

def calcDip(height):
    return (-0.97 * math.sqrt(height)) / 60.0

def calcRefraction(pressure, tempC, tangent):
    return (-0.00452*pressure) / ((273+tempC) * tangent)

def convertToCelcius(f):
    return (f - 32) * 5.0/9.0

def arcminToDegrees(min):
    return min / 60.0

def degreesToArcmin(degrees):
    return degrees * 60.0



def correct(values):
    return values

def locate(values):
    return values

input = {
            'op': 'predict',
            'body': 'Betelgeuse',
            'date': '2016-01-17',
            'time': '03:15:42'
        }

print(predict(input))
