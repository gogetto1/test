"""
This program shows how Covid-19 pandemic looks like day by day.
It shows in txt files: date and number of people infected from the beginning and per day. 
 
"""

from definition_c19 import create_cases_list, create_text_file, create_cases_list_per_day


confirmed_list = create_cases_list("Date", "Confirmed")

deaths_list = create_cases_list("Date", "Deaths")

confirmed_per_day_list = create_cases_list_per_day(confirmed_list)

deaths_per_day_list = create_cases_list_per_day(deaths_list)

create_text_file("date_confirmed_covid.txt", confirmed_list)

create_text_file("date_deaths_covid.txt", deaths_list)

create_text_file("confirmed_per_day.txt", confirmed_per_day_list)

create_text_file("death_per_day.txt", deaths_per_day_list)
