---
layout: page
title: Scraping Data Using Test-Driven Development
subtitle: Test-Driven Development
minutes: 30
---
> ## Learning Objectives {.objectives}
>
> * Explain the test-driven development process and apply it to a simple problem.
> * Compose appropriate unit tests for the component functions.

First, we need to consider the structure of our scripts.

-   `grab_stations.py`:
    -   receives no input from the command line
    -   scrapes station location data from the Web
    -   refactors the data into a sensible data structure
    -   outputs the station signs and their latitude and longitude (to `stdout`)

-   `grab_forecast.py`
    -   receives station sign and latitude and longitude from `stdin`
    -   scrapes the corresponding station forecast data from the Web
    -   refactors the data into a sensible data structure
    -   outputs the station signs, their latitude and longitude, and today's forecast (to `stdout`)

-   `plot_forecast.py`
    -   receives station sign, their latitude and longitude, and today's forecast from `stdin`
    -   plots station temperature and position against a map of the state of Illinois


### Script structure

Before we consider the technical details of these scripts, let's actually write some function descriptions for the two scripts we are responsible for.

Examine the steps above for each file and suggest a structure for the main function.  (This is an instructor-guided activity on a whiteboard.  The result should look something like the following.)

-   `grab_stations.py`:
        
        if __name__ == '__main__':
            text = grab_website_data()
            data = extract_section(text)
            for line in data.splitlines():
                try:
                    stn, lat, lon = parse_station_line(line)
                    print('%s\t%f\t%f'%(stn,lon,lat))
                except:
                    print('Could not parse line\n\t%s'%line)

-   `grab_forecast.py`:
        
        if __name__ == '__main__':
            input = grab_stdin()
            temp_data = grab_forecast_data()
            for line in input.splitlines():
                try:
                    stn, lat, lon = line.split('\t')
                    temp = get_station_temp(temp_data, stn)
                    print('%s\t%f\t%f\t%f'%(stn,lon,lat,temp))
                except:
                    print('Could not parse line\n\t%s'%line)


### Function unit tests

What sorts of things do we need to specify?

-   output format from each script
-   format of latitude and longitude

Let's write unit tests for a couple of functions then:

-   `parse_station_line`
-   `get_station_temp`

(The others mainly grab or manipulate large blocks of HTML as plain text strings, so we won't worry about the details of them right now.)


### What don't we know how to do yet?

The instructor should clarify any principles which need to be explained at this point.

-   `requests.text`
-   `sys.stdin`
-   parse/scrape the text (by inspection)


Compiled Python bytecode versions have been included in the `py2-pyc/` and `py3-pyc/` directories.  These can be used to test your code against the others:
    
    python py2-pyc/grab_stations.pyc | python py2-pyc/grab_forecast.pyc | python py2-pyc/plot_forecast.pyc 
    
or
    
    python3 py3-pyc/grab_stations.pyc | python3 py3-pyc/grab_forecast.pyc | python3 py3-pyc/plot_forecast.pyc 
