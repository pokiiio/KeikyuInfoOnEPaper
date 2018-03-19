# coding=utf-8

import keikyu
import text_to_image
import numpy
import epd2in7b
from os import path
from PIL import Image, ImageOps, ImageFont, ImageDraw

E_PAPER_WIDTH = 264
E_PAPER_HEIGHT = 176
HEADER_SIZE = 20


def remove_prefix(text):
    if not u"】" in text:
        return text

    text = text[text.find(u"】") + 1:]
    return text


def show_image(black_image, red_image):
    epd = epd2in7b.EPD()
    epd.init()

    frame_black = epd.get_frame_buffer(black_image)
    frame_red = epd.get_frame_buffer(red_image)
    epd.display_frame(frame_black, frame_red)


if __name__ == '__main__':
    keikyu_unko_info = remove_prefix(keikyu.get_unko())

    image_black = Image.new(
        "RGB", (E_PAPER_WIDTH, E_PAPER_HEIGHT), (255, 255, 255))

    image_black.paste(text_to_image.text_to_image(
        E_PAPER_WIDTH, E_PAPER_HEIGHT - HEADER_SIZE, keikyu_unko_info, 16), (0, HEADER_SIZE))

    image_red = Image.new(
        "RGB", (E_PAPER_WIDTH, E_PAPER_HEIGHT), (255, 255, 255))

    image_red.paste(ImageOps.invert(text_to_image.text_to_image(
        E_PAPER_WIDTH, HEADER_SIZE, u"京浜急行 運行情報", 16)))

    show_image(image_black.rotate(270, expand=True),
               image_red.rotate(270, expand=True))
