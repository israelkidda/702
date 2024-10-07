from data import population


# General expressions for CDR, CBR, CRNM, CRNPI, and CGR
cdr_formula = '''
Crude Death Rate (CDR) Formula:


CDR = (Total Deaths / Total Population) × 1000
'''


cbr_formula = '''
Crude Birth Rate (CBR) Formula:


CBR = (Total Births / Total Population) × 1000
'''


crnm_formula = '''
Crude Rate of Net Migration (CRNM) Formula:


CRNM = (Total Net Migration / Total Population) × 1000
'''


crnpi_formula = '''
Crude Rate of Natural Population Increase (CRNPI) Formula:


CRNPI = CBR - CDR
'''


cgr_formula = '''
Crude Growth Rate (CGR) Formula:


CGR = CRNPI + CRNM
'''


print(cdr_formula)
print(cbr_formula)
print(crnm_formula)
print(crnpi_formula)
print(cgr_formula)


# Extract the necessary information from the data
year = population['year']
china_data = population['countries']['china']
total_population_china = int(china_data['total_population'])
total_deaths_china = int(china_data['total_deaths'])
total_births_china = int(china_data['total_births'])
total_net_migration_china = int(china_data['total_net_migration'])


saudi_arabia_data = population['countries']['saudi_arabia']
total_population_saudi_arabia = int(saudi_arabia_data['total_population'])
total_deaths_saudi_arabia = int(saudi_arabia_data['total_deaths'])
total_births_saudi_arabia = int(saudi_arabia_data['total_births'])
total_net_migration_saudi_arabia = int(saudi_arabia_data['total_net_migration'])


# Calculate the Crude Death Rate (CDR)
crude_death_rate_china = (total_deaths_china / total_population_china) * 1000
crude_death_rate_saudi_arabia = (total_deaths_saudi_arabia / total_population_saudi_arabia) * 1000


# Calculate the Crude Birth Rate (CBR)
crude_birth_rate_china = (total_births_china / total_population_china) * 1000
crude_birth_rate_saudi_arabia = (total_births_saudi_arabia / total_population_saudi_arabia) * 1000


# Calculate the Crude Rate of Net Migration (CRNM)
crude_net_migration_rate_china = (total_net_migration_china / total_population_china) * 1000
crude_net_migration_rate_saudi_arabia = (total_net_migration_saudi_arabia / total_population_saudi_arabia) * 1000


# Calculate the Crude Rate of Natural Population Increase (CRNPI)
crude_rate_natural_increase_china = crude_birth_rate_china - crude_death_rate_china
crude_rate_natural_increase_saudi_arabia = crude_birth_rate_saudi_arabia - crude_death_rate_saudi_arabia


# Calculate the Crude Growth Rate (CGR)
crude_growth_rate_china = crude_rate_natural_increase_china + crude_net_migration_rate_china
crude_growth_rate_saudi_arabia = crude_rate_natural_increase_saudi_arabia + crude_net_migration_rate_saudi_arabia


# Function to print results
def print_results(country, measure, rate, decimal, percentage):
   print(f"In {year}, {country}'s {measure} was {rate:.2f} per 1,000 people.")
   print(f"In decimal form, {country}'s {measure} was {decimal:.5f} per person.")
   print(f"In percentage form, {country}'s {measure} was {percentage:.2f}% per population.")
   print()


# Print results for China
print_results("China", "Crude Death Rate", crude_death_rate_china,
             crude_death_rate_china/1000, crude_death_rate_china/10)
print_results("China", "Crude Birth Rate", crude_birth_rate_china,
             crude_birth_rate_china/1000, crude_birth_rate_china/10)
print_results("China", "Crude Rate of Net Migration", crude_net_migration_rate_china,
             crude_net_migration_rate_china/1000, crude_net_migration_rate_china/10)
print_results("China", "Crude Rate of Natural Population Increase", crude_rate_natural_increase_china,
             crude_rate_natural_increase_china/1000, crude_rate_natural_increase_china/10)
print_results("China", "Crude Growth Rate", crude_growth_rate_china,
             crude_growth_rate_china/1000, crude_growth_rate_china/10)


# Print results for Saudi Arabia
print_results("Saudi Arabia", "Crude Death Rate", crude_death_rate_saudi_arabia,
             crude_death_rate_saudi_arabia/1000, crude_death_rate_saudi_arabia/10)
print_results("Saudi Arabia", "Crude Birth Rate", crude_birth_rate_saudi_arabia,
             crude_birth_rate_saudi_arabia/1000, crude_birth_rate_saudi_arabia/10)
print_results("Saudi Arabia", "Crude Rate of Net Migration", crude_net_migration_rate_saudi_arabia,
             crude_net_migration_rate_saudi_arabia/1000, crude_net_migration_rate_saudi_arabia/10)
print_results("Saudi Arabia", "Crude Rate of Natural Population Increase", crude_rate_natural_increase_saudi_arabia,
             crude_rate_natural_increase_saudi_arabia/1000, crude_rate_natural_increase_saudi_arabia/10)
print_results("Saudi Arabia", "Crude Growth Rate", crude_growth_rate_saudi_arabia,
             crude_growth_rate_saudi_arabia/1000, crude_growth_rate_saudi_arabia/10)
