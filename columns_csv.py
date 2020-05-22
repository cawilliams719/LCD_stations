"""
April 30, 2020
LCD Station Import/Sort Data
LCD csv files are imported from outputs in download_data.py
This script iterates through each csv, sorting by mean monthly temperature data.
Columns of interested are printed as a result of this script.
"""

#Import csv and operator
import csv
import operator
import itertools

#Specify filenames to be sorted
filename = ["C:/Users/Caroline/Documents/Thesis_Data/LCD_WashingtonCoAirportPA_2005_2014.csv",
            "C:/Users/Caroline/Documents/Thesis_Data/LCD_QuakertownAirportPA_2005_2014.csv",
            "C:/Users/Caroline/Documents/Thesis_Data/LCD_IndianaJStewartPA_2005_2014.csv",
            "C:/Users/Caroline/Documents/Thesis_Data/LCD_AllentownLehighValleyInternationalAirportPA_2005_2014.csv",
            "C:/Users/Caroline/Documents/Thesis_Data/LCD_UniversityParkPA_2005_2014.csv",
            "C:/Users/Caroline/Documents/Thesis_Data/LCD_CaldwellEssexCoAirportNJ_2005_2014.csv",
            "C:/Users/Caroline/Documents/Thesis_Data/LCD_SussexAirportNJ_2005_2014.csv",
            "C:/Users/Caroline/Documents/Thesis_Data/LCD_PoughkeepsieAirportNY_2005_2014.csv",
            "C:/Users/Caroline/Documents/Thesis_Data/LCD_MonticelloSullivanNY_2005_2014.csv"]

#Specify the filename outputs and location
output =["C:/Users/Caroline/Documents/Thesis_Data/LCD_WashingtonCoAirportPA_2005_2014_columns.csv",
         "C:/Users/Caroline/Documents/Thesis_Data/LCD_QuakertownAirportPA_2005_2014_columns.csv",
         "C:/Users/Caroline/Documents/Thesis_Data/LCD_IndianaJStewartPA_2005_2014_columns.csv",
         "C:/Users/Caroline/Documents/Thesis_Data/LCD_AllentownLehighValleyInternationalAirportPA_2005_2014_columns.csv",
         "C:/Users/Caroline/Documents/Thesis_Data/LCD_UniversityParkPA_2005_2014_columns.csv",
         "C:/Users/Caroline/Documents/Thesis_Data/LCD_CaldwellEssexCoAirportNJ_2005_2014_columns.csv",
         "C:/Users/Caroline/Documents/Thesis_Data/LCD_SussexAirportNJ_2005_2014_columns.csv",
         "C:/Users/Caroline/Documents/Thesis_Data/LCD_PoughkeepsieAirportNY_2005_2014_columns.csv",
         "C:/Users/Caroline/Documents/Thesis_Data/LCD_MonticelloSullivanNY_2005_2014_columns.csv"]


#stationame = ["PortsmouthPeaseAFBNH", "MountWashingtonNH","PittsfieldMunicipalAirportMA"]

#Sort and print station ID, date, monthly maximum, monthly mean, and monthly minimum data
for fname, fout in itertools.izip(filename,output):
    sample = open((fname),"rb")
    csv1 = csv.reader (sample,delimiter= ",")
    sort = sorted(csv1, key=operator.itemgetter(80),reverse=True)#number here identifies the column to sort by from high to low
    newsamp = open((fout),'wb')
    for column in sort:
        csv2 = csv.writer(newsamp, delimiter=",")
        csv2.writerow((column[0:1], column[1:2], column[80:81], column[81:82], column[85:86]))
    newsamp.close
