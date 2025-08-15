from db.db_fetch import fetch_subscribers, fetch_locations
from weather.weather import get_weather
from emailer.sendEmail import sendEmail

def main():
#-- Collecting weather data for all locations in the db --
    all_locations = {}
    # Fetch locations from the database
    locations = fetch_locations()
    
    if not locations:
        print("No locations found in the database.")
        return
    else:
        print(f"Locations fetched: {locations}")

    # Fetch weather for each location
    for city in locations:
        weather_data = get_weather(city)
        all_locations[city] = weather_data

#-- Sending weather data to subscribers --
    # Fetch subscribers from the database
    subscribers = fetch_subscribers()
    if not subscribers:
        print("No subscribers found in the database.")
        return
    else:
        print(f"Subscribers fetched: {subscribers}")

    # Send weather data to each subscriber
    for subscriber in subscribers:
        subscriberCity = subscriber[3]
        subscriberEmail = subscriber[1]
        if subscriberCity in all_locations:
            content = all_locations[subscriberCity]
            sendEmail(content, subscriberEmail)

if __name__ == "__main__":
    main()