import requests

def get_forecast_url():
    url = "https://api.weather.gov/points/40.1934,-85.3864"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data['properties']['forecast']

def get_forecast_data(forecast_url):
    response = requests.get(forecast_url)
    response.raise_for_status()
    data = response.json()
    return data['properties']['periods']

def display_forecast(periods):
    for period in periods:
        print(f"{period['name']}: {period['temperature']}°F")
        print(f"Forecast: {period['detailedForecast']}\n")

def main():
    forecast_url = get_forecast_url()
    periods = get_forecast_data(forecast_url)
    display_forecast(periods)

if __name__ == "__main__":
    main()
