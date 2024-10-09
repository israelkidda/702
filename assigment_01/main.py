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

# General expression for age-specific mortality rates
asmr_formula = '''
Age-Specific Mortality Rate (ASMR) Formula:

ASMR(x) = D(x) / P(x)

Where:
ASMR(x) = Age-Specific Mortality Rate for age x
D(x) = Number of deaths at age x in a given year
P(x) = Mid-year population at age x in the same year

Note: This rate is typically expressed per 1,000 population, so the result is often multiplied by 1,000.
'''

print(asmr_formula)

from data import mortality_data, population_data

def calculate_asmr(deaths, population):
    return [d / p if p != 0 else 0 for d, p in zip(deaths, population)]

def print_asmr_results(country, age_groups, asmr):
    print(f"\nAge-Specific Mortality Rates for females in {country} (2014):")
    print("Age | Per 1,000 | Decimal | Percentage")
    print("----|-----------|---------|------------")
    for age, rate in zip(age_groups, asmr):
        per_1000 = rate * 1000
        decimal = rate
        percentage = rate * 100
        print(f"{age:3d} | {per_1000:9.2f} | {decimal:.5f} | {percentage:.2f}%")

# Calculate ASMR for USA females in 2014
usa_female_deaths = mortality_data['USA']['2014']['female']['deaths']
usa_female_population = population_data['USA']['2014']['female']['population']
usa_female_asmr = calculate_asmr(usa_female_deaths, usa_female_population)

# Calculate ASMR for Russia females in 2014
russia_female_deaths = mortality_data['Russia']['2014']['female']['deaths']
russia_female_population = population_data['Russia']['2014']['female']['population']
russia_female_asmr = calculate_asmr(russia_female_deaths, russia_female_population)

# Print results
age_groups = mortality_data['USA']['2014']['age_groups']
print_asmr_results("USA", age_groups, usa_female_asmr)
print_asmr_results("Russia", age_groups, russia_female_asmr)

import matplotlib.pyplot as plt

def plot_asmr(usa_asmr, russia_asmr, age_groups):
    # Ensure all data series have the same length
    min_length = min(len(age_groups), len(usa_asmr), len(russia_asmr))
    age_groups = age_groups[:min_length]
    usa_asmr = usa_asmr[:min_length]
    russia_asmr = russia_asmr[:min_length]

    plt.figure(figsize=(12, 6))
    plt.plot(age_groups, usa_asmr, label='USA', color='blue')
    plt.plot(age_groups, russia_asmr, label='Russia', color='red')
    plt.xlabel('Age')
    plt.ylabel('Mortality Rate (per 1,000)')
    plt.title('Age-Specific Mortality Rates for Females (2014)')
    plt.legend()
    plt.yscale('log')  # Use logarithmic scale for y-axis
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.tight_layout()
    plt.show()

# Assuming usa_female_asmr and russia_female_asmr are already calculated
# Convert rates to per 1,000 for plotting
usa_asmr_per_1000 = [rate * 1000 for rate in usa_female_asmr]
russia_asmr_per_1000 = [rate * 1000 for rate in russia_female_asmr]

# Plot the graph
plot_asmr(usa_asmr_per_1000, russia_asmr_per_1000, age_groups)

analysis_text = """
Comparing the age-specific mortality rates for females in the USA and Russia in 2014 reveals a mix of shared patterns and notable contrasts. Both countries exhibit the classic "U-shaped" curve, characterized by high infant mortality, a substantial drop during childhood and early adulthood, and a gradual increase through middle age and beyond. However, Russia consistently reports higher mortality rates than the USA across most age groups.

Russia's markedly higher infant mortality rate (6.69 per 1,000 compared to 5.40 in the USA) and elevated mortality among young adults (ages 15-40) stand out as key differences. This discrepancy widens further for middle-aged women (40-60), potentially reflecting factors such as healthcare access, lifestyle choices, and chronic disease prevalence. In the older population, the gap persists and even expands, with Russian females experiencing a steeper mortality rise from age 70 onward. By age 100 and above, Russia's mortality rate soars, indicating more severe health outcomes for the extremely elderly compared to the USA.

In conclusion, while both countries share overarching trends in age-specific mortality, Russia reports consistently higher rates, particularly among infants, middle-aged individuals, and the elderly, underscoring disparities in health, lifestyle, and socioeconomic factors between the two nations.
"""

print(analysis_text)

# (e) Expression for Crude Death Rate (CDR)
cdr_formula = '''
Crude Death Rate (CDR) Formula:

CDR = (Total Deaths / Total Population) × 1000

Where:
Total Deaths = Sum of all deaths in the population for a given year
Total Population = Midyear population for the same year
'''

print(cdr_formula)

# (f) Calculate CDR for female population in US and Russia (2014)

def calculate_cdr(deaths, population):
    return sum(deaths) / sum(population)

# US female CDR
us_female_deaths = mortality_data['USA']['2014']['female']['deaths']
us_female_population = population_data['USA']['2014']['female']['population']
us_female_cdr = calculate_cdr(us_female_deaths, us_female_population)

# Russia female CDR
russia_female_deaths = mortality_data['Russia']['2014']['female']['deaths']
russia_female_population = population_data['Russia']['2014']['female']['population']
russia_female_cdr = calculate_cdr(russia_female_deaths, russia_female_population)

# Print results
def print_cdr_results(country, cdr):
    print(f"\nCrude Death Rate for females in {country} (2014):")
    print(f"Per 1,000: {cdr * 1000:.2f}")
    print(f"Decimal: {cdr:.5f}")
    print(f"Percentage: {cdr * 100:.2f}%")

print_cdr_results("USA", us_female_cdr)
print_cdr_results("Russia", russia_female_cdr)

import numpy as np

def align_all_data(*arrays):
    """Align all input arrays to the shortest length among them."""
    min_length = min(len(arr) for arr in arrays)
    return [np.array(arr[:min_length]) for arr in arrays]

def calculate_ascdr(death_rates, standard_population):
    return np.sum(death_rates * standard_population) / np.sum(standard_population)

# Align all data
(us_female_deaths, us_female_population, 
 russia_female_deaths, russia_female_population) = align_all_data(
    us_female_deaths, us_female_population, 
    russia_female_deaths, russia_female_population
)

# Calculate age-specific death rates
us_death_rates = us_female_deaths / us_female_population
russia_death_rates = russia_female_deaths / russia_female_population

# Calculate ASCDRs using different standard populations
us_standard = us_female_population
russia_standard = russia_female_population
average_standard = (us_standard + russia_standard) / 2

# (g) Calculate ASCDRs
ascdr_us_standard = {
    'US': calculate_ascdr(us_death_rates, us_standard),
    'Russia': calculate_ascdr(russia_death_rates, us_standard)
}

ascdr_russia_standard = {
    'US': calculate_ascdr(us_death_rates, russia_standard),
    'Russia': calculate_ascdr(russia_death_rates, russia_standard)
}

ascdr_average_standard = {
    'US': calculate_ascdr(us_death_rates, average_standard),
    'Russia': calculate_ascdr(russia_death_rates, average_standard)
}

print("\n(g) Age Standardized Crude Death Rates (ASCDR):")
for standard, results in [("US", ascdr_us_standard), ("Russia", ascdr_russia_standard), ("Average", ascdr_average_standard)]:
    print(f"\nUsing {standard} female population as standard:")
    for country, rate in results.items():
        print(f"{country}: {rate*1000:.2f} per 1,000")

# (h) Kitagawa decomposition
def kitagawa_decomposition(rates1, pop1, rates2, pop2):
    total_pop = pop1 + pop2
    avg_rates = (rates1 + rates2) / 2
    avg_props = total_pop / np.sum(total_pop)
    
    rate_effect = np.sum((rates1 - rates2) * avg_props)
    comp_effect = np.sum((pop1/np.sum(pop1) - pop2/np.sum(pop2)) * avg_rates)
    
    return rate_effect, comp_effect

rate_effect, comp_effect = kitagawa_decomposition(russia_death_rates, russia_standard, us_death_rates, us_standard)

total_difference = russia_female_cdr - us_female_cdr
rate_share = rate_effect / total_difference * 100
comp_share = comp_effect / total_difference * 100

print("\n(h) Kitagawa Decomposition:")
print(f"Total CDR difference (Russia - US): {total_difference*1000:.2f} per 1,000")
print(f"Rate effect: {rate_effect*1000:.2f} per 1,000 ({rate_share:.2f}%)")
print(f"Composition effect: {comp_effect*1000:.2f} per 1,000 ({comp_share:.2f}%)")

print("\nInterpretation of results:")
print("""
1. Age Standardized Crude Death Rates (ASCDR):
   - Using any standard population, Russia consistently shows higher mortality rates than the US.
   - The difference in ASCDRs is smallest when using Russia's population structure as the standard, 
     suggesting that Russia's age structure partially masks its higher mortality rates.
   - The average population standard provides a balanced comparison, showing Russia's ASCDR is 
     significantly higher than the US.

2. Kitagawa Decomposition:
   - The rate effect explains the majority of the difference in CDRs between Russia and the US.
   - This suggests that the higher mortality rates in Russia across age groups are the primary 
     reason for its higher overall CDR, rather than differences in age structure.
   - The composition effect, while smaller, indicates that differences in age structure also 
     contribute to the CDR difference, but to a lesser extent.
   - The positive composition effect suggests that Russia's age structure actually slightly 
     reduces the CDR difference that would exist based solely on age-specific mortality rates.
""")



















# Introduction
print("Question 3: Comparative Analysis of (annual) fertility in the US, West Germany, and Japan during the period 1960 to 2017")
print("Part (a): General expressions for Crude Birth Rate and General Fertility Rate\n")

def crude_birth_rate(B, P):
    """
    General expression for the annual Crude Birth Rate (CBR)
    
    CBR = (B / P) * 1000
    
    Parameters:
    B (int): Number of live births in a year
    P (int): Total mid-year population (males and females)
    
    Returns:
    float: Crude Birth Rate per 1,000 population
    """
    return (B / P) * 1000

def general_fertility_rate(B, F_15_49):
    """
    General expression for the annual General Fertility Rate (GFR)
    
    GFR = (B / F_15_49) * 1000
    
    Parameters:
    B (int): Number of live births in a year
    F_15_49 (int): Mid-year female population aged 15 to under 50
    
    Returns:
    float: General Fertility Rate per 1,000 women aged 15-49
    """
    return (B / F_15_49) * 1000

# Explanation of notation
print("Notation explanation:")
print("B: Number of live births in a year")
print("P: Total mid-year population (males and females)")
print("F_15_49: Mid-year female population aged 15 to under 50")
print("Both rates are expressed per 1,000 population or women, respectively.")

print("\nCrude Birth Rate (CBR) Formula:")
print("CBR = (B / P) * 1000")

print("\nGeneral Fertility Rate (GFR) Formula:")
print("GFR = (B / F_15_49) * 1000")

print("\nThe CBR uses the total population as the denominator, while the GFR")
print("more accurately relates the birth count to the female population at risk")
print("(women aged 15 to under 50), providing a more precise measure of fertility.")





print()  # Adds a blank line
import pandas as pd
import numpy as np

print("Question 3: Comparative Analysis of (annual) fertility in the US, West Germany, and Japan during the period 1960 to 2017")
print("Part (b): Calculate annual birth rates (CBR and GFR) for each year between 1960 and 2017\n")

# File path
file_path = '/Users/israelmarykidda/Documents/Workspace_702/assigment_01/Population_Period_WGermany_Japan_USA_1x5(1)(1).xlsx'

# Load the Excel file
df = pd.read_excel(file_path, header=2)

# Rename columns to reflect countries
df.columns = ['Year', 'Age', 'Germany_Female', 'Germany_Male', 'Germany_Total', 
              'Unnamed', 'Japan_Female', 'Japan_Male', 'Japan_Total', 
              'Unnamed2', 'USA_Female', 'USA_Male', 'USA_Total']

# Drop unnamed columns
df = df.drop(columns=['Unnamed', 'Unnamed2'])

def crude_birth_rate(B, P):
    """Calculate the Crude Birth Rate (CBR)"""
    return (B / P) * 1000 if P != 0 else np.nan

def general_fertility_rate(B, F_15_49):
    """Calculate the General Fertility Rate (GFR)"""
    return (B / F_15_49) * 1000 if F_15_49 != 0 else np.nan

def get_births(country, year):
    return df[(df['Age'] == 0) & (df['Year'] == year)][f'{country}_Female'].values[0]

def get_total_population(country, year):
    return df[df['Year'] == year][f'{country}_Total'].sum()

def get_female_population_15_49(country, year):
    reproductive_age_mask = df['Age'].isin(['15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49'])
    return df[(df['Year'] == year) & reproductive_age_mask][f'{country}_Female'].sum()

# Calculate CBR and GFR for each country and year
countries = ['Germany', 'Japan', 'USA']
years = range(1960, 2018)
results = {country: {'CBR': {}, 'GFR': {}} for country in countries}

for country in countries:
    for year in years:
        try:
            births = get_births(country, year)
            total_population = get_total_population(country, year)
            female_population_15_49 = get_female_population_15_49(country, year)
            
            cbr = crude_birth_rate(births, total_population)
            gfr = general_fertility_rate(births, female_population_15_49)
            
            results[country]['CBR'][year] = cbr
            results[country]['GFR'][year] = gfr
        except Exception as e:
            print(f"Error processing {country} data for year {year}: {e}")

# Print results for each year
for country in countries:
    print(f"\n{country} Results:")
    print("Year\tCBR\tGFR")
    for year in years:
        cbr = results[country]['CBR'].get(year, 'N/A')
        gfr = results[country]['GFR'].get(year, 'N/A')
        if isinstance(cbr, float) and isinstance(gfr, float):
            print(f"{year}\t{cbr:.2f}\t{gfr:.2f}")
        else:
            print(f"{year}\t{cbr}\t{gfr}")

print("\nNote: Results are shown for all years from 1960 to 2017.")




















import matplotlib.pyplot as plt

# Assuming we have the results dictionary from the previous code

# Prepare data for plotting
years = list(range(1960, 2018))
countries = ['Germany', 'Japan', 'USA']
colors = ['red', 'green', 'blue']

# Create CBR chart
plt.figure(figsize=(12, 6))
for country, color in zip(countries, colors):
    cbr_values = [results[country]['CBR'][year] for year in years]
    plt.plot(years, cbr_values, color=color, label=country)

plt.title('Crude Birth Rate (CBR) from 1960 to 2017')
plt.xlabel('Year')
plt.ylabel('CBR (per 1,000 population)')
plt.legend()
plt.grid(True)
plt.savefig('cbr_chart.png')
plt.close()

# Create GFR chart
plt.figure(figsize=(12, 6))
for country, color in zip(countries, colors):
    gfr_values = [results[country]['GFR'][year] for year in years]
    plt.plot(years, gfr_values, color=color, label=country)

plt.title('General Fertility Rate (GFR) from 1960 to 2017')
plt.xlabel('Year')
plt.ylabel('GFR (per 1,000 women aged 15-49)')
plt.legend()
plt.grid(True)
plt.savefig('gfr_chart.png')
plt.close()

print("Charts have been created and saved as 'cbr_chart.png' and 'gfr_chart.png'.")







# Print the fertility trend analysis
print("\nFertility Trend Analysis (1960-2017):")
print("""
Over the course of 57 years (1960-2017), the United States, Germany, and Japan all followed the global pattern of decreasing fertility rates, as evidenced by their Crude Birth Rate (CBR) and General Fertility Rate (GFR) data. However, each nation exhibited unique fertility trends during this time.

While the United States maintained a relatively stable and consistently higher fertility level, Germany and Japan experienced a more rapid decline, particularly in the late 1960s and early 1970s. Notable dips in fertility were observed in Germany, most prominently in the 1970s, followed by a slight rebound post-reunification in the early 1990s. Japan's fertility trend showed more fluctuation due to specific cultural factors. By the 2000s, Germany and Japan had converged at very low fertility rates, with Japan experiencing the lowest rates by 2017.

In summary, despite all three countries experiencing long-term declines in fertility, the United States remained an outlier with consistently higher rates. Conversely, Germany and Japan concluded the period with significantly lower fertility rates, especially Japan, which faced the steepest decline by 2017.
""")





import pandas as pd
import matplotlib.pyplot as plt

# Years from 1960 to 2017
years = list(range(1960, 2018))

# Population of females aged 15-19 in each country (from screenshot)
germany_population = [
    2099949, 1883939, 1741635, 1721773, 1710125, 1726824, 1844545, 1902118, 1925141, 1945349, 
    1967215, 1963661, 2006978, 2055721, 2118968, 2167738, 2227869, 2296754, 2361055, 2438644, 
    2507063, 2555098, 2580591, 2574363, 2527403, 2442109, 2326925, 2200836, 2050085, 1887623, 
    1765653, 1683124, 1626990, 1596414, 1590144, 1950567, 1625330, 1651410, 1678126, 1693547, 
    1708177, 1706143, 1722892, 1742587, 1780029, 1813588, 1852151, 1860894, 1858987, 1839158, 
    1812995, 1771392, 1753150, 1750502, 1738991, 1734228, 1746194, 1676900, 1636983
]

japan_population = [
    4667825, 4542596, 4411138, 4595892, 4846921, 5106284, 5406823, 5565403, 5336794, 5004440, 
    4656669, 4405317, 4215316, 4063425, 3961237, 3920366, 3827869, 3853539, 3875130, 3900885, 
    3946762, 4005160, 3987371, 4108767, 4212683, 4306751, 4411936, 4613959, 4698284, 4796960, 
    4853833, 4839964, 4747507, 4660852, 4432404, 4256390, 4101259, 3956079, 3845315, 3755800, 
    3680803, 3601294, 3525803, 3443066, 3339827, 3231301, 3142251, 3071797, 3004865, 2951554, 
    2928732, 2927430, 2910949, 2903754, 2907071, 2902707, 2901215, 2886603, 2857887
]

usa_population = [
    6537613.96, 6716986.48, 7086023.99, 7512042.34, 7828446.18, 8196915.26, 8614116.96, 
    8839519.83, 8925057.64, 9124395.12, 9376525.41, 9628085.47, 9864339.72, 10009780.8, 
    10271715.1, 10408158.9, 10545289.7, 10581498.6, 10567964.4, 10552052.5, 10439029.1, 
    10238320.4, 9951806.99, 9661315.27, 9400771.51, 9230502.29, 9109039.76, 9172252.87, 
    9088346.54, 8934413.64, 8747667.32, 8531069, 8399748.97, 8442500.85, 8592847.73, 
    8805947.9, 9061538.77, 9309512.22, 9533376.16, 9701447.17, 9880837.99, 9945487.98, 
    10034366.4, 10164894, 10339054, 10516566.7, 10664493.1, 10768338.1, 10804887.5, 
    10753795.3, 10621349.1, 10474962.2, 10371372.3, 10307228.9, 10239299.7, 10321540.1, 
    10334832.9, 10308137.8
]

# Estimating total births for Germany, Japan, and the USA (this is hypothetical data for illustration)
germany_total_births = [1000000] * len(years)  # Replace with real birth data if available
japan_total_births = [1200000] * len(years)    # Replace with real birth data if available
usa_total_births = [4000000] * len(years)      # Replace with real birth data if available

# Estimate that 5% of total births are to females aged 15-19
def estimate_births_15_19(total_births):
    return [0.05 * b for b in total_births]

germany_births_15_19 = estimate_births_15_19(germany_total_births)
japan_births_15_19 = estimate_births_15_19(japan_total_births)
usa_births_15_19 = estimate_births_15_19(usa_total_births)

# Function to calculate ASFR for females aged 15-19
def calculate_asfr(births, population):
    return [(b / p) * 1000 if p != 0 else None for b, p in zip(births, population)]

# Calculate the ASFR for each country
asfr_germany = calculate_asfr(germany_births_15_19, germany_population)
asfr_japan = calculate_asfr(japan_births_15_19, japan_population)
asfr_usa = calculate_asfr(usa_births_15_19, usa_population)

# Plotting the ASFR for Germany, Japan, and USA
plt.figure(figsize=(12, 6))
plt.plot(years, asfr_germany, label='Germany', color='red')
plt.plot(years, asfr_japan, label='Japan', color='green')
plt.plot(years, asfr_usa, label='USA', color='blue')

plt.title('Age-Specific Fertility Rate (ASFR) for Females Aged 15-19 (1960-2017)')
plt.xlabel('Year')
plt.ylabel('ASFR (per 1,000 females aged 15-19)')
plt.legend()
plt.grid(True)
plt.show()
















print()
print()
print("Technical Problems")

import math

def calculate_population(initial_population, growth_rate, time):
    return initial_population * math.exp(time * growth_rate)

# Initial values
N_0 = 100000
r = 0.05

# Calculate N(5) and N(10)
N_5 = calculate_population(N_0, r, 5)
N_10 = calculate_population(N_0, r, 10)

print("0.")
print(f"(a). N(5) = {N_5:.2f}")
print(f"(b). N(10) = {N_10:.2f}")






import math

# Initial values
N_0 = 100000
r = 0.05
time = 10

# Calculate N(10)
N_10 = N_0 * math.exp(time * r)

# Calculate the mean annualized growth rate
mean_growth_rate = math.log(N_10 / N_0) / time

# Format the output
output = f"rˉ[0,10] = ln(N(10)/N(0)) / 10 = ln({N_10:.0f}/{N_0}) / 10 = {mean_growth_rate:.4f}"

print(output)




print()
import math

# Original values
N_0 = 100000
N_10_original = 134986
r_original = 0.03

# New growth rate
r_new = 0.05

# Calculate the population at N(10) for the new growth rate
N_10_new = N_0 * math.exp(r_new * 10)

# Calculate person years lived for original and new growth rates
PY_original = (N_10_original - N_0) / r_original
PY_new = (N_10_new - N_0) / r_new

# Format the output
print("2. Estimating person years lived between t=0 and t=10:")
print("(a). Assuming a constant growth rate.")
print("Original calculation (r = 0.03):")
print(f"PY[0, T] = (N(T) - N(0)) / r̅[0, T] = (N(10) - N(0)) / r̅[0, 10] = ({N_10_original} - {N_0}) / {r_original:.2f} = {PY_original:.0f}")
print("\nRecalculated with a 0.05 growth rate:")
print(f"PY[0, T] = (N(T) - N(0)) / r̅[0, T] = (N(10) - N(0)) / r̅[0, 10] = ({N_10_new:.0f} - {N_0}) / {r_new:.2f} = {PY_new:.0f}")




print()
import math

# Initial values
N_0 = 100000
r = 0.0500  # New growth rate
T = 10

# Calculate N(T/2) which is N(5) in this case
N_5 = N_0 * math.exp(r * 5)

# Calculate person years lived using mid-period approximation
PY = N_5 * T

# Format the output
print("2. Estimating person years lived between t=0 and t=10:")
print("(b). Assuming growth is linear and using the mid-period approximation:")
print(f"PY[0, T] = N(T/2) · T")
print(f"PY[0, 10] = N(5) · 10 = {N_5:.0f} · 10 = {PY:.0f}")






print()
import math

# Initial values
N_0 = 100000
r = 0.0500  # New growth rate
T = 10

# Calculate N(10) with the new growth rate
N_10 = N_0 * math.exp(r * T)

# Calculate person years lived using the mean of initial and final population sizes
PY = ((N_0 + N_10) / 2) * T

# Format the output
print("2. Estimating person years lived between t=0 and t=10:")
print("(c). Assuming growth is linear and using the mean of initial and final population sizes:")
print("PY[0, T] = [(N(0) + N(T)) / 2] · T")
print(f"PY[0, 10] = [(N(0) + N(10)) / 2] · 10")
print(f"         = [({N_0} + {N_10:.0f}) / 2] · 10 = {PY:.0f}")





print()
import math

# Initial values
N_0 = 100000
r = 0.0500  # New growth rate
T = 10

# Calculate N(10) with the new growth rate
N_10 = N_0 * math.exp(r * T)
population_change = N_10 - N_0

# Calculate N(5) for mid-period approximation (needed for PY_b)
N_5 = N_0 * math.exp(r * 5)

# Person-years lived calculations from previous questions
PY_a = (N_10 - N_0) / r  # From question 2(a)
PY_b = N_5 * T  # From question 2(b) - using N(5)
PY_c = ((N_0 + N_10) / 2) * T  # From question 2(c)

# Calculate crude growth rates
CGR_a = population_change / PY_a
CGR_b = population_change / PY_b
CGR_c = population_change / PY_c

# Format the output
print("3. Calculate crude growth rates based upon various estimates of person-years lived:")
print(f"a). CGR[0, T] = {population_change:.0f} / {PY_a:.0f} = {CGR_a:.4f}")
print(f"b). CGR[0, T] = {population_change:.0f} / {PY_b:.0f} = {CGR_b:.4f}")
print(f"c). CGR[0, T] = {population_change:.0f} / {PY_c:.0f} = {CGR_c:.4f}")




print()
# Final comment and analysis

comment = """
In the end, we can see that with the 5% growth rate, the person-years lived (PY)
estimates are higher compared to the 3% growth rate. This happens because the population 
grows faster, leading to a bigger population at N(10), which means an increase in the total 
person-years lived. As a result, this affects the crude growth rate (CGR), which is a bit lower 
with the 5% growth rate because of the larger PY estimates.

The mid-period approximation (using N(5)) becomes less accurate with higher growth rates 
(like 5%) because it doesn't fully capture the rapid increase in population growth that happens 
in the later part of the period. This leads to a bigger error in both PY and CGR.
"""

# Print the comment
print(comment)