# -*- coding: utf-8 -*-
import datetime

def interval(repetition, rating, easy_factor=2.5):
	""" SM2 algorithm: https://www.supermemo.com/english/ol/sm2.htm"""
	ef = easy_factor + (0.1 - (5 - rating) * (0.08 + (5 - rating) * 0.02))
	ef = ef if ef >= 1.3 else 1.3
	if rating < 3:
		return 1, ef
	if repetition == 1:
		return 1, ef
	if repetition == 2:
		return 6, ef
	i, ef = interval(repetition-1, rating, easy_factor)
	i *= easy_factor
	return i, ef
