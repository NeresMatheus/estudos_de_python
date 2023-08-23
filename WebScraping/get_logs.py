def make_meta_log(pdf_file, meta):
    with open('meta_log.txt', 'a') as f:
        f.write(pdf_file+'\n')
        f.write(str(meta.author)+'\n')
        f.write(str(meta.creator)+'\n')
        f.write(str(meta.producer)+'\n')
        f.write(str(meta.subject)+'\n')
        f.write(str(meta.title)+'\n'+'\n')


def make_pattern_log(pdf_file, init_position, end_position, content_first_page,
                     content_last_page, first_page):

    with open('finding_pattern_log.txt', 'a', encoding="utf-8") as f:
        log = '\n' + pdf_file
        log += '\nposição inicial: ' + content_first_page
        log += '\nposição final: ' + content_last_page
        log += '\nconteudo: ' + first_page[init_position:end_position] + '\n'
        f.write(log)

    return


def make_fPage_log(pdf_file, flag, end_position, first_page):
    if flag == 0:
        with open('first_page_log.txt', 'a', encoding="utf-8") as f:
            f.write('\n')

    if pdf_file != '':
        with open('first_page_log.txt', 'a', encoding="utf-8") as f:
            f.write('\n' + pdf_file + '\n')

    if flag == 1:
        with open('first_page_log.txt', 'a', encoding="utf-8") as f:
            f.write(first_page[end_position])
    return


def make_lPage_log(pdf_file, flag, end_position, first_page):
    if flag == 0:
        with open('last_page_log.txt', 'a', encoding="utf-8") as f:
            f.write('\n')

    if pdf_file != '':
        with open('last_page_log.txt', 'a', encoding="utf-8") as f:
            f.write('\n' + pdf_file + '\n')

    if flag == 1:
        with open('last_page_log.txt', 'a', encoding="utf-8") as f:
            f.write(first_page[end_position])
    return


def publication_log(txt_file, pucliation_list, content):
    with open('re_teste.txt', 'a', encoding='utf-8') as f:
        log = '\n\t----' + txt_file
        for p in pucliation_list:
            log += "\nposição: " + str(p.start())
            log += "\nconteudo: " + p.group()
            log += "\nconteudo: " + content[p.start()-3:p.start()+15] + '\n'
            f.write(log)
            log = ''

    return


def txt_pattern_log(txt_file, result, n_publications):
    with open('txt_pattern_log.txt', 'a', encoding="utf-8") as f:

        log = '\n' + txt_file
        log += '\nresultado: ' + result
        log += '\nnº de publicações: ' + str(n_publications) + '\n'
        f.write(log)

    return
