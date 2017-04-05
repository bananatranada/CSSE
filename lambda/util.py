import math

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
    degreesStr = degreesAndMinutes[0]
    degrees = int(degreesStr)
    # print('degrees', degrees)
    minutesStr = degreesAndMinutes[1]
    minutes = float(minutesStr)
    if degreesStr[0] == '-':
        return -1 * (abs(degrees) + arcminToDegrees(minutes))
    return degrees + arcminToDegrees(minutes)


def formatAlt(alt):
    degrees = math.floor(alt)
    if alt < 0:
        degrees = math.ceil(alt)
    arcmin = abs(round(degreesToArcmin(alt - degrees), 1))
    return '%dd%.1f' % (degrees, arcmin)

def formatAndNormalizeAlt(alt):
    degrees = math.floor(alt)
    if alt < 0:
        degrees = math.ceil(alt)
    normalizedDegrees = degrees % 360
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
