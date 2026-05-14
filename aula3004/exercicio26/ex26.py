def processar_notas(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            estudantes = []
            
            for linha in arquivo:
                linha = linha.strip()
                if linha:  
                    partes = linha.split()
                    nome = partes[0]
                    notas = [float(nota) for nota in partes[1:]]  
                    estudantes.append({'nome': nome, 'notas': notas})
        
        if not estudantes:
            print("Nenhum estudante encontrado no arquivo")
            return
        
        print("Relatório das notas dos estudantes")
        
        print("\n Estudantes com mais de 6 notas:")
        estudantes_mais_6 = [e for e in estudantes if len(e['notas']) > 6]
        
        if estudantes_mais_6:
            for e in estudantes_mais_6:
                print(f"  • {e['nome']} - {len(e['notas'])} notas")
        else:
            print("Nenhum estudante tem mais de 6 notas")
        
        print("\n Média de cada estudante:")
        for e in estudantes:
            media = sum(e['notas']) / len(e['notas'])
            print(f"  • {e['nome']}: {media:.2f}")
        
        print("\n Nota mínima:")
        nota_minima = float('inf')
        estudante_minimo = None
        
        for e in estudantes:
            min_estudante = min(e['notas'])
            if min_estudante < nota_minima:
                nota_minima = min_estudante
                estudante_minimo = e['nome']
        
        print(f" Estudante: {estudante_minimo}")
        print(f" Nota mínima: {nota_minima}")
        
        # 4. Nota máxima e estudante
        print("\n Nota máxima:")
        nota_maxima = float('-inf')
        estudante_maximo = None
        
        for e in estudantes:
            max_estudante = max(e['notas'])
            if max_estudante > nota_maxima:
                nota_maxima = max_estudante
                estudante_maximo = e['nome']
        
        print(f" Estudante: {estudante_maximo}")
        print(f" Nota máxima: {nota_maxima}")
        
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")


print("Sistema de análise de notas\n")
processar_notas("notas.txt")
