# Python CLI Weather Application

## Description
This is a CLI weather application built with python.

## Python modules
1. argparse
2. json
3. sys
4. configparser import ConfigParser
5. urllib

## API
Open Weather appli

## Installation
1. Install python3
2. Add python to the system path
3. Clone this application into your system

### Secret.ini
As part of the installation guideline, you have to add secret.ini file in the same directory containing the main.py

The secret.ini file should contain the following two lines of code.

[openweather]
api_key = <Your API key>

### API Key
In other to get the API key, you have to sign up an account on Open Weather website:
www.openweather.com

## How to run the application
(Make sure you have internet connection in other to be able to access data from the API)
On the directory containing the main.py file, run the command:

python main.py <name of city>

### Example
python main.py irkutsk

The above example will give the weather information of irkutst

## Acknowledgement
Realpython.com
