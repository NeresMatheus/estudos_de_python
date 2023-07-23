

def sec_pattern():
    search_pattern = []

    search_pattern.append(
        'Secretaria de Estado do Meio Ambiente e do Desenvolvimento Sustentável')
    search_pattern.append(
        'Secretaria de Estado de Meio Ambiente e Desenvolvimento Sustentável')
    search_pattern.append(
        'Secretaria de Estado do Meio Ambiente e do desenvolvimento Sustentável')

    return search_pattern


def match_pattern(page, patterns):

    for pattern in patterns:
        if page.find(pattern) != -1:
            searched_pattern = pattern

    return searched_pattern
