import sys

import pythonwhois

whois = pythonwhois.get_whois(sys.argv[1])
for key in whois.keys():
    print("%s :%s \n" % (key, whois[key]))
