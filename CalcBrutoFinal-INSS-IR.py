n1 = float(input("Digite o salario: "))

print("Salário bruto: R$", n1)

if n1>= 0 and n1 <= 1710.48:
    imp = 0
    print("sem imposto")
elif n1 > 1710.48 and n1 <= 2563.91:
    imp = n1 * 0.075 - 142.80
    print(f"imposto a ser pago: R${imp:8.2f}")
elif n1 > 2563.91 and n1 <= 3418.59:
    imp = n1 * 0.15 - 354.80
    print(f"imposto a ser pago: R${imp:8.2f}")
elif n1 > 3418.59 and n1 <= 4271.59:
    imp = n1 * 0.225 - 636.13
    print(f"imposto a ser pago: R${imp:8.2f}")
elif n1 > 4271.59:
    imp = n1 * 0.275 - 869.36
    print(f"imposto a ser pago: R${imp:8.2f}")
else:
    print("Numero invalido.")


if n1 >= 0 and n1 <= 1247.70:
    inss = n1 * 0.08
    print(f"valor do inss: R${inss:8.2f}")
elif n1 > 1247.70 and n1 <= 2079.50:
    inss = n1 * 0.09
    print(f"valor do inss: R${inss:8.2f}")
elif n1 > 2079.50 and n1 <= 4159:
    inss = n1 * 0.11
    print(f"valor do inss: R${inss:8.2f}")
else:
    inss = 468
    print(f"valor do inss: R${inss:8.2f}")

meudeus = n1 - imp - inss

print("Salário líquido: R$", meudeus)
