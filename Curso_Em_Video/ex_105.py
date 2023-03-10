def notas(*valores, sit=False):
    """
    Armazena notas e mostra situação do aluno
    
    Args:
        sit (bool, optional): Mostra ou não a situação do aluno. Defaults to False.
        valores: inserir notas sem quantidade pré-definida
        return: retorna o dicionário com notas e situação
    """
    total_notas = valores
    media = sum(total_notas) / len(total_notas)
    dict_notas = {'maior': max(total_notas), 'menor': min(total_notas), 'total': len(total_notas), 'média': media}

    if dict_notas['média'] >= 7:
        dict_notas['situação'] = 'Boa'
    if dict_notas['média'] < 7 and dict_notas['média'] >= 6:
        dict_notas['situação'] = 'Razoável'
    else:
        dict_notas['situação'] = 'Ruim'
    if sit == False:
        del dict_notas['situação']
    return(dict_notas)
    
notas(2.5, 3.5, 4.6, sit=False)
    
    
    