# taking an empty variable
sum_series = 0

for n in range(1, 9):
    term = n / (n+1)*(n+2)
    sum_series += term

print(f"Sum of the series is = {sum_series:.5f}")