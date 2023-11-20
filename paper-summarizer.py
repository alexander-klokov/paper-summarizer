#!/usr/bin/env python3
import sys
import os

from src.summarize_pdf import summarize_pdf

def main():
    # get the path to the input pdf
    path_to_pdf = sys.argv[1]

    # make the output file name
    file_name = os.path.splitext(path_to_pdf)[0]
    path_to_summary = file_name + '.summary.txt'

    # summarize pdf
    summary = summarize_pdf(path_to_pdf)

    print(summary)

    # write the summary to a file
    with open(path_to_summary, 'w') as f:
        f.write(summary)

    print("Done!")

if __name__ == '__main__':
    main()

