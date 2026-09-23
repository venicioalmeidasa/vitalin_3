divisao_conselho:dict[str,int] = {
            'crm': 600,
            'COREN': 2000,
            'CRP': 300,
            'CRO': 200,
            'CRN': 200,
            'CREFITO': 1000,
            'CRF': 200,
            'CRBM': 100,
            'CRBio': 100,
            'CREF': 100,
            'CRESS': 500,
            'CRMV': 200,
            'CREFONO': 500
        } 
cont = 0
for chave in divisao_conselho:
    cont += divisao_conselho[chave]

print(cont)
