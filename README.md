# Analyzing county-level presidential vote data from 2000 to 2020 in Texas for GOP, Democratic, Libertarian and Green parties

This respiratory contains the python code used to scrape county-level presidential election data for Texas counties. 

I used the [https://uselectionatlas.org/](https://uselectionatlas.org/) website and extracted the county-level presendtial votes.

I used [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library to extract each party's vote number from html code and saved it on a csv file.

You can change the `year` variable to get the information of different presidential election years.

For example, the output for 2020 year would be a table like below:

| County   | Republican | Democratic | Liberterian | Green |
|----------|------------|------------|-------------|-------|
| Anderson | 15110      | 3955       | 134         | 22    |
| Anderews | 4943       | 850        | 60          | 10    |
| ...      |            |            |             |       |
| Zavala   | 1490       | 2864       | 13          | 12    |



