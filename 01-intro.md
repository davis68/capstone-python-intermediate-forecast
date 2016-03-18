---
layout: page
title: Scraping Data Using Test-Driven Development
subtitle: Introduction
minutes: 2
---
> ## Learning Objectives {.objectives}
>
> * Explain the .
> * Explain the advantages of a single-table database.

For this capstone exercise, we wish to extract temperature data from a
Web site and plot it by latitude and longitude against a map.

Conceptually, we are going to use three scripts to accomplish the
different stages:

-   `grab_stations.py` will obtain information about station locations in Illinois and output it to the command line (`stdout`)
-   `grab_forecast.py` will obtain information about today's forecast for each station and output it to the command line (`stdout`)
-   `plot_forecast.py` will receive information about station location and today's forecast and plot it against a map of the state of Illinois

First, you will compose standards for the first two scripts (tests the functions have to pass).

You will then divide into two groups:  one group will recreate `grab_stations.py` and test it against a working compiled version of `grab_forecast.py`; the other group will use a working compiled version of `grab_stations.py` to compose the `grab_forecast.py` script.

Finally, you will work with a partner from the other group to put your codes into a new repository and test them against each other.  If you have adhered to the specification (test-driven development), then you should be able to run each other's code without problems.  If there are discrepancies, then correct them and commit the changes to the repo.