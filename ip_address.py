#ip Addrees localtor
#pip install geocoder
import geocoder as geo
#get your own Ip Addrees
ip_address = geo.ip('me')
print (ip_adress)
#find city of ip 
ip = geo.ip('192.xxx.xxx.x')
print(ip.city)
#get latitude and longitude of IP adress
print(ip.latlng)
#get area info
info = geo.googel('san Francisco')
print(info.geojson)
print(info.osm)
print(info.wkt)
