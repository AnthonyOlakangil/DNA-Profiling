import csv
import sys


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py file.csv file.txt")
        sys.exit(1)

    # Read database file into a variable
    with open(sys.argv[1], "r") as db_file:
        database = csv.reader(db_file)
        # skip the header
        db_header = next(database)

        # Read DNA sequence file into a variable
        with open(sys.argv[2], "r") as seq_file:
            sequence = seq_file.read()

        # Find longest match of each STR in DNA sequence
        AGATC_count = longest_match(sequence, "AGATC")
        TTTTTTCT_count = longest_match(sequence, "TTTTTTCT")
        AATG_count = longest_match(sequence, "AATG")
        TCTAG_count = longest_match(sequence, "TCTAG")
        TATC_count = longest_match(sequence, "TATC")
        GATA_count = longest_match(sequence, "GATA")
        GAAA_count = longest_match(sequence, "GAAA")
        TCTG_count = longest_match(sequence, "TCTG")
        # Check database for matching profiles
        found = False
        if sys.argv[1] == "databases/small.csv":
            for row in database:
                db_counts = [int(row[1]), int(row[2]), int(row[3])]

                # Compare counts
                if all(
                    db_count == dna_count
                    for db_count, dna_count in zip(
                        db_counts, [AGATC_count, AATG_count, TATC_count]
                    )
                ):
                    found = True
                    print("\nMatch found:", row[0],"\n")
                    break
            if not found:
                print("\nNo match found\n")
            return 0
        else:  # If using large.csv
            found = False
            for row in database:
                db_counts = [int(count) for count in row[1:]]
                dna_counts = [
                    AGATC_count,
                    TTTTTTCT_count,
                    AATG_count,
                    TCTAG_count,
                    GATA_count,
                    TATC_count,
                    GAAA_count,
                    TCTG_count
                    ]
                # Compare all counts in db vs sequence provided until a match is found
                if all(
                    db_count == dna_count
                    for db_count, dna_count in zip(db_counts, dna_counts)
                ):
                    found = True
                    print("\nMatch found:", row[0], "\n")
                    break
            if not found:
                print("\nNo match found\n")


def longest_match(sequence, subsequence):
    # Returns length of longest run of subsequence in sequence.

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, check next substring for subsequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
