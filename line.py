#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test script

"""
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError


CHANNEL_ACCESS_TOKEN = 'add token here'


line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

try:
    line_bot_api.broadcast(TextSendMessage(text='This is a test'))
except LineBotApiError as e:
    print("Error {}".format(e))
