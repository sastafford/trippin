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
  
def zip(instr:str, digit=5):
  if instr is None or instr == '' or (digits != 5 and digits != 9):
            return instr

        cleanzip = self.cleanaddrstr(instr, 'ZIP')
        if cleanzip == '':
            return cleanzip

        fields = cleanzip.split('-')
        if len(fields) == 2:
            if digits == 5:
                return fields[0].rjust(5, '0')
            else:
                return fields[0].rjust(5, '0') + '-' + fields[1].rjust(4, '0')
        elif len(fields) == 1:
            if len(fields[0]) <= 5:
                if digits == 5:
                    return fields[0].rjust(5, '0')
                else:
                    return fields[0].rjust(5, '0') + '-0000'
            elif len(fields[0]) == 9:
                if digits == 5:
                    return fields[0][:5]
                else:
                    return fields[0][:5] + '-' + fields[0][5:]
