from django.shortcuts import render
import json
import urllib.request

# Create your views here.
API_key="e0851fbe20b13ebf2479435692d06f51"

def index(request):
    if request.method=="POST":
        city=request.POST['city']
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
        res=urllib.request.urlopen(url).read()
        json_data=json.loads(res)
        data={
            "country_code":str(json_data['sys']['country']),
            "coordinate":str(json_data['coord']['lon']) + " " + str(json_data['coord']['lat']),
            "temp":str(json_data['main']['temp'])+'k',
            "pressure":str(json_data['main']['pressure']),
            "humidity":str(json_data['main']['humidity']),
        }
    else:
        data={}
    print(data)

    return render(request,'index.html',{"data":data})