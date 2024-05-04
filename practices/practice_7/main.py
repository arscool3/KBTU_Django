cities = {'Almaty':'utc+5', 'New York':'utc-4', 'Tokyo':'utc+9', 'London':'utc+1'}


def get_city_timezone(city: str):
    if city in cities:
        return cities[city]
    return f"Time zone information not available for this city: {city}"
