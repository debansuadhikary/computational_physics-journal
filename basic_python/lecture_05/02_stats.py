# here is a list of all the modules of statistics library :

import statistics as stats

data = [2, 4, 4, 4, 5, 5, 7, 9]
data2 = [10, 20, 30, 40, 50]

print("=== Central Tendency ===")
print("Mean:", stats.mean(data))
print("fmean:", stats.fmean(data))
print("Geometric Mean:", stats.geometric_mean(data))
print("Harmonic Mean:", stats.harmonic_mean(data))
print("Median:", stats.median(data))
print("Median Low:", stats.median_low(data))
print("Median High:", stats.median_high(data))
print("Median Grouped:", stats.median_grouped(data))
print("Mode:", stats.mode(data))
print("Multimode:", stats.multimode(data))

print("\n=== Dispersion (Spread) ===")
print("Population Variance:", stats.pvariance(data))
print("Sample Variance:", stats.variance(data))
print("Population Std Dev:", stats.pstdev(data))
print("Sample Std Dev:", stats.stdev(data))

# print("\n=== Relationship ===")
# print("Covariance:", stats.covariance(data, data2))
# print("Correlation:", stats.correlation(data, data2))
# print("Linear Regression (slope, intercept):", stats.linear_regression(data, data2))

print("\n=== Other Helpers ===")
print("Quantiles (Quartiles):", stats.quantiles(data, n=4))

# Example of handling errors
try:
    print("Mode of empty list:", stats.mode([]))
except stats.StatisticsError as e:
    print("StatisticsError:", e)
