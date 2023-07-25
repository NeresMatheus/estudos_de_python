from os import listdir
from os.path import isfile, join
from searching_patterns import sec_pattern, match_pattern
from get_logs import txt_pattern_log

if __name__ == '__main__':

    txt_dir = 'WebScraping\Txts'

    txt_files = [f for f in listdir(txt_dir) if isfile(join(txt_dir, f))]

    for txt_file in txt_files:

        txt_path = join(txt_dir, txt_file)

        with open(txt_path, 'r', encoding="utf-8") as f:

            content = f.read()
            result, index = match_pattern(content, sec_pattern())
            txt_pattern_log(txt_file, result)
