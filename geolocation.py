import socket
import geoip2.database

geoip_reader = geoip2.database.Reader('GeoLite2-City.mmdb')

def get_geolocation(host):
    try:
        ip_address = socket.gethostbyname(host)
        response = geoip_reader.city(ip_address)
        country = response.country.name if response.country.name else "{unknown}"
        city = response.city.name if response.city.name else "{unknown}"
        latitude = response.location.latitude if response.location.latitude else "{unknown}"
        longitude = response.location.longitude if response.location.longitude else "{unknown}"
        return country, city, latitude, longitude
    except geoip2.errors.AddressNotFoundError:
        return None, None, None, None