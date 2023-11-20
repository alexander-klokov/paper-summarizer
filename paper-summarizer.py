#!/usr/bin/env python3
import sys

from src.summarize_pdf import summarize_pdf

def main():
    path_to_pdf = sys.argv[1]
    path_to_summary = sys.argv[2] if len(sys.argv) > 2 else "summary.txt"

    summary = summarize_pdf(path_to_pdf)

    with open(path_to_summary, 'w') as f:
        f.write(summary)

    print("Done!")

if __name__ == '__main__':
    main()

