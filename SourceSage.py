

import os
import sys
import pprint

sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))
pprint.pprint(sys.path)

from modules.source_sage import SourceSage

if __name__ == "__main__":
    folders = ['./']
    source_sage = SourceSage(folders, ignore_file='.SourceSageignore',
                             output_file='SourceSage.md',
                             language_map_file='config/language_map.json')
    source_sage.generate_markdown()