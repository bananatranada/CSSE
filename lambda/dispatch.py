def dispatch(values=None):

    #Validate parm
    if(values == None):
        return {'error': 'parameter is missing'}
    if(not(isinstance(values,dict))):
        return {'error': 'parameter is not a dictionary'}
    if (not('op' in values)):
        values['error'] = 'no op  is specified'
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
        output['error'] = 'observation does not exist'
        return output
    degreesAndMinutes = values['observation'].split('d')
    degrees = degreesAndMinutes[0]
    minutesStr = degreesAndMinutes[1]
    minutes = float(minutesStr)
    if degrees < 0 or degrees >= 90:
        output['error'] = 'degrees must be an integer [0, 90)'
        return output
    if minutesStr[::-1].find('.') is not 1:
        output['error'] = 'minutes must be a float with a mandatory decimal [0.0, 60.0)'
        return output
    if minutes < 0.0 or minutes >= 60.0:
        output['error'] = 'minutes must be a float with a mandatory decimal [0.0, 60.0)'
        return output
    if degrees == 0 and minutes == 0.1:
        output['error'] = 'can\'t be less than 0d0.1'
        return output

    # height
    height = 0
    if 'height' in values:
        height = int(values['height'])
        if values['height'] < 0:
            output['error'] = 'height must be greater than 0'
            return output

    # temperature
    temperature = 72
    if 'temperature' in values:
        temperature = int(values['temperature'])
        if temperature < -20 or temperature > 120:
            output['error'] = 'temperature must be within range [-20, 120]'
            return output

    # pressure
    pressure = 1010
    if 'pressure' in values:
        pressure = values['pressure']
        if pressure < 100 or pressure > 1100:
            output['error'] = 'pressure must be within range [100, 1100]'
            return output

    # horizon
    horizon = 'natural'
    if 'horizon' in values:
        horizon = values['horizon'].lower()
        if horizon != 'artificial' or horizon != 'natural':
            output['error'] = 'horizon must be either artificial or natural (case-insensitive)'
            return output


    return values

def predict(values):
    return values

def correct(values):
    return values

def locate(values):
    return values
