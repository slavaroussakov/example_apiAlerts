#!/usr/bin/env python3
"""Entry point for script, should only be responsible for
gathering arguments and calling on other classes."""
import argparse
from check_factory import CheckFactory

my_parser = argparse.ArgumentParser(description='Runs checks on API')
my_parser.add_argument('-c',
                       '--currency',
                       help='The currency trading pair, or ALL',
                       action='store',
                       required=True)
my_parser.add_argument('-t',
                       '--checkType',
                       help='type of check to use',
                       action='store')

args = my_parser.parse_args()
CHECK = CheckFactory().get_check_by_parameter(args.checkType)
CHECK.execute(args)

# * CheckType paramenter usage - this for the sake of the exercise as there is only one check
# The point if this is to show how future extra checks would be handled if a "check type"
# parameter was present. CheckFactory ignores these for now.
