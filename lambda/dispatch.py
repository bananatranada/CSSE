import math

def dispatch(values=None):

    #Validate parm
    if(values == None):
        return {'error': 'parameter is missing'}
    if(not(isinstance(values,dict))):
        return {'error': 'parameter is not a dictionary'}
    if (not('op' in values)):
        values['error'] = 'no op is specified'
        return values

    #Perform designated function
    if(values['op'] == 'adjust'):
        return adjust(values)
    elif(values['op'] == 'predict'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'correct'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'locate'):
        return values    #This calculation is stubbed out
    else:
        values['error'] = 'op is not a legal operation'
        return values

# TODO:
# 1. calculation
# 2. handle errors
# 3. test
def adjust(values):
    output = values.copy()

    if 'altitude' in values:
        output['error'] = 'altitude already exists in the input'
        return output

    # observation (degrees and minutes)
    if 'observation' not in values:
        output['error'] = 'mandatory information is missing'
        return output
    try:
        degreesAndMinutes = values['observation'].split('d')
        degrees = int(degreesAndMinutes[0])
        print('degrees', degrees)
        minutesStr = degreesAndMinutes[1]
        minutes = float(minutesStr)
        print('minutes', minutes)
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
    print('totalDegrees', totalDegrees)

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
            output['error'] = 'height is invalid'
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
    print('dip', dip)

    # refraction
    refraction = calcRefraction(pressure, convertToCelcius(temperature), math.tan(math.radians(totalDegrees)))
    print('refraction', refraction)
    print('temp in C', convertToCelcius(temperature))

    altitude = calcAltitude(totalDegrees, dip, refraction)
    print('altitude', altitude)
    if altitude < 0 or altitude >= 91:
        output['error'] = 'altitude is invalid'
        return output
    formattedAltitude = formatAlt(altitude)
    print('formatted altitude', formattedAltitude)
    # TODO: check if altitude is within valid ranges


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

def degreesToRadians(degrees):
    return degrees * 180.0

def radiansToDegrees(radians):
    return radians / 180.0

def predict(values):
    return values

def correct(values):
    return values

def locate(values):
    return values

input = {
    'observation': '30d1.5',
    'height': '19',
    'pressure': '1000',
    'horizon': 'artificial',
    'op': 'adjust',
    'temperature': '85'
}
# input = {
#     'observation': '42d0.0',
#     'op': 'adjust',
# }
output = dispatch(input)
print(output)
