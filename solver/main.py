import sys
import pprint

def clean_line(line):
    return line.strip('\n').split(':')

FILENAME = sys.argv[1]
F = open(FILENAME, "r")
covered_files = []

filename = ''
covered_lines = {}
for line in F.readlines():
    if line.startswith('SF'):
        key, filename = clean_line(line)
    if line.startswith('DA'):
        key, coverage = clean_line(line)
        line, hits = coverage.split(',')
        covered_lines[line] = hits
    if line == 'end_of_record\n':
        covered_files.append({
            "filename": filename,
            "covered_lines": covered_lines
        })
        covered_lines = {}

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(covered_files)
print('{} files covered'.format(len(covered_files)))
# print(covered_files)
