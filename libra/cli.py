#!/usr/bin/python

import argparse

libra_str = """
  _      _   _                 
 | |    (_) | |__   _ _   __ _ 
 | |__  | | | '_ \ | '_| / _` |
 |____| |_| |_.__/ |_|   \__,_|                               
            An superawesome Python load balancer.
"""


class Colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def print_libra_msg():
    print(f"{Colors.OKBLUE}{libra_str}{Colors.ENDC}")


parser = argparse.ArgumentParser(
    description=print_libra_msg())

parser.add_argument("-v", "--version",
                    help="Shows Libra version", action="store_true")
parser.add_argument("-s", "--start", help="Start Libra", action="store_true")
parser.add_argument(
    "-d", "--detach", help="Start Libra in detach mode", action="store_true")
parser.add_argument("-c", "--cleanup",
                    help="Clean up workers", action="store_true")

parser.parse_args()
