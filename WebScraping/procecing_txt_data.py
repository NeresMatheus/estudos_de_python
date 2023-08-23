from os import listdir
from os.path import isfile, join
from searching_patterns import sec_pattern, match_pattern, find_publications
from get_logs import txt_pattern_log, publication_log
import re

if __name__ == '__main__':

    """
    txt_path = 'WebScraping\Txts\caderno1_2017-07-25.txt'

    with open(txt_path, 'r', encoding="utf-8") as f:

        content = f.read()
        result, *_, sec_index = match_pattern(content, sec_pattern())

        publication_list, n_publications = find_publications(
            content, sec_index, '2017')

        publication_log('caderno1_2017-07-25.txt', publication_list, content)
        txt_pattern_log('caderno1_2017-07-25.txt', result, n_publications)

    """
    txt_dir = 'WebScraping\Txts'

    txt_files = [f for f in listdir(txt_dir) if isfile(join(txt_dir, f))]

    for txt_file in txt_files:

        txt_path = join(txt_dir, txt_file)

        with open(txt_path, 'r', encoding="utf-8") as f:

            content = f.read()
            result, *_, sec_index = match_pattern(content, sec_pattern())

            # kind of don't need n_publications, just need to use len()
            publication_list, n_publications = find_publications(
                content, sec_index, txt_file[9:13])  # take year from txt_file

            publication_log(txt_file, publication_list, content)
            txt_pattern_log(txt_file, result, n_publications)
