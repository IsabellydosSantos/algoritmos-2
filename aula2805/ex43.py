n = int(input("Insira a quantidade de números: "))
nums = [int(input(f"{i+1}° Número: ")) for i in range(n)]

cont = [0, 0, 0, 0]

for num in nums:
    if 0 <= num <= 25:
        cont[0] += 1
    elif 26 <= num <= 50:
        cont[1] += 1
    elif 51 <= num <= 75:
        cont[2] += 1
    elif 76 <= num <= 100:
        cont[3] += 1

print(f"[0,25]: {cont[0]}")
print(f"[26,50]: {cont[1]}")
print(f"[51,75]: {cont[2]}")
print(f"[76,100]: {cont[3]}")
