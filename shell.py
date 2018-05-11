#!/usr/bin/python
""" Command line shell interface. Usage python shell.py  -h """
__author__ = "Jeyson Molina"
__email__ = "jjmc82@gmail.com"
__version__ = "1.0"

import argparse as ap

from ir_webstats.client import iRWebStats
from ir_webstats.util import *

if __name__ == '__main__':

    parser = ap.ArgumentParser(description="Shell interface for iRWebStats")
    parser.add_argument("-u", "--user", help='iRacing user', required=False)
    parser.add_argument("-p", "--passw", help='iRacing password',required=False)
    parser.add_argument("-m", "--method", help='Function to execute',required=False)
    parser.add_argument("-l", "--list", help='List of available functions to execute',required=False, action='store_true')
    parser.add_argument("-a", "--args", help='Named function arguments separated by semicolon ("p1=1;p2=2;...;p5=\'String\'")',required=False)
    args = parser.parse_args()

    irw = iRWebStats()


    if args.list:
        l = inspect.getmembers(iRWebStats)
        o = '\n'.join(["%s: %s"%(f[0], inspect.getdoc(f[1])) for f in l[3:]])
        print(o)

    elif args.method:
        f = args.method
        if hasattr(iRWebStats, f):
            func = getattr(irw, f)
            a = inspect.getargspec(func)
            if args.args or len(a.args) == 1:
                #extract args
                try:
                    if args.args:
                        exec("res={'" + args.args.replace("=", "':").replace(";", ",'") + "}")
                    else:
                        res = {}

                    if args.user and args.passw:
                        irw.login(username=args.user, password=args.passw)
                    else:
                        irw.login() #No login provided, maybe there's a valid cookie
                    r = func(**res) #execute
                    print(json.dumps(r)) #Output result using json format
                except Exception as e:
                    print("Error: ", e)

            else: #Print args
                pprint ("%s : %s"%(f, inspect.getdoc(func)))
                print("\n")
                print("Parameters: ")
                for ind, i in enumerate(a.args):
                    if i not in ('self',):
                        df = ''
                        if a.defaults is not None and len(a.defaults) >= ind:
                            df = "(default: %s)"%(str(a.defaults[ind-1]))
                        print("%s %s"%(i, df))

        else:
            print("Error: %s is not a member of iRWebstat")
