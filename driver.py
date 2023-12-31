import sys
from markov import identify_speaker

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print(
            f"Usage: python3 {sys.argv[0]} <filenameA> <filenameB> <filenameC> <k> <hashtable-or-dict>"
        )
        sys.exit(1)

    # extract parameters from command line & convert types
    filenameA, filenameB, filenameC, k, hashtable_or_dict = sys.argv[1:]
    k = int(k)
    if hashtable_or_dict not in ("hashtable", "dict"):
        print("Final parameter must either be 'hashtable' or 'dict'")
        sys.exit(1)

    # TODO: add code here to open files & read text
    f1 = open(filenameA).read()
    f2 = open(filenameB).read()
    f3 = open(filenameC).read()

    # TODO: add code to call identify_speaker & print results
    if hashtable_or_dict == "hashtable":
        is_hash = True
    else:
        is_hash = False

    print(identify_speaker(f1, f2, f3, k, is_hash))

    # Output should resemble (values will differ based on inputs):

    # Speaker A: -2.1670591295191572
    # Speaker B: -2.2363636778055525

    # Conclusion: Speaker A is most likely
