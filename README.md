# ECON860-_midterm

## Description
This program is a python script designed to collect and analyze GitHub uyser data from an assigned webpage, as well as the Github API. This program provideds an easy way to gather information about Github Users, and use that information to analyze the data and come up with conclusions. The information is gathered by scraping the given webpage using the 'requests' and 'Beautiful Soup' libraries. 'Pandas" is used to help convert the information into a dataframe, so it can be used put into a .csv file. 'Matplotlib' is used to plot data from the downloaded .csv files into scatterplots. 

## Dependencies 
'requests' is used for making HTTP requests that will fetch data from both websites and the Github API
'beautifulsoup4' is a library used for parsing HTML content. This helps extract data from these websites
'pandas' is a library that is used for data manipulation. This helps us create and manage data frames. 
'Matplotlib' a library allowing used to create a variety of visualizations for data.

## Install
This program was written in the IDE PyCharm 2023. In order to use this scraper, clone the repository or download the both script to your computer. You can install the required libraries using the commands below. 

pip install requests 
pip install pandas
pip install beautifulsoup4
pip install matplotlib

## Screenshots
![ss1](https://github.com/XJrain/ECON860-_midterm/assets/143531877/aed02d1b-0b4c-4549-bf93-683e0cbf6599)
![ss2](https://github.com/XJrain/ECON860-_midterm/assets/143531877/a7c9a40f-a6b1-4170-82c0-0cb9393062ac)
![ss3](https://github.com/XJrain/ECON860-_midterm/assets/143531877/33ef8f5e-ed5e-4562-a986-93e8e5a0722b)
## Usage
This program is very easy to set up and use, and can be customized as needed. You can adjust the URL, .csv file names, and other parameters to fit your needs specifically. Additionally, you can modify the code to grab additional information from the GitHub API if necessary. Running the file Midterm1.py will scrape the URL desired, and put relevant information into a .csv file. It will the take the login IDs from the orginal data frame, compare them to the Github API, and pull the desired information into a new .csv file. Running the Scatterplot.py file will create scatterplots for two separate figures. One plotting Repository Count vs Follower Count, and Follower count vs Starred Count.





---


