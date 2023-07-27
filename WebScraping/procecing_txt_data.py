from os import listdir
from os.path import isfile, join
from searching_patterns import sec_pattern, match_pattern, publication_pattern
from get_logs import txt_pattern_log, publication_log
import re

if __name__ == '__main__':
    """
    txt_path = 'WebScraping\Txts\caderno1_2017-07-25.txt'

    with open(txt_path, 'r', encoding="utf-8") as f:

        content = f.read()
        result, index = match_pattern(content, sec_pattern())

        pattern = re.compile(
            r'[0-9]{2}[ ][0-9]{6}[ ]-[ ][0-9]')

        lista_de_posicoes = [m for m in pattern.finditer(content)]

        n_publications = len(lista_de_posicoes)


        txt_pattern_log('caderno1_2017-07-25', result, n_publications)

    """
    txt_dir = 'WebScraping\Txts'

    txt_files = [f for f in listdir(txt_dir) if isfile(join(txt_dir, f))]

    for txt_file in txt_files:

        txt_path = join(txt_dir, txt_file)

        with open(txt_path, 'r', encoding="utf-8") as f:

            content = f.read()
            result, index = match_pattern(content, sec_pattern())

            # make a function in searchin_patterns
            pattern = re.compile(
                r'[0-9]{2}[ ][0-9]{7}[ ].*?[0-9]|[0-9]{2}[ ][0-9]{6}[ ]-[ ][0-9]')

            pucliation_list = [m for m in pattern.finditer(content)]
            n_publications = len(pucliation_list)

            publication_log(txt_file, pucliation_list, content)
            txt_pattern_log(txt_file, result, n_publications)
