import phonenumbers
import folium
from phonenumbers import geocoder,carrier
from opencage.geocoder import OpenCageGeocode
number = input("Enter the phone number you want to locate: ")
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,"en")
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,"en"))
key= "d447d6d81b824b2fac83a416ed17a1d4"
geocoder = OpenCageGeocode(key)
query = str(location)

results = geocoder.geocode(query)
#print(results)
lat = results[0]['geometry']['lat']
lng = results[1]['geometry']['lng']
print(lat,lng)
myMap = folium.Map(location = [lat,lng], zoom_start = 9)
folium.Marker([lat, lng], popup=location).add_to(myMap)
myMap.save("mylocation.html")