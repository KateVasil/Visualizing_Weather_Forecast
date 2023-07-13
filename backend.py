import requests

API_KEY = "a418ef704fdf6f7648e73bc45838887e"


def get_data(place, forecasted_days=None, option=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecasted_days
    filtered_data = filtered_data[:nr_values]
    if option == "Temperature":
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
    if option == "Sky":
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]
    return filtered_data


print(get_data(place="Tokyo", forecasted_days=3, option="Temperature"))



