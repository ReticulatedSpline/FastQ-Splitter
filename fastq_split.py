# Creative Commons License - Ben Carpenter | 2018 | carpe504@d.umn.edu
# Split fastQ files into respective forward and reverse files
# requires a .fastq file in the same directory as code. Run with `python fastq_split.py`.

import os.path as path
import sys

input_path = ""
output_path = ""
consent = "N"
linecount = 0
curline = 0

def print_progress(current_count, total_count, stage):
    hashes = 70.0 * (float(current_count) / float(total_count))
    whitespace = 70 - hashes
    # clear the command line
    print("\033[H\033[J")
    # print the progress bar
    print "\r" + stage
    print ("\r[" + "#" * int(hashes) + " " * int(whitespace) + "]" )

print("|-- Fastq splitter by Ben Jamin'. Press enter to use default values. --|")
input_path = raw_input("Enter source fastq file name: ")
if not input_path:
    input_path = path.realpath("./input.fastq")
    print (input_path.replace(" ", "\ "))

output_path = raw_input("Enter destination folder: ")
if not output_path:
    output_path = path.realpath("./")
    print (output_path.replace(" ", "\ "))

consent = raw_input("Proceed? [Y/n] : ")

if consent.upper() == "Y":
    stage = "Counting lines..."
    with open(input_path, "r") as file:
        for newline in file:
            linecount += 1
        print("Lines: " + str(linecount))
    
    with open(input_path, "r") as infile:
        i = 0
        chunk = []

        # Run through the file opened on line 7 line by line.
        for line in infile:
            stage = "Splitting chunks..."
            curline += 1
            if i != 3:
                chunk.append(line)
                i += 1
            # Check the first line of the chunk, second to last character (last character is newline)
            elif chunk[0][-2: -1] == "1":
                print_progress(curline, linecount, stage)
                chunk.append(line)
                with open(output_path + "forward.fastq", "a+") as forward:
                    for cline in chunk:
                        forward.write(cline)
                chunk = []
                i = 0
            # Repeat for the reverse "2" direction
            elif str(chunk[0][-2: -1]) == "2":
                chunk.append(line)
                with open(output_path + "reverse.fastq", "a+") as reverse:
                    for cline in chunk:
                        reverse.write(cline)
                chunk = []
                i = 0
    # yay
    stage = "Complete!"
    print_progress(curline, linecount, stage)
    print "Results written to " + output_path.replace(" ", "\ ")
    sys.exit(0)
else:
    print("Exiting...")
    sys.exit(0)
