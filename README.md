DNA is a sequence of molecules called nucleotides, arranged into a particular shape (a double helix). Every human cell has billions of nucleotides arranged in sequence. Each nucleotide of DNA contains one of four different bases: adenine (A), cytosine (C), guanine (G), or thymine (T).

One place where DNA tends to have high genetic diversity is in Short Tandem Repeats (STRs). An STR is a short sequence of DNA bases that tends to repeat consecutively numerous times at specific locations inside of a person’s DNA. The number of times any particular STR repeats varies a lot among individuals.

If the probability that two people have the same number of repeats for a single STR is 5%, and the analyst looks at 10 different STRs, then the probability that two DNA samples match purely by chance is about 1 in 1 quadrillion.

In the csv files, each row corresponds to the STR count of a person, for example, the longest sequence of AGATC for Albus in large.csv is 15.

In order to run, command-line-arguments are required: 
- python dna.py database/name.csv sequences/number.txt
- where name and number are the names of the files in each respective directory

Some sequences do not have matches. For example if you ran
- python dna.py database/large.csv sequences/5.txt would output Lavender.
But if you ran 
- python dna.py database/large.csv sequences/13.txt would output No match found