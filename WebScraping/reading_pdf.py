import PyPDF2
import os


def get_content_pages(page):
    """ looking in the summary on the first page for the page 
    who has the information we want"""

    first_page = page.extract_text()
    search_pattern = 'Secretaria de Estado de Meio Ambiente e Desenvolvimento Sustentável'
    end_position = first_page.find(search_pattern) + len(search_pattern)

    caracter = end_position + 1
    content_first_page = ''
    while not (first_page[caracter].isalpha()):
        caracter += 1
        if first_page[caracter].isnumeric():
            content_first_page += first_page[caracter]

    print(content_first_page)
    print('até')

    while not (first_page[caracter].isnumeric()):
        caracter += 1

    content_last_page = first_page[caracter:caracter+2]
    print(content_last_page)
    return int(content_first_page)-1, int(content_last_page)-1


if __name__ == '__main__':
    print('ta rolando')

    pdf_path = 'WebScraping\pdfs\caderno1_2023_07_18.pdf'

    with open(pdf_path, 'rb') as file_pdf:

        reader = PyPDF2.PdfReader(file_pdf)

        page = reader.pages[0]
        first_page, last_page = get_content_pages(page)

        indice = first_page
        with open('teste.txt', 'w', encoding="utf-8") as f:
            while indice < last_page + 2:
                texto = reader.pages[indice].extract_text()
                f.write(texto)
                indice += 1
