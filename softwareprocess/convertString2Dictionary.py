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
    # no spaces in between
    # must begin with a letter followed by letters or numbers or .
    pattern = '^[a-zA-Z][a-zA-Z0-9\.]*$'
    return re.match(pattern, key.strip())

def isValidValue(val):
    # no spaces in between
    # must be letters or numbers or .
    pattern = '^[a-zA-Z0-9\.]+$'
    return re.match(pattern, val.strip())

def isValidQueryString(qs):
    # querystring can only contain & = . or space
    pattern = '^[a-zA-Z0-9\.&= ]+$'
    return re.match(pattern, qs)

def convertString2Dictionary(inputString = ""):
    errorDict = {'error':'true'}

    qs = urllib.unquote(inputString).replace(',', '&')

    if not isValidQueryString(qs):
        return errorDict

    # transform querystring into a dictionary
    try:
        qsDict = urlparse.parse_qs(qs, strict_parsing=1) # this can fail parsing
    except ValueError:
        return errorDict

    if len(qsDict) == 0:
        return errorDict

    result = {}
    for key, val in qsDict.iteritems():
        if len(val) != 1:
            return errorDict
        key = key.strip()
        val = val[0].strip()
        if key in result or not isValidKey(key) or not isValidValue(val):
            return errorDict
        result[key] = val

    return result
