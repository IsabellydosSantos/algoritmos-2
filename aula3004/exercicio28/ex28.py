def analisar_vendas(nome_arquivo):
    try:
        vendas_vendedor = {}
        vendas_produto = {}
        
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                
                campos = linha.split()
                vendedor = campos[0]
                produto = campos[1]
                valor = float(campos[2])
                
                if vendedor in vendas_vendedor:
                    vendas_vendedor[vendedor] += valor
                else:
                    vendas_vendedor[vendedor] = valor
                
                if produto in vendas_produto:
                    vendas_produto[produto] += valor
                else:
                    vendas_produto[produto] = valor
        
        linhas_relatorio = []
        
        linhas_relatorio.append("Relatório de vendas")
        
        linhas_relatorio.append("\n Total por vendedor:")
        for vendedor, total in vendas_vendedor.items():
            linhas_relatorio.append(f"{vendedor}: R$ {total:.2f}")
        
        linhas_relatorio.append("\n Total por produto:")
        for produto, total in vendas_produto.items():
            linhas_relatorio.append(f"{produto}: R$ {total:.2f}")
        
        linhas_relatorio.append("\n Vendedor do mês:")
        vendedor_top = max(vendas_vendedor, key=vendas_vendedor.get)
        valor_top = vendas_vendedor[vendedor_top]
        linhas_relatorio.append(f"{vendedor_top} com R$ {valor_top:.2f}")
        
        linhas_relatorio.append("\n Produto mais vendido:")
        produto_top = max(vendas_produto, key=vendas_produto.get)
        valor_produto_top = vendas_produto[produto_top]
        linhas_relatorio.append(f"{produto_top} com R$ {valor_produto_top:.2f}")
        
        print("\n".join(linhas_relatorio))
        
        with open("relatorio.txt", "w", encoding='utf-8') as relatorio:
            relatorio.write("\n".join(linhas_relatorio))
        
        print("\n Relatório salvo em 'relatorio.txt'")
        
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado")
    except ValueError as e:
        print(f"Erro: Valor inválido no arquivo - {e}")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")


print("Sistema de análise de vendas \n")
analisar_vendas("vendas.txt")
