# dbf2csv
Command line Python tool to convert FoxPro DBF database files to .csv files.

USAGE: 
-i inputfile
-o outputfile (if omitted use stdout) 
-e input encoding
Output encoding is always utf-8

To make an exe file using py2exe, use compile.py. The exe will need the C++ runtime libraries MSVCR100.DLL.
https://www.microsoft.com/en-us/download/details.aspx?id=5555
