from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import telegram

def sitestatus_responses(input_text):
    user_message = str("https://"+input_text).lower()
    req = Request(user_message)

    try:
        response = urlopen(req)
    except HTTPError as e:
        return ("The server couldn\'t ful-fill the request and the Website is not available at this moment ☹️"+ ' ' +"Error Code:"+ ' ' +str(e.code))
    except URLError as e:
        return "Please check the URL you have typed ! May be you're typing it wrong--missing a letter or a punctuation 😊"
    else:
        return "Hooray ! That Website is available at this moment 🥳"
