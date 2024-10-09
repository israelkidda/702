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
