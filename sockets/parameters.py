#import argparse

#parser = argparse.ArgumentParser(description='params port scan')
#parser.add_argument("-t", dest="target", help="target", required=True)

#parser.add_argument("-p", "--port", dest="port", type=int, default=80,help="port to scan. Default: 80.")

#parser.add_argument('-v', dest='verbosity', help='verbosity level', type=int, default=0)

#parser.add_argument("--open", dest="only_open", action="store_true",
#    help="only display open ports", default=False)


#params = parser.parse_args()

#print("Target :",params.target)
#print("Port %:",params.port)
#print("Verbosity :",params.verbosity)
#print("Only open :",params.only_open)

import argparse

description = """ Examples of use:
        + Basic scan:
             -target 127.0.0.1
        + Indicate a specific port:
             -target 127.0.0.1 -port 21
        + Only show open ports
             -target 127.0.0.1 --open True """
parser = argparse.ArgumentParser(description='Port scanning', epilog=description,                     formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-target", metavar='TARGET', dest="target", help="target to scan",required=True)
parser.add_argument("-p", "--port", dest="port",
type=int,help="port to scan. Defaul: 80.", default=80)
parser.add_argument("-ports", dest="ports", help="Please, specify the target port(s) separated by comma[80,8080 by default]",default = "80,8080")
parser.add_argument('-v', dest='verbosity', default=0, action="count",help="verbosity level: -v, -vv, -vvv.")
parser.add_argument("--open", dest="only_open", action="store_true",help="only display open ports", default=False)
params = parser.parse_args()
