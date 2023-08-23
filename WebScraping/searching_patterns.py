import re


def find_publications(content, sec_index, year):

    if int(year) <= 2017:
        pattern = re.compile(
            r'[0-9]{2}[ ][0-9]{6}[ ]-[ ][0-9]')
    else:
        pattern = re.compile(
            r'[0-9]{2}[ ][0-9]{7}[ ].*?[0-9]')

    publication_list = []
    for p in pattern.finditer(content):
        publication_list.append(p)

    n_publications = len(publication_list)

    return publication_list, n_publications


def sec_pattern():
    search_pattern = []

    search_pattern.append(
        'Secretaria de Estado do Meio Ambiente e do Desenvolvimento Sustentável')
    search_pattern.append(
        'Secretaria de Estado de Meio Ambiente e Desenvolvimento Sustentável')
    search_pattern.append(
        'Secretaria de Estado do Meio Ambiente e do desenvolvimento Sustentável')
    search_pattern.append(
        'Secretaria de Estado do meio Ambiente e do Desenvolvimento Sustentável')
    search_pattern.append(
        'Secretaria de Estado de meio Ambiente e Desenvolvimento Sustentável')

    return search_pattern


def match_pattern(page, patterns):

    for i, pattern in enumerate(patterns):
        if page.find(pattern) != -1:
            sec_index = page.find(pattern)
            return pattern, i, sec_index

    return 'failed', i, -1
