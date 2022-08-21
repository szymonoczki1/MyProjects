import webbrowser
import subprocess


def urlArray(urlFile = 'urls.txt'):
    '''Makes an array containing urls from the txt file given in the parameter'''
    urlArray = []
    with open(urlFile,'r') as urls:
        for url in urls:
            urlArray.append(url.strip())
    return urlArray


def openUrlsInBrowser(urlArray = None):
    '''opens all urls from urlarray in chrome'''
    if urlArray == None:
        print('urlArray is not given?')
    else:
        for i in urlArray:
            webbrowser.open(i,1)

subprocess.call('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
openUrlsInBrowser(urlArray())
