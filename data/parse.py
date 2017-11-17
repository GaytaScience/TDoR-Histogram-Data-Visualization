#----------------------------------------------------------------------------------------
# Parse data from Trans day of Rememberance Update Report for Visualization
#
# Kelsey Campbell - 11/11/2017
#
# Report Information:
# TvT research project (2017) “Trans Murder Monitoring (TMM) TDoR 2017 Update”, Transrespect versus Transphobia Worldwide  
# TvT project website: http://transrespect.org/en/trans-murder-monitoring/tmm-resources/ 
# ---------------------------------------------------------------------------------------

# Convert to txt file using PDFMiner on command line:
# pdf2txt.py -o output.txt TvT_TMM_TDoR2017_Namelist_EN.pdf

import pandas as pd

# Converted .txt file
file = open("C:/Users/Kelsey/Desktop/TDOR_2017/data/output.txt", encoding="utf8")

# Initialize pandas dataframe
df = pd.DataFrame()

# Define list of strings designating line without data, to pass (not record)
passStrings = ["Name:", "Age", "Date of death", "Location of death", "Cause of death", "Remarks", "Source", "If you wish to reference", "TVT research project", \
               "TvT research project", "TvT project website", "TMM UPDATE", "reported murders of", "between 1 October", "270978", "bisexual-", "19.01.2017"]

# Initialize loop helper variables
abv2Line = ""
prevLine = ""
prevLabel = ""
cnt = 0
record = {}

# Loop through lines, record data
for line in file:
    
    # Remove next line characters from text
    line = line.replace('\n', '').strip()

    # Skip empty lines
    #if line in ['\n', '\r\n']:
    if len(line.strip()) == 0 and prevLabel == "":
        pass
    
    # Skip page number lines
    elif "transrespect.org" in prevLine:
        pass
    elif "transrespect.org" in abv2Line:
        pass
    
    # Skip label lines
    elif any(s in line for s in passStrings):
        pass
    
    # Otherwise, line has data that we want to record - comes in 7-9 line chunks
    else:
        
        # Update loop helper variable
        cnt += 1

        # First line in chunk is Name
        if cnt == 1:
            name = line
            record['name'] = name
            prevLabel = "name"
        
        # Second line in chunck is Age
        elif cnt == 2:
            age = line
            record['age'] = age
            prevLabel = "age"
        
        # Third line in chunck is Date
        elif cnt == 3:
            date = line
            record['date'] = date
            prevLabel = "date"
        
        # Forth line in chunck is Location
        elif cnt == 4:
            location = line
            record['location'] = location
            prevlabel = "location"
            
            # Parse seperate field for country
            country = location[location.find("(")+1:location.find(")")]
            record['country'] = country
            
            # Create field for Continent
            namerica = ['USA', 'Canada', 'Mexico', 'Dominican Republic', 'Costa Rica', 'El Salvador', 'Honduras']
            samerica = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Paraguay', 'Peru', 'Venezuela']
            asia = ['China', 'India', 'Indonesia', 'Japan', 'Malaysia', 'Nepal', 'Pakistan', "Philippines", 'Thailand', 'Saudi Arabia']
            europe = ['France', "Italy", 'UK', "Russia", 'Turkey', 'Sweden', 'Netherlands', 'Georgia', 'Spain']
            africa = ['Liberia', 'South Africa']
            oceania = ['Papua New Guinea']
            if country in namerica:
                continent = "North America"
            elif country in samerica:
                continent = "South America"
            elif country in asia:
                continent = "Asia"
            elif country in europe:
                continent = "Europe"
            elif country in africa:
                continent = "Africa"
            elif country in oceania:
                continent = "Oceania"
            record['continent'] = continent
        
        # Fifth line in chunck is Cause
        elif cnt == 5:
            cause = line
            record['cause'] = cause
            prevLabel = "cause"
        
        # Sixth line in chunk is Remarks
        elif cnt == 6:
            remarks = line
            prevLabel = "remarks"
        
        # Lines 7-9, however many exist, are either additional Remark lines and/or Source line(s)
        else:
            if prevLabel == "remarks":
                
                # Line 7 is Source and Source is a single line - Record and start over
                #if "TvT" in line and line[-1] not in [",", "&", "n", "a", "1", "s"]: <-- 2016 specific
                if ("TvT" in line or line[0:4] == "http") and line[-1] in ["4", "5", "6", "7", "."]:
                    source = line
                    record['remarks'] = remarks
                    record['source'] = source
                    prevLabel = "source"
                    cnt = 0
                    prevLabel = ""
                    df = df.append(record, ignore_index = True)
                    print(record)
                    print()
                
                # Source has multiple Lines, need next line added to source
                elif "TvT" in line or line[0:4] == "http": 
                    source = line
                    record['remarks'] = remarks
                    prevLabel = "source"
                
                # Line 7 is not source - Remarks had multiple lines
                else: 
                    remarks += " " + line
            
            # If exists, Add 2nd, 3rd line to Source 
            elif prevLabel == "source":
                if len(line.strip()) != 0:
                    source += " " + line

                else: #Record and start over
                    record['source'] = source
                    cnt = 0
                    prevLabel = ""
                    df = df.append(record, ignore_index = True)
                    print(record)
                    print()


    # Update loop helper variables
    abv2Line = prevLine
    prevLine = line


# Write pandas dataframe to .csv file for further manipulation
df.head()
df.to_csv("C:/Users/Kelsey/Desktop/TDOR_2017/data/parsed.csv")
