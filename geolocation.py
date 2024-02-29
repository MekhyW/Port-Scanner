import socket
import geoip2.database

geoip_reader = geoip2.database.Reader('GeoLite2-City.mmdb')

def get_geolocation(host):
    try:
        ip_address = socket.gethostbyname(host)
        response = geoip_reader.city(ip_address)
        country = response.country.name.capitalize()
        city = response.city.name.capitalize()
        latitude = response.location.latitude
        longitude = response.location.longitude
        return country, city, latitude, longitude
    except geoip2.errors.AddressNotFoundError:
        return None, None, None, None