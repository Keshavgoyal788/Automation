import requests


class FetchAPIResponse:

    def getTempFromAPI(city_name):
        api_key = '0fdce9db16a74caf520b9fe3c07de7eb'
        base_url = 'http://api.openweathermap.org/data/2.5/weather?'
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name

        try:
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] == 200:
                y = x['main']
                current_temp = y['temp']
                temp = int(current_temp) - 273.15
                temp = "{:.2f}".format(temp)
                print(f'Current temperature is (in Celcius) from API: {temp} \n')
            else:
                print('City not found !!!')
                temp = None
            return temp
        except Exception as e:
            print("Exception occured: " + str(e))
