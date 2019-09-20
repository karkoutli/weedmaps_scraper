import requests
import csv
#from lxml import html
#import time
import json
import datetime

#how do i seperate this from the mainfile???
class scraper:

    #constructor method
    
    def __init__(self, json_site, source):
        current = datetime.datetime.now()

        self.date = current.strftime("%d%m%Y")
        self.json_site = json_site  
        self.source = source
    
    def parse(self):
        count = 0
        self.dataframe = [] # <- python list

        resp = requests.get(self.json_site)

        if resp:
            print('Successfully connected to site!') #status 200
        else:
            print('An error occurred, please check internet connection and try rerunning the script') #status 404

        #print(resp.text) <- html text, maybe practice using using beautifulsoup 

        #requests JSON in (json() returns a dictionary{x:x})
        newJson = resp.json()["data"]["listings"]#only want data from listings

        for value in newJson:
            if value["name"]: #<- if "x" exists in the JSON dictionary

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

                self.dataframe.append(data)
                count += 1
                print("Dispensaries Scraped: ", count)


    def output(self, filename):
        #json streamwriter out

        with open("output/" + filename + self.date + ".json", 'w', encoding = 'utf-8') as jsonStream: 
            json.dump(self.dataframe, jsonStream)
            jsonStream.close()

        #csv streamwriter /// maybe try pandas
        with open("output/" + filename + ".csv", 'w', encoding = 'utf-8') as csvStream:
            
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
            writer.writerows(self.dataframe)

            print("writing completed")
            csvStream.close()

