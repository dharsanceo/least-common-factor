a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
for i in range(max(a, b), a * b + 1):
    if i % a == 0 and i % b == 0:
        print("LCM =", i)
        break
