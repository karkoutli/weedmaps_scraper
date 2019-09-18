import requests
import csv
#from lxml import html
#import time
import json
import arcpy

#how do i seperate this from the mainfile???
class scraper:

    #constructor method
    
    def __init__(self, json_site, source):
        self.json_site = json_site  
        self.source = source

    #
    def parse(self):
        count = 0
        dataframe = [] # <- python list

        resp = requests.get(self.json_site)

        if resp:
            print('Successfully connected to site!') #status 200
        else:
            print('An error has occurred, please check internet connection.') #status 404

        #print(resp.text) <- html text, maybe practice using using beautifulsoup 

    ####################################^^^CONNECTION CHECK^^^###################################################

        #requests JSON in (json() returns a dictionary{x:x})
        newJson = resp.json()["data"]["listings"]#only want data from listings

        for value in newJson:
            if value["address"]: #<- if "x" exists in the dictionary

                data = {#what you want         what its labeled
                        "business name":value["name"],
                        "address":value["address"],
                        "longitude": value["longitude"],
                        "latitude": value["latitude"],
                        "state": value["state"],
                        "city": value["city"],
                        "zip_code": value["zip_code"],
                        "ranking": value["ranking"],
                        "rating": value["rating"],
                        "web_url": value["web_url"],
                        "reviews_count": value["reviews_count"],
                        "license type":value["license_type"],
                        "type":value["type"],
                        "intro_body":value["intro_body"],
                        "retailer_services":value["retailer_services"][0],
                        }

                dataframe.append(data)
                count += 1
                print("Dispensaries Converted: ", count)


        #json streamwriter out
        with open('output/weedmaps_0919.json', 'w', encoding = 'utf-8') as jsonStream: 
            json.dump(dataframe, jsonStream)
            jsonStream.close()

        #csv streamwriter /// maybe try pandas
        with open('output/weedmaps_0919.csv', 'w', encoding = 'utf-8') as csvStream:
            
            fields = [
                        "business name",
                        "address",
                        "longitude",
                        "latitude",
                        "state",
                        "city",
                        "zip_code",
                        "ranking",
                        "rating",
                        "web_url",
                        "reviews_count",
                        "license type",
                        "type",
                        "intro_body",
                        "retailer_services",
                     ]

            writer = csv.DictWriter(csvStream, fieldnames = fields) #fieldnames is how Dictwriter identifies column names in 
            
            writer.writeheader()
            writer.writerows(dataframe)

            print("writing completed")
            csvStream.close()


weedmaps_json_site = "https://api-g.weedmaps.com/discovery/v1/listings?sort_by=position&filter%5Blocation%5D=any&latlng=33.96210098266602%2C-118.2745513916016&page_size=100&page=1"
source = "Weedmaps"

dummy = scraper(weedmaps_json_site, source)
dummy.parse()