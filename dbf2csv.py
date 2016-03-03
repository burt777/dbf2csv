#!/usr/bin/env python3
import sys
import csv
import logging
from dbfread import DBF
import argparse
import codecs


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

    parser.add_argument(
            '-e', '--encoding', 
            action = "store",
            nargs = '?',
            dest = 'encodingIn',
            type = str,
            default = 'cp1252',
            help = "Encoding of input file, default: cp1252, try latin5 for Turkish, cp1250 for Polish, or utf_8 if you're really hip"
    )

    # Get all arguments
    args = parser.parse_args()

    # Check if inputFile was given:
    if args.inputFile == False:
        parser.print_help()
        sys.exit(1)

    # Input:
    reader = DBF(args.inputFile.name, encoding = args.encodingIn,  ignore_missing_memofile = True)

    # Output: use stdOut if no output file was given:
    if args.outputFile == False:
        sys.stdout = codecs.getwriter('utf8')(sys.stdout)
        outFileHandle = sys.stdout
    elif args.outputFile is None:
        print ("Error: no output file. Specify output file like this: ")
        print ("\t -o table.csv")
        sys.exit(1)
    else:
        outFileHandle = open(args.outputFile.name, 'w', newline='', encoding = 'UTF-8') #, encoding = args.encoding)
    
    # Go go go:
    for nr, row in enumerate(reader):
        if nr == 0:
            writer = csv.DictWriter(outFileHandle, row.keys())
            writer.writeheader()
        writer.writerow(row)

if __name__ == "__main__":
    dbf2csv()