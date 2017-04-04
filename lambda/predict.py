import math
import datetime

stars = {
    'Alpheratz': '357d41.7,29d10.9',
    'Ankaa': '353d14.1,-42d13.4',
    'Schedar': '349d38.4,56d37.7',
    'Diphda':'348d54.1,-17d54.1',
    'Achernar':	'335d25.5,-57d09.7',
    'Hamal': '327d58.7,23d32.3',
    'Polaris':'316d41.3,89d20.1'
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
    'Markab'	:'13d36.7,15d17.6',

}

def predict(values):
    output = values.copy()

    # if 'altitude' in values:
    #     output['error'] = 'altitude already exists in the input'
    #     return output

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
            time = values['date'].split(':')

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


    try:
        degreesAndMinutes = values['observation'].split('d')
        degrees = int(degreesAndMinutes[0])
        # print('degrees', degrees)
        minutesStr = degreesAndMinutes[1]
        minutes = float(minutesStr)
        # print('minutes', minutes)
    except:
        output['error'] = 'observation is invalid'
        return output
    if degrees < 0 or degrees >= 90:
        # output['error'] = 'degrees must be an integer [0, 90)'
        output['error'] = 'observation is invalid'
        return output
    if minutesStr[::-1].find('.') is not 1:
        # output['error'] = 'minutes must be a float with a mandatory decimal [0.0, 60.0)'
        output['error'] = 'observation is invalid'
        return output
    if minutes < 0.0 or minutes >= 60.0:
        # output['error'] = 'minutes must be a float with a mandatory decimal [0.0, 60.0)'
        output['error'] = 'observation is invalid'
        return output
    if degrees == 0 and minutes == 0.1:
        # output['error'] = 'can\'t be less than 0d0.1'
        output['error'] = 'observation is invalid'
        return output
    totalDegrees = degrees + arcminToDegrees(minutes)
    # print('totalDegrees', totalDegrees)

    # height (numeric? int or float accepted?)
    height = 0
    if 'height' in values:
        try:
            height = float(values['height'])
        except ValueError:
            output['error'] = 'height is invalid'
            return output
        if values['height'] < 0:
            # output['error'] = 'height must be greater than 0'
            output['error'] = 'height must be greater than 0'
            return output

    # temperature (int)
    temperature = 72
    if 'temperature' in values:
        try:
            temperature = int(values['temperature'])
        except ValueError:
            output['error'] = 'temperature is invalid'
            return output
        if temperature < -20 or temperature > 120:
            # output['error'] = 'temperature must be within range [-20, 120]'
            output['error'] = 'temperature is invalid'
            return output

    # pressure (int)
    pressure = 1010
    if 'pressure' in values:
        try:
            pressure = int(values['pressure'])
        except ValueError:
            output['error'] = 'pressure is invalid'
            return output
        if pressure < 100 or pressure > 1100:
            # output['error'] = 'pressure must be within range [100, 1100]'
            output['error'] = 'pressure is invalid'
            return output

    # horizon (string)
    horizon = 'natural'
    if 'horizon' in values:
        try:
            horizon = values['horizon'].lower()
        except AttributeError:
            output['error'] = 'horizon is invalid'
            return output
        if horizon != 'artificial' and horizon != 'natural':
            # output['error'] = 'horizon must be either artificial or natural (case-insensitive)'
            output['error'] = 'horizon is invalid'
            return output

    # dip
    dip = 0
    if horizon == 'natural':
        dip = calcDip(height)
    # print('dip', dip)

    # refraction
    refraction = calcRefraction(pressure, convertToCelcius(temperature), math.tan(math.radians(totalDegrees)))
    # print('refraction', refraction)
    # print('temp in C', convertToCelcius(temperature))

    altitude = calcAltitude(totalDegrees, dip, refraction)
    # print('altitude', altitude)
    # check to see if altitude is within valid range
    if altitude < 0 or altitude >= 91:
        output['error'] = 'altitude is invalid'
        return output
    formattedAltitude = formatAlt(altitude)
    # print('formatted altitude', formattedAltitude)

    output['altitude'] = formattedAltitude

    return output

def formatAlt(alt):
    degrees = math.floor(alt)
    arcmin = round(degreesToArcmin(alt - degrees), 1)
    return '%dd%.1f' % (degrees, arcmin)

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

def predict(values):
    return values

def correct(values):
    return values

def locate(values):
    return values
