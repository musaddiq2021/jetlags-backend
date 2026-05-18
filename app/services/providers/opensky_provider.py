import requests

def get_opensky_live_flights():
    url = "https://opensky-network.org/api/states/all"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    states = data.get("states", [])

    flights = []

    for aircraft in states[:10]:
        flights.append({
            "icao24": aircraft[0],
            "callsign": aircraft[1].strip() if aircraft[1] else "Unknown",
            "origin_country": aircraft[2],
            "longitude": aircraft[5],
            "latitude": aircraft[6],
            "altitude": aircraft[7],
            "velocity": aircraft[9],
            "heading": aircraft[10]
        })

    return flights