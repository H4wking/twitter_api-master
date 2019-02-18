import folium
import twitter2
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


def get_coordinates(locations):
    coordinates = []
    geolocator = Nominatim(user_agent='name', timeout=None, scheme='http')
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=0.1)
    for loc in locations:
        try:
            location = geolocator.geocode(locations[loc])
            coordinates.append([loc, location.latitude, location.longitude])
        except:
            continue
    return coordinates


def fg_locations(name):
    """
    (int) -> folium.map.FeatureGroup
    Return a FeatureGroup containing locations of twitter friends.
    """
    fg_lc = folium.FeatureGroup(name="Locations")
    coordinates = get_coordinates(twitter2.get_data(twitter2.get_json(name), "location"))
    for name, lt, ln in coordinates:
        fg_lc.add_child(folium.Marker(location=[lt, ln], popup=name, icon=folium.Icon()))
    return fg_lc


def create_map(name):
    map = folium.Map()
    fg_lc = fg_locations(name)
    map.add_child(fg_lc)
    map.save('/Users/danylonazaruk/PycharmProjects/twitter_api-master/templates/map.html')


if __name__ == "__main__":
    name = str(input("Enter account name: "))
    create_map(name)
