import requests


def metres_to_feet(metres):
    if metres is None:
        return None
    return round(metres * 3.28084)


def mps_to_kmh(mps):
    if mps is None:
        return None
    return round(mps * 3.6)


def mps_to_mph(mps):
    if mps is None:
        return None
    return round(mps * 2.23694)


def format_opensky_aircraft(aircraft):
    altitude_metres = aircraft[7]
    velocity_mps = aircraft[9]

    return {
        "icao24": aircraft[0],
        "callsign": aircraft[1].strip() if aircraft[1] else "Unknown",
        "origin_country": aircraft[2],
        "longitude": aircraft[5],
        "latitude": aircraft[6],
        "altitude_metres": altitude_metres,
        "altitude_feet": metres_to_feet(altitude_metres),
        "speed_mps": velocity_mps,
        "speed_kmh": mps_to_kmh(velocity_mps),
        "speed_mph": mps_to_mph(velocity_mps),
        "heading": aircraft[10],
        "tracking_source": "OpenSky"
    }


def get_opensky_live_flights():
    url = "https://opensky-network.org/api/states/all"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    states = data.get("states", [])

    flights = []

    for aircraft in states[:10]:
        flights.append(format_opensky_aircraft(aircraft))

    return flights


def get_opensky_uk_live_flights():
    url = "https://opensky-network.org/api/states/all"

    params = {
        "lamin": 49.8,
        "lamax": 60.9,
        "lomin": -8.6,
        "lomax": 1.8
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    states = data.get("states", [])

    flights = []

    for aircraft in states[:20]:
        flights.append(format_opensky_aircraft(aircraft))

    return flights