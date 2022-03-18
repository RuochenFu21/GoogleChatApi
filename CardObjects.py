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
    return {"textParagraph": {"text": text}}
