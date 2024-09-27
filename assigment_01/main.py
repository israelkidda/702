from data import data

# Extract the necessary information from the data
year = data['year']
china_data = data['countries']['china']
total_population = int(china_data['total_population'])
total_deaths = int(china_data['total_deaths'])

# Calculate the Crude Death Rate (CDR)
crude_death_rate = (total_deaths / total_population) * 1000


# ------------- CDR (China, year 2000) -------------------
# Print the result
print(f"In {year}, China's Crude Death Rate was {crude_death_rate:.2f} deaths per 1,000 people.")
