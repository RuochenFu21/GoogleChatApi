### GoogleChatApi 0.0.2

- Only for Cards in google Hangouts bot **YET**
- Work in progress

# GoogleChatApi 0.0.2

![](https://img.shields.io/badge/language-python-yellow.svg) ![](https://img.shields.io/badge/python-package-green.svg)

**Table of Contents**
- [Usage](#usage)
  * [Message Object](#message-object)
    + [Card Object](#card-object)
      - [Header](#header)
      - [Widgets](#widgets)
        * [Text Paragraph](#text-paragraph)
        * [Image](#Image)
  * [Adding them all up](#adding-them-all-up)
  * [Sending them](#sending-them)
  * [Change Log](#Change-Log)

# Usage
## Message Object
    from GoogleChatApi import *
    from GoogleChatApi.CardObjects import *
    
	# make a message
    message = Message([]) # the list is optional
-- -
### Card Object
	# One message object can contain more than one card
	CardObj = Message.CardObj()
-- -
#### Header
	#One Card Object only can have one header
	header = Header(["rickroll",
	                               "rickroll", # subtitle, optional
                                   "<Image Link>",             #Image Link,optional
                                   "Image"]) # or "Avatar"  #Image Type,optional, if you have a Image Type or Image Link, you need both of them
-- -
#### Widgets 
	# One Card Object can contain more than one Widgets
	widgets = Message.CardObjWidgets()
-- -
##### Text Paragraph
	# One Widget can contain more than one Text Paragraph
	paragraph = TextParagraph('<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">Rick Roll video</a>') # Html text
-- -
##### Image
    # One Widget can contain more than one Image
    image = Image('https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg', https://www.youtube.com/watch?v=dQw4w9WgXcQ') # ImageUrl and The Website to open when click on it
-- -
## Adding them all up
	CardObj.SetHeader(header) # Set the head of the Card
	Widgets.add(paragraph)   # Add the TextParagraph to the widget
    Widgets.add(image)   # Add the Image to the widget
	CardObj.AddWidget(widgets) # Add the widget to the Card
	message.addCardObj(CardObj) # Add the Card!
-- -
## Sending them
	message.send("<The Bot Url>") 
finally, after this whole lot of code, you now sent the message!

-- -
## Change Log

## 0.0.2 (19-03-2022)
 -- -
### Bug Fixed
- Readme "Sending them" problem fixed

### Added Features
- Image
- Change Log

## 0.0.1 (17-03-2022)
 -- -
### Features
- Readme Added
- Have access to Send a card message
