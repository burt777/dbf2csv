#!/usr/bin/env python3
import sys
import csv
import logging
from dbfread import DBF
import argparse

def dbf2csv():
    ''' Convert a FoxPro DBF file to CSV, either stdOut or output file  '''

    parser = argparse.ArgumentParser(description = dbf2csv.__doc__)

    parser.add_argument (
            '-i', '--input-file',
            nargs = '?', 
            dest = "inputFile", 
            type = argparse.FileType('r'), 
            help = "Input file (.dbf)",
            default = False,
    )

    parser.add_argument(
            '-o', '--output-file', 
            action = "store", 
            nargs = '?',
            dest = 'outputFile', 
            type = argparse.FileType('w'), 
            default = False,
            help = "Output file (.csv), default: stdOut"
    )

    # Get all arguments
    args = parser.parse_args()

    # Check if inputFile was given:
    if args.inputFile == False:
        parser.print_help()
        sys.exit(1)

    # Use stdOut if no output file was given:
    if args.outputFile == False:
        outFileHandle = sys.stdout
    elif args.outputFile is None:
        print ("Error: no output file. Specify output file like this: ")
        print ("\t -o table.csv")
        sys.exit(1)
    else:
        outFileHandle = open(args.outputFile.name, 'w', newline='')
    
    reader = DBF(args.inputFile.name, ignore_missing_memofile = True)
    
    rowNr = 0
    for row in reader:
        if rowNr < 1:
            writer = csv.DictWriter(outFileHandle, row.keys())
            writer.writeheader()
        writer.writerow(row)
        rowNr += 1

if __name__ == "__main__":
    dbf2csv()