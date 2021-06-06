import argparse
from sys import argv
# Initialize parser
msg = "dileep"
parser = argparse.ArgumentParser(description=msg)
parser.parse_args()

print(type(argv))