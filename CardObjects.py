def Header(item: list) -> dict:
    listin = {"header": {}}
    if not hasattr(item, '__iter__') or len(item) == 3:
        raise ValueError("Pass an Right Value")
        return

    listin["header"]["title"] = item[0]
    try:
        listin["header"]["subtitle"] = item[1]
    except:
        pass
    else:
        pass
    try:
        listin["header"]["imageUrl"], listin["header"]["imageStyle"] = item[2], item[3]
    except:
        pass
    else:
        pass
    return listin["header"]


def TextParagraph(text: str) -> dict:
    """
    Text Paragraph
    Support Html Text
    :param text: HTML Text Object
    :return: TextParagraph
    """
    return {"textParagraph": {"text": text}}


def Image(ImageUrl: str, Onclick: str = None):
    if Onclick is None:
        return {"image": {"imageUrl": ImageUrl}}
    if type(Onclick) == type(''):
        return {"image": {"imageUrl": ImageUrl, "onClick": {"openLink": {"url": Onclick}}}}
    return {"image": {"imageUrl": ImageUrl, "onClick": Onclick}}
