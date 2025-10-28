from datetime import datetime

class Location:
    def __init__(self, city, country):
        self.city = city
        self.country = country

    def get_city(self):
        return self.city


class WeatherData:
    def __init__(self, temperature, humidity, condition):
        self.timestamp = datetime.now()
        self.temperature = temperature
        self.humidity = humidity
        self.condition = condition

    def __str__(self):
        return f"{self.condition} ({self.temperature}°C, {self.humidity}% humidity)"


class Forecast:
    def __init__(self, date, weather_data):
        self.date = date
        self.weather_data = weather_data  # Composition

    def get_weather_data(self):
        return self.weather_data


class WeatherService:
    # ⚙️ DEPENDENCY: uses other classes, but does not store them.
    def get_current_weather(self, location: Location) -> WeatherData:
        print(f"Fetching weather for {location.get_city()}...")
        return WeatherData(temperature=24.5, humidity=68, condition="Sunny")

    def get_forecast(self, location: Location, days: int):
        print(f"Fetching {days}-day forecast for {location.get_city()}...")
        forecast_list = []
        for i in range(days):
            forecast_list.append(Forecast(
                date=f"Day {i+1}",
                weather_data=WeatherData(temperature=25 + i, humidity=60 - i, condition="Sunny")
            ))
        return forecast_list


# --- Demonstration ---
service = WeatherService()
loc = Location("Los Angeles", "USA")

today_weather = service.get_current_weather(loc)
print(today_weather)

forecast = service.get_forecast(loc, 3)
for f in forecast:
    print(f"{f.date}: {f.get_weather_data()}")