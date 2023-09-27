import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) == 3:
        database_dir = sys.argv[1]
        sequence_dir = sys.argv[2]
    else:
        print("Please, check for the command line argument, For example:")
        print('"dna.py databases/large.csv sequences/5.txt"')
        return 3

    # TODO: Read database file into a variable
    file = open(database_dir, "r")
    database = csv.DictReader(file)
    headers = database.fieldnames

    # TODO: Read DNA sequence file into a variable
    with open(sequence_dir, "r") as f:
        sequence = f.readlines()
        sequence = sequence[0]

    # TODO: Find longest match of each STR in DNA sequence
    matchs = []
    for subsequence in headers[1:]:
        #print(subsequence)
        matchs.append(longest_match(sequence, subsequence))

    # TODO: Check database for matching profiles

    for row in database:
        temp_row = []
        #print(row["name"])
        for h in headers[1:]:
            temp_row.append(int(row[h]))
        if temp_row == matchs:
            print(row["name"])
            return 1

    print("Not Match")
    file.close()
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
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
