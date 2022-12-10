import re

def format_name(name):  #do one thing, use a small number of arguments
    retstr = re.sub(r'\t', ' ', name)
    retstr = re.sub(r' +', ' ', retstr)
    retstr = retstr.strip()
    retstr = retstr.upper()
    return retstr

def format_city_name(name):  
    retstr = re.sub(r'[^\P{P}\-]+', '', name)
    retstr = format_name(retstr) # DRY - Don't repeat yourself
    return retstr

def format_address_name(name):
    retstr = re.sub(r'[^\P{P}\-&]+', '', name)
    retstr = format_name(retstr)
    return retstr