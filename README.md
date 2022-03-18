# GoogleChatApi 0.0.1

- Only for Cards in google Hangouts bot
- Work in progress

# Usage
## Message Object
    from GoogleChatApi import *
    from GoogleChatApi.CardObjects import *
    
	# make a message
    message = Message([]) # the list is optional
### Card Object
	# One message object can contain more than one card
	CardObj = Message.CardObj()
#### Header
	#One Card Object only can have one header
	header = Header(["rickroll",
	                               "rickroll", # subtitle, optional
                                   "<Image Link>",             #Image Link,optional
                                   "Image"]) # or "Avatar"  #Image Type,optional, if you have a Image Type or Image Link, you need both of them
#### Widgets 
	# One Card Object can contain more than one Widgets
	widgets = Message.CardObjWidgets()
##### Text Paragraph
	# One Widget can contain more than one Text Paragraph
	paragraph = TextParagraph('<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">Rick Roll video</a>') # Html text
## Adding them all up
	CardObj.SetHeader(header) # Set the head of the Card
	Widgets.add(paragraph) # Add the TextParagraph to the widget
	CardObj.AddWidget(widgets) # Add the widget to the Card
	message.addCardObj(CardObj) # Add the Card!
## Sending them
	CardObj.send("<The Bot Url>") 
finally, after this whole lot of code, you now sent the message!
