import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo', help='foo help')
args = parser.parse_args()
# This will add the '--foo' command line option to the script

# Fun Facts

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('integers', metavar='N', type=int, nargs='+')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
args = parser.parse_args()
# This will add the 'N' positional command line option to the script, and the '--sum' optional command line option