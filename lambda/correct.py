import math
import datetime
import util

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

def correct(values):
    output = values.copy()

    if 'lat' not in values:
        output['error'] = 'mandatory information is missing'
        return output
    if not isinstance(output['lat'], str):
        output['error'] = 'lat is invalid'
        return output


    if not isinstance(output['long'], str):
        output['error'] = 'long is invalid'
        return output

    if 'altitude' not in values:
        output['error'] = 'mandatory information is missing'
    if not isinstance(output['altitude'], str):
        output['error'] = 'altitude is invalid'
        return output

    if 'assumedLat' not in values:
        output['error'] = 'mandatory information is missing'
    if not isinstance(output['assumedLat'], str):
        output['error'] = 'assumedLat is invalid'
        return output

    if 'assumedLong' not in values:
        output['error'] = 'mandatory information is missing'
    if not isinstance(output['assumedLong'], str):
        output['error'] = 'assumedLong is invalid'
        return output

    if 'correctedDistance' in values:
        output['error'] = 'correctedDistance already exists'

    if 'correctedAzimuth' in values:
        output['error'] = 'correctedAzimuth already exists'

    # lat
    try:
        degreesAndMinutes = values['lat'].split('d')
        degrees = int(degreesAndMinutes[0])
        # print('degrees', degrees)
        minutesStr = degreesAndMinutes[1]
        minutes = float(minutesStr)
        # print('minutes', minutes)
    except:
        output['error'] = 'lat is invalid'
        return output
    if degrees <= -90 or degrees >= 90:
        # output['error'] = 'degrees must be an integer (-90, 90)'
        output['error'] = 'lat is invalid'
        return output
    if minutesStr[::-1].find('.') is not 1:
        # output['error'] = 'minutes must be a float with a mandatory decimal [0.0, 60.0)'
        output['error'] = 'lat is invalid'
        return output
    if minutes < 0.0 or minutes >= 60.0:
        # output['error'] = 'minutes must be a float with a mandatory decimal [0.0, 60.0)'
        output['error'] = 'lat is invalid'
        return output
    if degrees == 0 and minutes == 0.1:
        # output['error'] = 'can\'t be less than 0d0.1'
        output['error'] = 'lat is invalid'
        return output
    if degrees >= 0:
        totalLatDegrees = degrees + util.arcminToDegrees(minutes)
    else:
        totalLatDegrees = degrees - util.arcminToDegrees(minutes)

    # long
    try:
        degreesAndMinutes = values['long'].split('d')
        degrees = int(degreesAndMinutes[0])
        # print('degrees', degrees)
        minutesStr = degreesAndMinutes[1]
        minutes = float(minutesStr)
        # print('minutes', minutes)
    except:
        output['error'] = 'long is invalid'
        return output
    if degrees < 0 or degrees >= 360:
        # output['error'] = 'degrees must be an integer [0, 360)'
        output['error'] = 'long is invalid'
        return output
    if minutesStr[::-1].find('.') is not 1:
        # output['error'] = 'minutes must be a float with a mandatory decimal [0.0, 60.0)'
        output['error'] = 'long is invalid'
        return output
    if minutes < 0.0 or minutes >= 60.0:
        # output['error'] = 'minutes must be a float with a mandatory decimal [0.0, 60.0)'
        output['error'] = 'long is invalid'
        return output
    if degrees == 0 and minutes == 0.1:
        # output['error'] = 'can\'t be less than 0d0.1'
        output['error'] = 'long is invalid'
        return output
    totalLongDegrees = degrees + util.arcminToDegrees(minutes)

    # altitude
    try:
        degreesAndMinutes = values['altitude'].split('d')
        degrees = int(degreesAndMinutes[0])
        # print('degrees', degrees)
        minutesStr = degreesAndMinutes[1]
        minutes = float(minutesStr)
        # print('minutes', minutes)
    except:
        output['error'] = 'altitude is invalid'
        return output
    if degrees <= 0 or degrees >= 90:
        # output['error'] = 'degrees must be an integer (0, 90)'
        output['error'] = 'altitude is invalid'
        return output
    if minutesStr[::-1].find('.') is not 1:
        # output['error'] = 'minutes must be a float with a mandatory decimal [0.0, 60.0)'
        output['error'] = 'altitude is invalid'
        return output
    if minutes < 0.0 or minutes >= 60.0:
        # output['error'] = 'minutes must be a float with a mandatory decimal [0.0, 60.0)'
        output['error'] = 'altitude is invalid'
        return output
    if degrees == 0 and minutes == 0.1:
        # output['error'] = 'can\'t be less than 0d0.1'
        output['error'] = 'altitude is invalid'
        return output
    totalAltitudeDegrees = degrees + util.arcminToDegrees(minutes)

    # assumed lat
    try:
        degreesAndMinutes = values['assumedLat'].split('d')
        degrees = int(degreesAndMinutes[0])
        # print('degrees', degrees)
        minutesStr = degreesAndMinutes[1]
        minutes = float(minutesStr)
        # print('minutes', minutes)
    except:
        output['error'] = 'assumedLat is invalid'
        return output
    if degrees <= -90 or degrees >= 90:
        # output['error'] = 'degrees must be an integer (-90, 90)'
        output['error'] = 'assumedLat is invalid'
        return output
    if minutesStr[::-1].find('.') is not 1:
        # output['error'] = 'minutes must be a float with a mandatory decimal [0.0, 60.0)'
        output['error'] = 'assumedLat is invalid'
        return output
    if minutes < 0.0 or minutes >= 60.0:
        # output['error'] = 'minutes must be a float with a mandatory decimal [0.0, 60.0)'
        output['error'] = 'assumedLat is invalid'
        return output
    if degrees == 0 and minutes == 0.1:
        # output['error'] = 'can\'t be less than 0d0.1'
        output['error'] = 'assumedLat is invalid'
        return output
    if degrees >= 0:
        totalAssumedLatDegrees = degrees + util.arcminToDegrees(minutes)
    else:
        totalAssumedLatDegrees = degrees - util.arcminToDegrees(minutes)

    # assumedLong
    try:
        degreesAndMinutes = values['assumedLong'].split('d')
        degrees = int(degreesAndMinutes[0])
        # print('degrees', degrees)
        minutesStr = degreesAndMinutes[1]
        minutes = float(minutesStr)
        # print('minutes', minutes)
    except:
        output['error'] = 'assumedLong is invalid'
        return output
    if degrees < 0 or degrees >= 360:
        # output['error'] = 'degrees must be an integer [0, 360)'
        output['error'] = 'assumedLong is invalid'
        return output
    if minutesStr[::-1].find('.') is not 1:
        # output['error'] = 'minutes must be a float with a mandatory decimal [0.0, 60.0)'
        output['error'] = 'assumedLong is invalid'
        return output
    if minutes < 0.0 or minutes >= 60.0:
        # output['error'] = 'minutes must be a float with a mandatory decimal [0.0, 60.0)'
        output['error'] = 'assumedLong is invalid'
        return output
    if degrees == 0 and minutes == 0.1:
        # output['error'] = 'can\'t be less than 0d0.1'
        output['error'] = 'assumedLong is invalid'
        return output
    totalAssumedLongDegrees = degrees + util.arcminToDegrees(minutes)

    LHA = totalLongDegrees + totalAssumedLongDegrees
    # print('LHA', util.formatAndNormalizeAlt(LHA))
    intermediateDistance = (math.sin(math.radians(totalLatDegrees)) * math.sin(math.radians(totalAssumedLatDegrees))) + (math.cos(math.radians(totalLatDegrees)) * math.cos(math.radians(totalAssumedLatDegrees)) * math.cos(math.radians(LHA)))
    # print('intermediateDistance', intermediateDistance)
    # print('sin(lat)', round(math.sin(math.radians(totalLatDegrees)), 3))
    # print('sin(assumedLat)', round(math.sin(math.radians(totalAssumedLatDegrees)), 3))
    # print('cos(lat)', round(math.cos(math.radians(totalLatDegrees)), 3))
    # print('cos(assumedLat)', round(math.cos(math.radians(totalAssumedLatDegrees)), 3))
    # print('cos(LHA)', round(math.cos(math.radians(LHA)), 3))
    correctedAltitude = math.asin(intermediateDistance)
    # print('correctedAltitude', correctedAltitude)
    correctedDistance = int(round(util.degreesToArcmin(totalAltitudeDegrees - math.degrees(correctedAltitude)), 0))
    correctedAzimuth = util.formatAndNormalizeAlt(math.degrees(math.acos((math.sin(math.radians(totalLatDegrees)) - (math.sin(math.radians(totalAssumedLatDegrees)) * intermediateDistance))/(math.cos(math.radians(totalAssumedLatDegrees)) * math.cos(math.asin(intermediateDistance))))))
    # print('sin(lat)', math.sin(math.radians(totalLatDegrees)))
    # print(math.sin(math.radians(totalAssumedLatDegrees)))
    #
    # print(correctedDistance)
    # print(correctedAzimuth)

    output['correctedDistace'] = correctedDistance
    output['correctedAzimuth'] = correctedAzimuth

    return output

# input = {'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
# input = {
#     'lat' : '89d20.1',
#     'long' :'154d5.4',
#     'altitude' :'37d17.4',
#     'assumedLat': '35d59.7',
#     'assumedLong': '74d35.3',
# }
# output = correct(input)
# print(output)
