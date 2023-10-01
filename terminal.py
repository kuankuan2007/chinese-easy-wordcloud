"""
Copyright (c) 2023 Gou Haoming
chineseEasyWordcloud is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2.
You may obtain a copy of Mulan PSL v2 at:
         http://license.coscl.org.cn/MulanPSL2
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.
"""
import doFolder
from . import easyWordcloud
from . import cut
from typing import List


class ArgumentError(Exception):
    pass



def chineseWordcloud():
    import argparse
    argparser = argparse.ArgumentParser()
    argparser.add_argument('content', nargs='?', type=str,
                           help="original content of text", default=None)
    argparser.add_argument('-f', '--file', nargs="+",
                           action='extend', default=[], help="List of files that will be read as utf-8 plain text")
    argparser.add_argument('-d', '--dir', nargs="+",
                           action='append', default=[], help="Folder list, the first item is the folder, and all items after that are considered to be ignored files in the folder")
    argparser.add_argument('-o', '--output',required=True, type=str, help="Output file")

    argparser.add_argument('--font_path', type=str, default=None,
                        help='Font path to the font that will be used (OTF or TTF)')

    argparser.add_argument('--width', type=int, default=400,
                        help='Width of the canvas')
    argparser.add_argument('--height', type=int, default=200,
                        help='Height of the canvas')
    argparser.add_argument('--margin', type=int, default=2, help='Margin')
    argparser.add_argument('--ranks_only', type=bool, default=None, help='Ranks only')
    argparser.add_argument('--prefer_horizontal', type=float,
                        default=0.9, help='Prefer horizontal')
    argparser.add_argument('--scale', type=float, default=1, help='Scale')
    
    argparser.add_argument('--max_words', type=int, default=200,
                        help='Maximum number of words')
    argparser.add_argument('--min_font_size', type=int, default=4,
                        help='Smallest font size to use')
    argparser.add_argument('--stopwords',action='extend', nargs='+', type=str, default=[], help='Stopwords')
    argparser.add_argument('--random_state', type=int,
                        default=None, help='Random state')
    argparser.add_argument('--background_color', type=str,
                        default='black', help='Background color')
    argparser.add_argument('--max_font_size', type=int,
                        default=None, help='Maximum font size')
    argparser.add_argument('--font_step', type=int, default=1, help='Font step')
    argparser.add_argument('--mode', type=str, default='RGB', help='Mode')
    argparser.add_argument('--relative_scaling', type=lambda x:float(x) if x!='auto' else x,
                        default='auto', help='Relative scaling')
    argparser.add_argument('--regexp', type=str, default=None, help='Regexp')
    argparser.add_argument('--collocations', type=bool,
                        default=True, help='Collocations')
    argparser.add_argument('--colormap', type=str, default=None, help='Colormap')
    argparser.add_argument('--normalize_plurals', type=bool,
                        default=True, help='Normalize plurals')
    argparser.add_argument('--contour_width', type=float,
                        default=0, help='Contour width')
    argparser.add_argument('--contour_color', type=str,
                        default='black', help='Contour color')
    argparser.add_argument('--repeat', type=bool, default=False, help='Repeat')
    argparser.add_argument('--include_numbers', type=bool,
                        default=False, help='Include numbers')
    argparser.add_argument('--min_word_length', type=int,
                        default=0, help='Minimum word length')
    argparser.add_argument('--collocation_threshold', type=int,
                        default=30, help='Collocation threshold')

    args = argparser.parse_args().__dict__

    if args['content']==None and len(args['file'])==0 and len(args['dir'])==0:
        raise ArgumentError(
            "The original content, file list, and folder list cannot be empty at the same time\n原始内容、文件列表和文件夹列表不能同时为空"
        )
    content:str=args['content'] or ""

    def contFileContent(x: doFolder.File):
        nonlocal content
        content += x.content.decode()+"\n"
    for i in args['file']:
        contFileContent(doFolder.File(i))
    for i in args['dir']:
        doFolder.Folder(i[0], ignores=i[1:]).forEachFile(contFileContent)
    easyWordcloud.generate(cut.removeStopwords(cut.cutWordDefault(content),args['stopwords']), args['output'], **{i: args[i] for i in args if i not in [
                           'content', 'file', 'dir', 'output','stopwords'] and args[i] != None})
if __name__ == "__main__":
    chineseWordcloud()
    