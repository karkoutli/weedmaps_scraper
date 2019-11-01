import sys
from source import scraper
# sys.path.append('source/')
# import scraper

weedmaps_json_site = "https://api-g.weedmaps.com/discovery/v1/listings?sort_by=position&filter%5Blocation%5D=any&latlng=33.96210098266602%2C-118.2745513916016&page_size=100&page=1"
source = "Weedmaps"

weedmap = scraper.scraper(weedmaps_json_site, source)
weedmap.connect()
weedmap.parse()
weedmap.output("11_01")

print("All Done")