# Data Skills 2 Homework 4

### Due Monday November 14th before midnight

For your final assignment you will be creating a choropleth using geopandas and Chicago data, inside an interactive Shiny app.  To do this you will use the City of Chicago [Data Portal](https://data.cityofchicago.org/).

  1. Download the [CTA "L" shapefile](https://data.cityofchicago.org/Transportation/CTA-L-Rail-Lines-Shapefile/53r7-y88m).
  2. Download any other one [shapefile](https://data.cityofchicago.org/browse?tags=shapefiles) of some Chicago division (wards, neighborhoods, etc).  Keep this shapefile relatively small, e.g. police districts, not building footprints.
  3. Download two [datasets](https://data.cityofchicago.org/browse?limitTo=datasets) that can be plotted on your shapefile.  For example, if you choose wards at step two, your data from step three should either be at the ward level, or individual points that could be plotted independent of divisions.
  
Create a single plot of the shapefile from step 2 in your user interface, with controls that allow you to do the following:

  - Toggle the "L" lines shapefile from step 1 off and on.
  - Switch between the two datasets from step 3 to change how the choropleth is colored.
  
Do some basic efforts to make the display look nice - you can clean up your figure using geopandas/pandas/matplotlib/seaborn, and experiment with Shiny elements like tags, rows, and columns.

Finally, include in your repo a screen shot of your Shiny app running in your web browser (with its default settings on the interactions is fine).  Name this file web_page.png.

Note that we will not be deploying your app to the web on shinyapps.io for this assignment.  In my experimenting with the interface I encountered frequent errors that made this difficult to do, which I attribute to the pre-release nature of Shiny in Python.  If you wish to explore the option yourself, the directions are [here](https://docs.rstudio.com/shinyapps.io/getting-started.html#creating-a-shinyapps.io-account).
