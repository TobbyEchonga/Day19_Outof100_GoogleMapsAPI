import googlemaps

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = 'YOUR_API_KEY'
gmaps = googlemaps.Client(key=API_KEY)

def get_coordinates(address):
    try:
        # Geocoding API request
        result = gmaps.geocode(address)

        if result:
            location = result[0]['geometry']['location']
            lat, lng = location['lat'], location['lng']
            return lat, lng
        else:
            return None

    except googlemaps.exceptions.HTTPError as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    # Example: Get coordinates for a given address
    address = "1600 Amphitheatre Parkway, Mountain View, CA"
    coordinates = get_coordinates(address)

    if coordinates:
        print(f"Coordinates for '{address}': {coordinates}")
    else:
        print(f"Could not retrieve coordinates for '{address}'.")
