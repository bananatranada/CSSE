# %3D = '=' - separates key and its value (must be exactly 1)
# %20 = ' ' - can have 0 or more anywhere (just ignore)
# %2C = ',' - separates key-value pairs (must be exactly 1)
# keys and values can't have spaces within them (%20)
import urllib
import urlparse
import re

# 1. convert escaped characters to their actual characters (urllib.unquote)
# 2. replace , to &
# 3. urlparse.parse_qs
# 4. create empty dictionary and add values as you check
# strip keys and values!
# regex on keys and values to make sure they're in the proper format

def isValidKey(key):
    # regex: whitelist
    # no spaces in between
    # must begin with a letter followed by letters or numbers
    # key = key.strip()
    # pattern = '[a-zA-Z_]([a-zA-Z0-9_])*'
    pattern = '^[a-zA-Z][a-zA-Z0-9_\.]*$'
    match = re.match(pattern, key.strip())
    if not match:
        print('invalid key')
    return match

print('is valid', isValidKey('a90'))

def isValidValue(val):
    # regex: whitelist
    # no spaces in between
    # must be letters or numbers
    # val = val.strip()
    # pattern = re.compile('^[a-zA-Z0-9_]*$')
    pattern = '^[a-zA-Z0-9_\.]+$'
    match = re.match(pattern, val.strip())
    if not match:
        print('invalid value')
    return match
    # return pattern.match(val.strip()).lastindex

def isValidQueryString(qs):
    # querystring can only contain & = or space
    pattern = '^[a-zA-Z0-9\.&= ]+$'
    match = re.match(pattern, qs)
    if not match:
        print('invalid qs')
    return match

def convertString2Dictionary(inputString = ""):
    errorDict = {'error':'true'}

    qs = urllib.unquote(inputString).replace(',', '&')

    if not isValidQueryString(qs):
        print('invalid querystring')
        return errorDict

    print('qs; ', qs)
    # transform querystring into a dictionary
    try:
        qsDict = urlparse.parse_qs(qs, strict_parsing=1) # this can fail parsing
        print('passed parse_qs; ', qsDict)
    except ValueError:
        print('cant parse_qs')
        return errorDict

    if len(qsDict) == 0:
        return errorDict

    print('dictionary', qsDict)

    result = {}
    for key, val in qsDict.iteritems():
        if len(val) != 1:
            return errorDict
        key = key.strip()
        val = val[0].strip()
        if key in result or not isValidKey(key) or not isValidValue(val):
            print('dupe key, invalid key or value')
            return errorDict
        result[key] = val

    return result

# print(urlparse.parse_qs('key', strict_parsing=1))

# inputString =  'function%3D%20calculatePosition%2C%20sighting%3DBetelgeuse'
# inputString =  'abc%3D123'
# inputString =  'function%20%3D%20get_stars'

# inputString =  'key%3Dvalue%2C%20key%3Dvalue'
inputString = 'key%3D'
# inputString = 'value'
# inputString =  '1key%3Dvalue'
# inputString =  'k%20e%20y%20%3D%20value'
# inputString = ''
# inputString =  'key1%3Dvalue%3B%20key2%3Dvalue'
result = convertString2Dictionary(inputString)
print('result', result)
