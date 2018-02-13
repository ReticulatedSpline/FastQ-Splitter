# Creative Commons - Ben Carpenter 2018
# Split fastQ files into respective forward and reverse files
# requires a .fastq file in the same directory as code. Run with `python fastq_split.py`.

with open("./input.fastq", "r") as infile:
    i = 0
    chunk = []
    print("Beginning processing...")
    # Run through the file opened on line 7 line by line.
    for line in infile:
        if i != 3:
            chunk.append(line)
            i += 1
        # Check the first line of the chunk, second to last character (last character is newline)
        elif chunk[0][-2: -1] == "1":
            chunk.append(line)
            print("forward: "),
            print(chunk[0])
            with open("./forward.fastq", "a+") as forward:
                for cline in chunk:
                    forward.write(cline)
            chunk = []
            i = 0
        elif str(chunk[0][-2: -1]) == "2":
            chunk.append(line)
            print("reverse: "),
            print(chunk[0])
            with open("./reverse.fastq", "a+") as reverse:
                for cline in chunk:
                    reverse.write(cline)
            chunk = []
            i = 0
print("\nComplete!")
