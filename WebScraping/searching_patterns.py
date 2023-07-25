

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
            return pattern, i

    return 'failed', i
