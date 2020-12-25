#!/usr/bin/env python3
import pyqrcode


def main():
    card = pyqrcode.create(
        content="https://taiseiyo.github.io/christmas_card/", error='H')
    card.png(file='./static/qr_code.png', scale=6)


main()
