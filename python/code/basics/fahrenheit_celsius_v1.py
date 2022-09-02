lower = 0
upper = 300
step = 20

print(f"Fahrenheit Celsius")
print(f"---------- -------")
fahr = lower
while fahr <= upper:
    celsius = 5 * (fahr - 32) / 9
    print(f"{fahr:<10} {celsius:>7.1f}")
    fahr = fahr + step
