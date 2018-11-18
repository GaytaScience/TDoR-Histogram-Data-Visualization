## TDoR Histogram Data Visualization
Data Visualization for Transgender Day of Remembrance (TDoR) 11/20 

### Data Folder
[Trans Respect vs Transphobia Worldwide](http://transrespect.org) publishes [reports for TDoR](http://transrespect.org/en/trans-murder-monitoring/tmm-resources/) every year. One of the reports is a Name List, which lists available information for every reported murder of a trans or gender-diverse person in the last year. 

In 2018, [Anna-Jayne Metcalfe](https://twitter.com/annajayne) sought out to [learn more about all those we have lost](https://medium.com/@annajayne/tdor-learning-more-about-those-we-have-lost-8043146f402c). The new https://tdor.translivesmatter.info/ website combines, gathers, and disseminates details about each victim’s life and death in a way that has not been available before, allowing the community to better connect with and celebrate them.

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

### Visualization
The file dotbar.html contains the code for the d3.v4.js visualization. 

### Branches
Master branch development uses dots or circles to represent each victim. The candles branch replaces these with a candle icon. The candle version was ultimatly used in the published version, however, the branch was not merged into master due to the dot version being more reusable. 

* **Master Branch (Dot) Version:** ![alt text](https://www.gaytascience.com/wp-content/uploads/2018/11/dots.gif)
* **Candles Branch (Candle Icon) Version:** ![alt text](https://www.gaytascience.com/wp-content/uploads/2018/11/longgif3.gif)

### Related Products
Related posts can be found below:
* **Final Visualizations:** [2018](https://www.gaytascience.com/tdor2018/), [2017 (TGEU data only)](https://www.gaytascience.com/tdor2017/)
* **Blog Post:** https://www.gaytascience.com/tdor-dataviz/
