def status(nota):
    if nota >= 6:
        return "Aprovado"
    elif nota >= 4:
        return "Verificação Suplementar"
    else:
        return "Reprovado"
    
notas = [5, 7.5, 8.3, 9, 3, 4]
for nota in notas:
    res = status(nota)
    print(f"Nota: {nota} - {res}")