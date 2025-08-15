from email.message import EmailMessage
from datetime import datetime

def format_email(name, weather):
    msg = EmailMessage()
    
    city = weather['location']['city']
    country = weather['location']['country']
    current = weather['current']
    hourly = weather['hourtly']

    # Current datetime
    now = datetime.now()

    # Filter hourly forecasts from current hour onwards
    upcoming_hours = [
        h for h in hourly
        if datetime.strptime(h['time'], "%Y-%m-%d %H:%M") >= now
    ]

    # Plain text version
    plain_text = f"Hi {name},\n\nHere is your weather update for {city}, {country}:\n\n" \
                 f"Current Weather:\n" \
                 f"Temperature: {current['temp_c']}°C\n" \
                 f"Condition: {current['condition']}\n" \
                 f"Humidity: {current['humidity']}%\n" \
                 f"Wind Speed: {current['wind_kph']} km/h\n\n" \
                 f"Hourly Forecast:\n"

    for hour in upcoming_hours:
        hour_time = datetime.strptime(hour['time'], "%Y-%m-%d %H:%M").strftime("%H:%M")
        plain_text += f"{hour_time}: {hour['temp_c']}°C, {hour['condition']}, Wind {hour['wind_kph']} km/h, Humidity {hour['humidity']}%\n"

    msg.set_content(plain_text)

    # HTML version
    hourly_rows = ""
    for hour in upcoming_hours:
        hour_time = datetime.strptime(hour['time'], "%Y-%m-%d %H:%M").strftime("%H:%M")
        hourly_rows += f"""
        <tr>
            <td style="padding:4px; border:1px solid #ddd;">{hour_time}</td>
            <td style="padding:4px; border:1px solid #ddd;">{hour['temp_c']}°C</td>
            <td style="padding:4px; border:1px solid #ddd;">{hour['condition']}</td>
            <td style="padding:4px; border:1px solid #ddd;">{hour['wind_kph']} km/h</td>
            <td style="padding:4px; border:1px solid #ddd;">{hour['humidity']}%</td>
        </tr>
        """

    html_content = f"""\
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style type="text/css">
        body {{ font-family: Arial, sans-serif; background-color: #f5f5f5; margin:0; padding:0; }}
        h1 {{ font-size: 28px; margin-bottom: 10px; color: #000000;}}
        h2 {{ font-size: 22px; margin-bottom: 10px; color: #000000;}}
        p {{ margin: 5px 0; }}
        table {{ border-collapse: collapse; width: 100%; }}
        td, th {{ padding: 8px; border: 1px solid #ddd; text-align: left; color: #000000;}}
        #email-container {{ max-width: 600px; margin: auto; background-color: #ffffff; padding: 20px; }}
        #current-weather {{text-align: center; margin: auto;}}
    </style>
</head>
<body>
    <div id="email-container">
        <h1>Hi {name},</h1>
        <h2>Weather Update for {city}, {country}</h2>
        
        <h1>Current Weather: </h1>
        <div id="current-weather">
            <h2>Temperature: {current['temp_c']}°C</h2>
            <h2>Condition: {current['condition']}</h2>
            <h2>Humidity: {current['humidity']}%</h2>
            <h2>Wind Speed: {current['wind_kph']} km/h</h2>
        </div>

        <h1>Hourly Forecast</h1>
        <table>
            <tr>
                <th>Time</th>
                <th>Temp</th>
                <th>Condition</th>
                <th>Wind</th>
                <th>Humidity</th>
            </tr>
            {hourly_rows}
        </table>
    </div>
</body>
</html>
"""

    msg.add_alternative(html_content, subtype='html')
    return msg
