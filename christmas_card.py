#!/usr/bin/env python3
import pyqrcode

card = pyqrcode.create(
    content="https://taiseiyo.github.io/computational_game/", error='H')
card.png(file='card.png', scale=6)
