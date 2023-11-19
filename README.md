## TDoR Histogram Data Visualization
Data Visualization for Transgender Day of Remembrance (TDoR) 11/20 

### Data Folder
[Trans Respect vs Transphobia Worldwide](http://transrespect.org) publishes [reports for TDoR](http://transrespect.org/en/trans-murder-monitoring/tmm-resources/) every year. One of the reports is a Name List, which lists available information for every reported murder of a trans or gender-diverse person in the last year. 

In 2018, [Anna-Jayne Metcalfe](https://twitter.com/annajayne) sought out to [learn more about all those we have lost](https://medium.com/@annajayne/tdor-learning-more-about-those-we-have-lost-8043146f402c). The new https://tdor.translivesmatter.info/ website combines, gathers, and disseminates details about each victim’s life and death in a way that has not been available before, allowing the community to better connect with and celebrate them.

The 2017 data folder contains parsing scripts and data from the TGEU original reports, while all other years contain cleaned files pulled from https://tdor.translivesmatter.info/ 

### Visualization
The file dotbar.html contains the code for the d3.v4.js visualization (TW abuse, death, murder, rape, suicide, torture, transphobia, violence, weapons): 
![Animated gif of Transgender Day of Remembrance (TDoR) data visualization.](https://www.gaytascience.com/wp-content/uploads/2023/11/giflong.gif)

### Links
* **Final Visualizations:** [2023](https://www.gaytascience.com/tdor2023/), [2022](https://www.gaytascience.com/tdor2022/), [2021](https://www.gaytascience.com/tdor2021/), [2020](https://www.gaytascience.com/tdor2020/), [2019](https://www.gaytascience.com/tdor2019/), [2018](https://www.gaytascience.com/tdor2018/), [2017 (TGEU data only)](https://www.gaytascience.com/tdor2017/)
* **Blog Post:** https://www.gaytascience.com/tdor-dataviz/

### Development
Visualization can be built locally after cloning the repository. For example, to use a python simple server:
* In a terminal navigate to the repository folder (`cd [filepath]`)
* Start a simple server for local development. For Python 3 the command is `python -m http.server 8000`
* In a browser go to http://localhost:8000/dotbar.html
* Files can now be edited locally with changes reflected when you refresh your browser page!
