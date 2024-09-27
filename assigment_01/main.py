from data import data

# Extract the necessary information from the data
year = data['year']
china_data = data['countries']['china']
total_population_china = int(china_data['total_population'])
total_deaths_china = int(china_data['total_deaths'])

saudi_arabia_data = data['countries']['saudi_arabia']
total_population_saudi_arabia = int(saudi_arabia_data['total_population'])
total_deaths_saudi_arabia = int(saudi_arabia_data['total_deaths'])

# Calculate the Crude Death Rate (CDR)
crude_death_rate_china = (total_deaths_china / total_population_china) * 1000
crude_death_rate_saudi_arabia = (total_deaths_saudi_arabia / total_population_saudi_arabia) * 1000


# ------------- CDR (China, year 2000) -------------------
# Print the result
print(f"In {year}, China's Crude Death Rate was {crude_death_rate_china:.2f} deaths per 1,000 people.")


# ------------- CDR (Saudi Arabia, year 2000) -------------------
# Print the result
print(f"In {year}, Saudi Arabia's Crude Death Rate was {crude_death_rate_saudi_arabia:.2f} deaths per 1,000 people.")
