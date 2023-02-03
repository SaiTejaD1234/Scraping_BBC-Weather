# Scraping Weather from BBC Website
    1.  Project Motivation
    2.  Installation
    3.  Implementation
    4.  Result


## 1. Project Motivation
Web Scarping is an important aspect of Data Science. This requires patience and attention to detail. When Scarping I spend 30-40% of the time analyzing the webpage *(navigate through HTML parse trees and inspecting elements)* and the rest in **ETL**. This project was meant to showcase my Scarping skills.
## 2. Installation
* Python version 3.*.
* Python Libraries:
     * pandas
     * numpy
     * bs4
     * os
     * re
     * json
      
## 3. Implementation
The helper function was written to extract the ID for the city. Using the ID we find the url for the BBC website containing the weather. We parse the loaded webpage and extact the high, low, date and summary throught each unique attributes from the parsed webpage. The values are stored in respective arrays and are loaded into a dataframe with date as index. 

Using the .py file you can keep harvesting data that's being updated every hour. The new/refreshed data is being written to a .txt file that will be stored on your local computer. Furthermore the code has been written in such a way that it can also be deployed on jupyter notebook (invovles copy/pasting into cells)

## 4. Result
The high, low and summary for the dates have been scraped. The weather for 13 days has been loaded into the dataframe. It contains high, low and summary for the date.
The text file created will keep adding new data and will serve as a record of the weather.
