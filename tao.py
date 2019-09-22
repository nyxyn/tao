#!/usr/bin/env python3

import sys
import random
import json

tao_text_location = '/var/tao/taoTeChing.json'


def run():
    chapters = get_chapters()

    if len(sys.argv) is 1:
        random_chapter = random.randint(0, len(chapters) - 1)
        print_chapter(chapters, random_chapter)
    else:
        requested_chapter = int(sys.argv[1]) - 1
        if requested_chapter < 0 or requested_chapter > len(chapters) - 1:
            print('Chapter argument must be between 1 and ' + str(len(chapters)))
        else:
            print_chapter(chapters, int(requested_chapter))


def print_chapter(chapters, index):
    chapter_obj = chapters[index]
    chapter_num = chapter_obj['chapter']
    chapter_text = chapter_obj['text']

    print('Chapter ' + str(chapter_num))
    print(chapter_text)


def get_chapters():
    with open(tao_text_location) as f:
        return json.loads(f.read())


run()
