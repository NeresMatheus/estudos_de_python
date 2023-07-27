import re


def find_publication(content, sec_index):

    pattern = re.compile(
        r'[0-9]{2}[ ][0-9]{7}[ ].*?[0-9]|[0-9]{2}[ ][0-9]{6}[ ]-[ ][0-9]')

    publiation_list = [p for p in pattern.finditer(content)]
    n_publications = len(publiation_list)

    return publiation_list, n_publications


...


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
            return pattern, i, page.find(pattern)

    return 'failed', i, -1
