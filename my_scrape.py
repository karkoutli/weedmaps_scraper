import scraper

weedmaps_json_site = "https://api-g.weedmaps.com/discovery/v1/listings?filter%5Bbounding_box%5D=33.77115672832914%2C-119.14947509765626%2C34.16977214177208%2C-117.39166259765626&page_size=100&page=1"
source = "Weedmaps"

weedmap = scraper(weedmaps_json_site, source)
weedmap.parse()
weedmap.output("test")