import PyPDF2
from os import listdir, chdir, getcwd
from os.path import isfile, join
from get_logs import make_pattern_log, make_fPage_log, make_lPage_log
from searching_patterns import sec_pattern, match_pattern


def get_first_page(end_position, first_page):

    caracter_postion = end_position + 1
    content_first_page = ''

    while not (first_page[caracter_postion].isalpha()):
        caracter_postion += 1
        if first_page[caracter_postion].isnumeric():
            content_first_page += first_page[caracter_postion]
            make_fPage_log('', 1, caracter_postion, first_page)

    return content_first_page, caracter_postion


def get_last_page(caracther_indice, first_page):

    while not (first_page[caracther_indice].isnumeric()):
        caracther_indice += 1

    content_last_page = ''
    while first_page[caracther_indice].isnumeric():
        content_last_page += first_page[caracther_indice]
        make_lPage_log('', 1, caracther_indice, first_page)
        caracther_indice += 1

    return content_last_page


def get_content_pages(page, pdf_file):
    """ looking in the summary on the first page for the page 
    who has the information we want"""

    first_page = page.extract_text()

    """
    search_pattern = 'Secretaria de Estado do Meio Ambiente e do Desenvolvimento Sustentável'
    if first_page.find(search_pattern) == -1:
        search_pattern = 'Secretaria de Estado de Meio Ambiente e Desenvolvimento Sustentável'
        if first_page.find(search_pattern) == -1:
            search_pattern = 'Secretaria de Estado do Meio Ambiente e do desenvolvimento Sustentável'
    """

    pattern = match_pattern(first_page, sec_pattern())

    init_position = first_page.find(pattern)
    end_position = init_position + len(pattern)

    make_fPage_log(pdf_file, 0, end_position, first_page)
    content_first_page, caracther_indice = get_first_page(
        end_position, first_page)

    make_lPage_log(pdf_file, 0, end_position, first_page)
    content_last_page = get_last_page(caracther_indice, first_page)

    make_pattern_log(pdf_file, init_position, end_position, content_first_page,
                     content_last_page, first_page)

    return int(content_first_page)-1, int(content_last_page)-1


def extract_content(reader, first_page, last_page, pdf_file):

    file_name = pdf_file[:-3] + 'txt'
    initia_path = getcwd()
    chdir('D:\Gits_clonados\Projetos_pessoais\estudos_de_python\WebScraping\Txts')

    with open(file_name, 'w', encoding="utf-8") as f:
        while first_page <= last_page:
            texto = reader.pages[first_page].extract_text()
            f.write(texto)
            first_page += 1

    chdir(initia_path)
    return


def read_pdf_files():

    pdf_dir = 'WebScraping\pdfs'

    pdf_files = [f for f in listdir(pdf_dir) if isfile(join(pdf_dir, f))]

    for pdf_file in pdf_files:

        pdf_path = join(pdf_dir, pdf_file)

        with open(pdf_path, 'rb') as file_pdf:

            reader = PyPDF2.PdfReader(file_pdf)

            page = reader.pages[0]

            print(pdf_file)
            first_page, last_page = get_content_pages(page, pdf_file)
            extract_content(reader, first_page, last_page, pdf_file)


if __name__ == '__main__':

    """pdf_path = 'WebScraping\pdfs\caderno1_2010-12-16.pdf'

    with open(pdf_path, 'rb') as file_pdf:

        reader = PyPDF2.PdfReader(file_pdf)

        page = reader.pages[0]

        first_page, last_page = get_content_pages(
            page, 'caderno1_2010-12-16.pdf')

        extract_content(reader, first_page, last_page,
                        'caderno1_2010-12-16.pdf')


    """
    pdf_dir = 'WebScraping\pdfs'

    pdf_files = [f for f in listdir(pdf_dir) if isfile(join(pdf_dir, f))]

    for pdf_file in pdf_files:

        pdf_path = join(pdf_dir, pdf_file)

        with open(pdf_path, 'rb') as file_pdf:

            reader = PyPDF2.PdfReader(file_pdf)

            page = reader.pages[0]

            print(pdf_file)
            first_page, last_page = get_content_pages(page, pdf_file)
            extract_content(reader, first_page, last_page, pdf_file)
