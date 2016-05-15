import urllib
import urllib2

def grabfromdatabase(request):
    plantname = {"Beatrice":'Plant1',
                 "Lassie":'Plant2',
                 "Paul":'Plant3'
                 }
    url = 'https://blinding-inferno-9101.firebaseio.com/'+plantname[request]+'.json'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    answer = response.read().decode("utf-8")
    response.close()
    return answer
    
flower = grabfromdatabase("Lassie")
wait(3000)
newflower = eval(flower)
say(newflower["humidity"])
