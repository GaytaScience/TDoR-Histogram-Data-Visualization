The `2017` data folder contains parsing scripts and data from the Transgender Europe (TGEU) original reports, while the folders for the more recent years contain data pulled from https://tdor.translivesmatter.info/. The `All` folder contains initial code for processing all data for a comprehensive data visualization.

`2017` files include:
* **TvT_TMM_TDoR2017_Namelist_EN:** Original report downloaded from [TGEU](http://transrespect.org/en/trans-murder-monitoring/tmm-resources/)
* **output.txt:** PDFMiner was used to convert the .pdf file to a .txt file using ```pdf2txt.py -o output.txt TvT_TMM_TDoR2017_Namelist_EN.pdf``` on the command line.
* **parse.py:** A python script was then used to read in the file line by line, saving desired information in a .csv datatable. 
* **parsed.csv:** Original datafile output from parse.py
* **parsed_enc.csv:** Datafile used for visualization. Includes some manual cleaning and html replacements for unicode letters and symbols

`2018`+ files include:
* **Cleaned CSV:** Datafile used for visualization. Originally downloaded from https://tdor.translivesmatter.info/, this file includes some manual cleaning/enhancements as well as html replacements for unicode letters.
* **TvT_TMM Report: (optional)** TGEU report for cross referencing, if desired.

`All` files include:
* **All_Exploration.ipynb:** Jupyter notebook exploring data export through 2020 from https://tdor.translivesmatter.info/. The notebook merges on manual remarks from Gayta Science's yearly TDoR visualizations, does some light cleaning, and exports a full .csv file.
* **All_Enhanced.csv:** An enhanced version of the exported .csv file from All_Exploration.ipynb.
* **ImgProcessing.py:** A simple script that ingests all photos downloaded from https://tdor.translivesmatter.info/, scales them, and turns them black and white. 

There is also a `test` folder containing 2016 test data parsed from TGEU original reports. 
