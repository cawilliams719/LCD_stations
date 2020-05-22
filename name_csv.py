"""
April 30, 2020
LCD Station Data Download
Local Climatological Data is ordered from the provided url: https://www.ncdc.noaa.gov/cdo-web/datatools/lcd
Once each order is processed the download for each station is copied
This script saves the csv files from  these csv url links into the appropriate naming convention
"""

#Import Library Requests
import itertools 
import requests

"""
LCD Download URL links: How to Copy
Using the URL in the first comment block, download desired stations
specify format, year, etc
order the station
copy download links in email
"""

#Copy URL link for LCD station download
url = ['https://nam10.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.ncei.noaa.gov%2Forders%2Fcdo%2F2131845.csv&data=02%7C01%7Ccawilliams%40clarku.edu%7Ccba2af6919c54694c41b08d7eca2a5cc%7Cb5b2263d68aa453eb972aa1421410f80%7C1%7C0%7C637238055636097486&sdata=IKqxmbA1BE0QrXcQ%2FLLbVV%2FvQJWdA37HZcmexSESwKg%3D&reserved=0',
       'https://nam10.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.ncei.noaa.gov%2Forders%2Fcdo%2F2131847.csv&data=02%7C01%7Ccawilliams%40clarku.edu%7Ced431509f62b485334cc08d7eca358ae%7Cb5b2263d68aa453eb972aa1421410f80%7C1%7C0%7C637238058629588355&sdata=VlrhwYPLSm7%2BFgVzni8eHK3lqPfA6bg2yeBqGDbNjI0%3D&reserved=0',
       'https://nam10.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.ncei.noaa.gov%2Forders%2Fcdo%2F2131855.csv&data=02%7C01%7Ccawilliams%40clarku.edu%7C14bac1f969954eaa34e908d7eca40b7e%7Cb5b2263d68aa453eb972aa1421410f80%7C1%7C0%7C637238061623354368&sdata=1sEM8gHkVTaxoA2mCbEWzcRiUIUK7p%2BPRkQ9pe4kTL8%3D&reserved=0',
       'https://nam10.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.ncei.noaa.gov%2Forders%2Fcdo%2F2131858.csv&data=02%7C01%7Ccawilliams%40clarku.edu%7Cc5d323cd586346b16df708d7eca476dd%7Cb5b2263d68aa453eb972aa1421410f80%7C1%7C0%7C637238063428169794&sdata=XcjfjEo1ar1zG7F2C%2BMUjxWhJPDXIj%2B5UEAqKyYjYW4%3D&reserved=0',
       'https://nam10.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.ncei.noaa.gov%2Forders%2Fcdo%2F2131860.csv&data=02%7C01%7Ccawilliams%40clarku.edu%7Cedc46b8be59d4da8d34b08d7eca529aa%7Cb5b2263d68aa453eb972aa1421410f80%7C1%7C0%7C637238066426233180&sdata=7%2ByjCsq6Pbr5hbMkHxqK49RSZjx8FFrN3%2BgxdVK6T28%3D&reserved=0',
       'https://nam10.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.ncei.noaa.gov%2Forders%2Fcdo%2F2131864.csv&data=02%7C01%7Ccawilliams%40clarku.edu%7C9ce81cc0e46c4f8c2a4708d7eca582d1%7Cb5b2263d68aa453eb972aa1421410f80%7C1%7C0%7C637238067928552070&sdata=Lvn24Cc3J%2FQ2C9gmoEUPAZM1zWxmmfL6TMqxqzBz2hQ%3D&reserved=0',
       'https://nam10.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.ncei.noaa.gov%2Forders%2Fcdo%2F2131868.csv&data=02%7C01%7Ccawilliams%40clarku.edu%7Cd5e40b04820f4b7c73db08d7eca5ee06%7Cb5b2263d68aa453eb972aa1421410f80%7C1%7C0%7C637238069797634692&sdata=2JaWGwcxELGfpDvFW2pXFX0qTmFeUYZl8WScjfUp2I4%3D&reserved=0',
       'https://nam10.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.ncei.noaa.gov%2Forders%2Fcdo%2F2131871.csv&data=02%7C01%7Ccawilliams%40clarku.edu%7Cd8116b5a8b814f600d5508d7eca65976%7Cb5b2263d68aa453eb972aa1421410f80%7C1%7C0%7C637238071519572539&sdata=gq8IZoeC0oQU9qzxVqYSk5AlFCY2KhfJvXyO4FNmNMA%3D&reserved=0',
       'https://nam10.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.ncei.noaa.gov%2Forders%2Fcdo%2F2131873.csv&data=02%7C01%7Ccawilliams%40clarku.edu%7C17a85f736b2445c1fe1208d7eca70c13%7Cb5b2263d68aa453eb972aa1421410f80%7C1%7C0%7C637238074526845052&sdata=%2B7cm%2FqcW%2Fmb%2BCqlHIHalj3qmw3Otzxh1OFZX2v1u2iY%3D&reserved=0']

#List Station Names to be used in the csv file name
stationame = ["WashingtonCoAirportPA","QuakertownAirportPA","IndianaJStewartPA","AllentownLehighValleyInternationalAirportPA","UniversityParkPA","CaldwellEssexCoAirportNJ","SussexAirportNJ","PoughkeepsieAirportNY","MonticelloSullivanNY"]

#For loop to iterate through both the URL links provided and list of station names to use
for item, name in itertools.izip(url, stationame):
    req = requests.get(item, allow_redirects = True)
    url_content = req.content
    csv_file = open("LCD_" + str(name)+"_2005_2014.csv", "wb")
    csv_file.write(str(url_content))
    csv_file.close()
        
        
