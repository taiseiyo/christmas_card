#!/usr/bin/env python3
import pyqrcode

card = pyqrcode.create(
    content="https://taiseiyo.github.io/christmas_card/", error='H')
card.png(file='card.png', scale=6)
