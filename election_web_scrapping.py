import requests
from bs4 import BeautifulSoup
import csv


def get_info_from_county(url):
    
    # get the page using requests
    page = requests.get(url)
        
    # parse html data
    soup = BeautifulSoup(page.content, "html.parser")
    
    # retrieve table related tags
    table = soup.find_all('table', {'class':'result'})[0]
    tbody = table.find('tbody')
    rows = tbody.find_all('tr')
    
    # initialize variables for each party
    rep_num = 0
    dem_num = 0
    lib_num = 0
    grn_num = 0
    
    # for each row in table rows
    for row in rows:
        # find tags with attribute class value of 'name' and 'num'
        columns = row.find_all('td', {'class':['name', 'num']})

        # update the party number               
        if columns[2].contents[0] == 'Republican':
            rep_num = columns[3].contents[0]
        elif columns[2].contents[0] == 'Democratic':
            dem_num = columns[3].contents[0]
        elif columns[2].contents[0] == 'Libertarian':
            lib_num = columns[3].contents[0]
        elif columns[2].contents[0] == 'Green':
            grn_num = columns[3].contents[0]
            
    # get name of county
    b_tags = soup.find_all('b')
    county_name = b_tags[1].contents[0].split()[0]
    
    # wrap variables in list
    output_row = [county_name, rep_num, dem_num, lib_num, grn_num]
    return output_row
    

# create initial variables to form the url
base_url = "https://uselectionatlas.org/RESULTS/statesub.php?"
first_county_id = 48001
last_county_id = 48508
year = 2020
output_filename = "county_level_presidential_data_{}.csv".format(year)

# create headers of csv data
csv_data = []
csv_data.append(['County', 'Republican', 'Democratic', 'Libertarian', 'Green'])

for county_id in range(first_county_id, last_county_id, 2):
    url = base_url + "year={}&fips={}&minper=0&f=1&off=0&elect=0".format(year, county_id)
    csv_row = get_info_from_county(url)
    csv_data.append(csv_row)
    
# save the csv data list to the csv file
with open(output_filename, "w") as f:
    writer = csv.writer(f)
    writer.writerows(csv_data)
    