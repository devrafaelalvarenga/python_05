def csv_reader(path: str) -> list:
    """
    Faz a leitura do arquivo csv 
    Transforma dados em um dicionario
    Armazena s dados em uma lista

    Args:
        path (str): caminho do arquivo csv

    Returns:
        list: retorno da função. Uma lista com dicionarios
    """
    import csv
    covid_data: list = list()

    with open(file=path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(f=csv_file, delimiter=';')

        for l in csv_reader:
            covid_data.append(l)

    return covid_data


print(csv_reader(path='arquivo.csv'))
