dep = float(input("Qual o valor do depósito inicial (em R$)? " ))
taxa = float(input("Qual a taxa de juros da poupança (em %)? "))

taxa_dec = taxa / 100

saldo = dep
total_juros = 0

print("\n" + "="*50)
print(f"{'Mês':<6} {'Saldo (R$)':<15} {'Juros no mês (R$)':<18}")
print("="*50)

for mes in range(1, 25):
    juros_mes = saldo * taxa_dec
    total_juros += juros_mes
    
    saldo += juros_mes
    
    print(f"{mes:<6} R$ {saldo:>11.2f}    R$ {juros_mes:>11.2f}")

print("="*50)
print(f"\n--- RESUMO FINAL ---")
print(f"Depósito inicial: R$ {deposito_inicial:.2f}")
print(f"Taxa de juros: {taxa_juros}% ao mês")
print(f"Saldo final após 24 meses: R$ {saldo:.2f}")
print(f"Total ganho com juros: R$ {total_juros:.2f}")
print(f"Rendimento total: {(total_juros/deposito_inicial)*100:.1f}%")

