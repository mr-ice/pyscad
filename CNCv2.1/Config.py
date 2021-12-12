import re
from objdict import objdict

def ReadConfig(file):
    retconfig = objdict()
    with open(file, 'r') as f:
        for line in f:
            line = re.split(r'#', line)[0]
            if not re.match(r'^\s*$', line):
                line = line.strip()
                k,v = re.split(r'\s*=\s*', line)

                # Handle True/False values
                if v.lower() == 'true':
                    v = True
                if v.lower() == 'false':
                    v = False

                # Handle int/float values
                try: 
                    v = int(v)
                except ValueError:
                    try:
                        v = float(v)
                    except ValueError:
                        pass

                # everything else remains a string
                retconfig[k] = v
    return retconfig