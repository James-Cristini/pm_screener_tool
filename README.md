# pm_screener_toolkit
The pm_screener_tool is a Python application currently in use by the project management department that is composed of threee major functionalities that aid each assoicate in performing due dilligence tasks quickly, efficiently, and accurately. It builds upon the previous, standalone stem_filter program and adds the ability to search names via google (with or without an added keyword) and through Micromedex, an online drug database.

## Stem Filter
This aspect of the program allows a user to input a list of names and builds an excel document (using xlwt) which outlines any/all conflicts with each name. Users are able to choose between different types of projects in order to filter names through different parameters.

![Picture](http://i.imgur.com/ZHuJI2B.png?1) 

## Google Searcher
Checking names on google is a great way to determine if a brand name is currently being used by another company and so is part of our due diligence process. The Google tab in this application allows users to input a list of names and will open up new tabs in google for each. Users are also able to searcg wuth a keyword to further refine their search.

![Picture](http://i.imgur.com/dshBfYh.png?1) 

## Micromedex Scraper
This final part of the application allows users to input a list of names and will search each of those names through Micromedex, a large online drug database with a handy lookup tool, helpful for finding similar drug names across markets. 

Once all of the data for each name has been gathered, a table is built outlining the name checked, the number of conflicts found, and what those conflicts are. In the final column is a direct link to the data on the Micromedex site. Cells highlighted in red indicate that there is further information with the name that should be investigated via the direct linke. 

Users are also able to export the data to an excel document which is in the exact format needed for an easy copy-paste int he master database for the names.

![Picture](http://i.imgur.com/yjx9ayy.png?1) 



PyQt4
webbrowser
requests
Beautifulsoup
urllib
xlwt
