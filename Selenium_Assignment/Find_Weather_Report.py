from Fetch_API_Response import FetchAPIResponse
from Fetch_UI_Response import FetchUIResponse


class FindWeatherReport:

    def find_variance_range(temp, variance):
        higher_val = int(temp) * (100 + int(variance)) / 100
        lower_val = int(temp) * (100 - int(variance)) / 100
        return higher_val, lower_val

    def find_response_final(city, variance):
        temp_ui = FetchUIResponse.getTempFromUI(city)
        temp_api = FetchAPIResponse.getTempFromAPI(city)

        if temp_api is not None and temp_ui is not None:
            temp_ui = temp_ui[:-1]
            upper, lower = FindWeatherReport.find_variance_range(temp_ui, variance)

            temp_ui, temp_api, lower, upper = float(temp_ui), float(temp_api), float(lower), float(upper)

            if lower <= temp_api <= upper:
                print('Success \n')
            else:
                if temp_api < lower:
                    print(f'Temperature is lower than variance range by {lower - temp_api} \n')
                else:
                    print(f'Temperature is higher than variance range by {temp_api - upper} \n')


if __name__ == '__main__':
    json = {
        "City": ["Kolkata", "Newyork", "Texas"],
        "Variance": 3
    }

    var = json.get('Variance')
    city_names_list = json.get('City')

    for city_name in city_names_list:
        print(city_name)
        FindWeatherReport.find_response_final(city_name, var)
