The 2017 data folder contains parsing scripts and data from the TGEU original reports, while 2018 contains files pulled from https://tdor.translivesmatter.info/

2017 files include:
* **TvT_TMM_TDoR2017_Namelist_EN:** Original report downloaded from http://transrespect.org/en/trans-murder-monitoring/tmm-resources/
* **output.txt:** PDFMiner was used to convert the .pdf file to a .txt file using ```pdf2txt.py -o output.txt TvT_TMM_TDoR2017_Namelist_EN.pdf``` on the command line.
* **parse.py:** A python script was then used to read in the file line by line, saving desired information in a .csv datatable. 
* **parsed.csv:** Original datafile output from parse.py
* **parsed_enc.csv:** Datafile used for visualization. Includes some manual cleaning and html replacements for unicode letters and symbols

2018+ files include:
* **Cleaned CSV:** Datafile used for visualization. Originally downloaded from https://tdor.translivesmatter.info/, this file includes some manual cleaning/enhancements as well as html replacements for unicode letters.
* **TvT_TMM Report: (optional)** TGEU report for cross referencing, if desired.

There is also a test folder containing 2016 test data parsed from TGEU original reports. 
