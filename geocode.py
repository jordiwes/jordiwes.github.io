#!/usr/bin/env python3
"""
Simple address geocoder using multiple services.
Usage: python3 geocode.py "Address Here"
"""

import sys
import json
import urllib.request
import urllib.parse

def geocode_nominatim(address):
    """Geocode using Nominatim (OpenStreetMap)"""
    print(f"Trying Nominatim...")
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': address,
        'format': 'json',
        'limit': 1
    }
    url = f"{base_url}?{urllib.parse.urlencode(params)}"

    req = urllib.request.Request(url, headers={'User-Agent': 'FriendsMapGeocoder/1.0'})

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read())
            if data:
                result = data[0]
                return {
                    'lat': float(result['lat']),
                    'lng': float(result['lon']),
                    'formatted_address': result['display_name'],
                    'service': 'Nominatim'
                }
    except Exception as e:
        print(f"  Nominatim error: {e}")

    return None

def geocode_photon(address):
    """Geocode using Photon (another OSM-based service)"""
    print(f"Trying Photon...")
    base_url = "https://photon.komoot.io/api/"
    params = {
        'q': address,
        'limit': 1
    }
    url = f"{base_url}?{urllib.parse.urlencode(params)}"

    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            data = json.loads(response.read())
            if data['features']:
                feature = data['features'][0]
                coords = feature['geometry']['coordinates']
                props = feature['properties']
                return {
                    'lat': coords[1],
                    'lng': coords[0],
                    'formatted_address': props.get('name', address),
                    'service': 'Photon'
                }
    except Exception as e:
        print(f"  Photon error: {e}")

    return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 geocode.py 'Address Here'")
        print("Example: python3 geocode.py '2355 N 100 W Reynolds IN 47980'")
        sys.exit(1)

    address = ' '.join(sys.argv[1:])
    print(f"\nGeocoding: {address}\n")
    print("=" * 60)

    # Try different services
    services = [geocode_nominatim, geocode_photon]

    for service in services:
        result = service(address)
        if result:
            print(f"\n✓ Success with {result['service']}!")
            print("=" * 60)
            print(f"Formatted Address: {result['formatted_address']}")
            print(f"Latitude:  {result['lat']}")
            print(f"Longitude: {result['lng']}")
            print("\nCSV Format (for Google Sheets):")
            print(f"[Name Here],{result['lat']},{result['lng']}")
            print("=" * 60)
            return

    print("\n✗ Could not geocode this address with any service.")
    print("Try:")
    print("  1. Simplifying the address (just city/state)")
    print("  2. Using Google Maps to manually find coordinates")
    print("  3. Checking the address spelling")

if __name__ == "__main__":
    main()
