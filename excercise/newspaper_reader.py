# import requests
# payload= { 'key1' :'sanket'}
# # r = requests.get("https://httpbin.org/get ",params=payload)
# # print(r.url)
# # print(r.text)
# # print(r.status_code)
#
#
# r = requests.get("https://httpbin.org/get ",data=payload)
# print(r.text)
# # url = "www.something.com"
# # data = {
# #     "p1":4,
# #     "p2":8
# # }
# # r2 = requests.post(url=url, data=data)



# """ this is news reader problem"""



# Akhbaar padhke sunaao
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today.. Lets begin")
    url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=5688f62d88f1427681b081fe183470c4"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        print(article['title'])
        speak("Moving on to the next news..Listen Carefully")

    speak("Thanks for listening...")

