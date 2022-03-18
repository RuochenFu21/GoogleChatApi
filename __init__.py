from json import dumps
import time
from typing import *

from httplib2 import Http


class Message:
    selflist: list[Dict]

    def __init__(self, selflist=[]):
        self.selflist = selflist

    def send(self, where: str) -> dict:
        """

        :rtype: object
        """
        url = where
        bot_message = {"cards": self.selflist}
        message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

        http_obj = Http()

        response = http_obj.request(
            uri=url,
            method='POST',
            headers=message_headers,
            body=dumps(bot_message),
        )

        return response

    class CardObjWidgets:
        def __init__(self) -> object:
            self.items = []

        def add(self, item):
            self.items.append(item)

    class CardObj:
        items: dict

        def __init__(self, items=None) -> None:
            if items is None:
                items = {"header": {}, "sections": []}
            self.items = items
            return None

        def SetHeader(self, header):
            self.items["header"] = header

        def AddWidget(self, widget):
            self.items["sections"].append({'widgets': widget.items})

    def AddCardObj(self, CardObj):
        self.selflist.append(CardObj.items)
