from datetime import datetime, timedelta

jours_semaine = {
    "lundi": 0,
    "mardi": 1,
    "mercredi": 2,
    "jeudi": 3,
    "vendredi": 4,
    "samedi": 5,
    "dimanche": 6
}

mois_annee = {
    "janvier": 1,
    "février": 2,
    "mars": 3,
    "avril": 4,
    "mai": 5,
    "juin": 6,
    "juillet": 7,
    "août": 8,
    "septembre": 9,
    "octobre": 10,
    "novembre": 11,
    "décembre": 12
}

# Exemple d'utilisation
print("Le numéro associé à février est:", mois_annee["février"])
print("Le numéro associé à septembre est:", mois_annee["septembre"])


# Exemple d'utilisation
print("Le numéro associé à mardi est:", jours_semaine["mardi"])
print("Le numéro associé à dimanche est:", jours_semaine["dimanche"])


from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()
print("Current date and time:", current_datetime)

# Access components of the datetime object
print("Year:", current_datetime.year)
print("Month:", current_datetime.month)
print("Day:", current_datetime.day)
print("Hour:", current_datetime.hour)
print("Minute:", current_datetime.minute)
print("Second:", current_datetime.second)

# Format the date as a string
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date:", formatted_date)

# Parse a string to create a datetime object
date_string = "2023-01-01 12:30:00"
parsed_datetime = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", parsed_datetime)


# Get the current date
current_date = datetime.now()

# Calculate the start and end of the current week
start_of_week = current_date - timedelta(days=current_date.weekday())
end_of_week = start_of_week + timedelta(days=6)

# Format and print the start and end dates of the week
formatted_start_of_week = start_of_week.strftime("%Y-%m-%d")
formatted_end_of_week = end_of_week.strftime("%Y-%m-%d")
print("Start of the current week:", formatted_start_of_week)
print("End of the current week:", formatted_end_of_week)

# Get the ISO week number
week_number = current_date.isocalendar()[1]

# Print the current week number
print("Current week number:", week_number)

# from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Set the start date to the first day of the next year
start_date = datetime(current_date.year + 1, 1, 1)

# Iterate through the days of the next year
current_day = start_date
while current_day.year == start_date.year:
    if current_day.weekday() == 4:  # 4 corresponds to Friday
        formatted_date = current_day.strftime("%Y-%m-%d")
        print("Friday:", formatted_date)



    current_day += timedelta(days=1)
    
def get_all_jours_nextYear(jour):
    current_day = start_date
    n = 4
    while current_day.year == start_date.year:
        if current_day.weekday() == n:  
            formatted_date = current_day.strftime("%Y-%m-%d")
            print(f"{jour}:", formatted_date)

        current_day += timedelta(days=1)
        
get_all_jours_nextYear("vendredi")

from datetime import datetime, timedelta

def get_all_jours_nextYear(jour,jours_semaine):
    
    jour=jours_semaine[jour]
    
    # Get the current date
    current_date = datetime.now()

    # Set the start date to the first day of the next year
    start_date = datetime(current_date.year + 1, 1, 1)

    # Initialize an empty list to store the dates
    dates_list = []

    # Iterate through the days of the next year
    current_day = start_date
    while current_day.year == start_date.year:
        if current_day.weekday() == jour:
            formatted_date = current_day.strftime("%Y-%m-%d")
            dates_list.append(formatted_date)

        current_day += timedelta(days=1)

    return dates_list

# Example usage

jour_to_find = "vendredi"
le_quantieme = 2
next_year_jours = get_all_jours_nextYear(jour_to_find,jours_semaine)  # 4 corresponds to Friday
print(f"{jour_to_find} of next year:", next_year_jours)

print(next_year_jours[le_quantieme-1])
# print(next_year_jours[3])




