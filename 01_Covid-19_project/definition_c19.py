import requests
import json
import os
os.chdir('D:\\programowanie\\vs code\\01_Covid-19_project')


r = requests.get("https://api.covid19api.com/dayone/country/poland")

tasks = r.json()

def create_cases_list(first_value, second_value):
    result = []
    for day in tasks:
        result.append((day[first_value][:10], day[second_value]))
    return result


def create_text_file(file_name, list_name):
    with open(file_name, "w") as file:
        for item in list_name:
            file.write("{}\n".format(item))


def create_cases_list_per_day(lista):
    result = [(lista[0][0], lista[0][1])]
    i = 1
    while i < len(lista):
        result.append(
            (lista[i][0], (lista[i][1]-lista[i-1][1])))
        i += 1
    return result