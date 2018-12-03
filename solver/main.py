import sys


def clean_line(line):
    return line.strip('\n').split(':')

FILENAME = sys.argv[1]
F = open(FILENAME, "r")
covered_files = []

for line in F.readlines():
    if line.startswith('SF'):
        key, value = clean_line(line)
        covered_files.append(value)

print(covered_files)