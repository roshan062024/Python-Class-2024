#!/usr/bin/python
"""
Purpose: Reading(Parsing) csv, using unstructure file ops
# Method 1
with open("my_file.csv", mode="r") as fh:
    file_content = fh.read()
    # print(file_content)

names = []
for line in file_content.splitlines()[1:]: #  .split('\n'):
    if line:
        names.append(line.split(',')[1])

print(f"{names =}")


# Assignment : try with fh.readlines(), instead of fh.read()
# Assignment: try with fh.readline(), with a yield to create like a generator
"""

# Using fh.readlines()
with open("my_file.csv", mode="r") as fh:
    lines = fh.readlines()

names = []
for line in lines[1:]:
    if line.strip():  # Ensure line is not empty or just whitespace
        names.append(line.strip().split(',')[1])

print(f"{names =}")


# Using fh.readline() with a generator
def read_names(filename):
    with open(filename, mode="r") as fh:
        fh.readline() 
        line = fh.readline()
        while line:
            if line.strip():
                yield line.strip().split(',')[1]
            line = fh.readline()

names_gen = read_names("my_file.csv")

for name in names_gen:
    print(name)
