months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = int(input("Enter a month number: "))
month = months[(n - 1) * 3:(n - 1) * 3+ 3]
print(month)
