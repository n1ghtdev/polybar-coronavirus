#!/bin/python

import sys
import requests

URL = "https://corona.lmao.ninja/v2/all"
headers = {'Content-Type': 'application/json'}

def get_corona_data():
    try:
        response = requests.get(URL, headers=headers)
    except (requests.ConnectionError,
                requests.RequestException,
                requests.HTTPError,
                requests.Timeout,
                requests.TooManyRedirects) as error:
        msg = str(error)
        print(msg)

    if response.status_code != 200:
        print('Server responded with status code {}'.format(response.status_code))

    response_data = response.json()
    return response_data

def format_string(string):
    return '{:,}'.format(string).replace(',', ' ')

def get_print_output(corona_data):
    cases = format_string(corona_data['cases'])
    todayCases = format_string(corona_data['todayCases'])
    deaths = format_string(corona_data['deaths'])
    todayDeaths = format_string(corona_data['todayDeaths'])

    # lemonbar color formatting
    output = f'{cases} %{{F#00FF00}}+{todayCases}%{{F-}} / {deaths} %{{F#FF0000}}+{todayDeaths}%{{F-}}'
    return output

data = get_corona_data()
data_output = get_print_output(data)

sys.stdout.write(data_output)
