import pandas as pd
import folium
import googlemaps
import logging

# Create a DataFrame for the addresses and their descriptions

# Your Google Maps API key - replace 'YOUR_API_KEY' with your actual API key
gmaps = googlemaps.Client(key='')

data = {
    "Address": [
        "南区藤野901番1付近",
        "南区真駒内39番4付近",
        "南区北ノ沢1730番2付近",
        "南区豊滝市民の森(案内板5番付近)",
        "南区北ノ沢1742番35付近",
        "南区北ノ沢1742番2付近",
        "西区西野290番251付近",
        "南区白川1814番415付近",
        "南区北ノ沢1726番14付近",
        "南区中ノ沢1812番21付近",
        "南区北ノ沢1804番31付近",
        "南区藤野766番5付近",
        "南区藤野901番1付近",
        "手稲区手稲本町593番1付近",
        "南区白川1814番150付近",
        "南区南沢515番66",
        "中央区南28条西13丁目1番付近",
        "南区簾舞1条4丁目2番付近",
        "南区石山610番5付近",
        "西区西野290番付近",
        "西区小別沢50番2付近",
        "南区定山渓無番地",
        "南区豊滝410番付近",
        "南区小金湯577番7付近",
        "南区藻岩山無番地",
        "南区定山渓無番地",
        "中央区宮の森1262番付近",
        "南区豊滝532番付近",
        "南区小金湯675番1付近",
        "南区豊滝市民の森",
        "西区山の手427番付近",
        "南区簾舞369番付近",
        "南区簾舞無番地",
        "南区定山渓738番2付近",
        "南区定山渓無番地",
        "南区豊滝市民の森",
        "西区西野704番8付近",
        "中央区自然歩道",
        "南区砥山134番7付近",
        "中央区自然歩道",
        "南区白川1814番119付近",
        "南区真駒内153番1付近",
        "南区小金湯595番1付近",
        "西区西野1006番12付近",
        "南区中ノ沢1812番605付近",
        "南区中ノ沢1985番101付近",
        "南区藤野489番110付近",
        "西区福井5丁目16番付近",
        "西区山の手2条12丁目7番付近",
        "西区山の手7条8丁目5番付近",
        "西区福井9丁目358番1付近",
        "南区中ノ沢1812番1253付近",
        "南区砥山186番1付近",
        "南区藤野富士登山道",
        "南区白川1814番150付近",
        "西区西野708番1付近",
        "南区豊滝509番1付近",
        "西区宮の沢490番11付近",
        "中央区自然歩道",
        "手稲区手稲金山127番11付近",
        "南区北ノ沢1742番35付近",
        "南区南39条西11丁目1番付近",
        "南区藤野910番69付近",
        "手稲区手稲本町593番付近",
        "南区豊滝494番22付近",
        "東区北19条東10丁目付近",
        "西区西野8条9丁目11番付近",
        "南区小金湯637番3付近",
        "手稲区自然歩道",
        "南区定山渓無番地",
        "南区豊滝市民の森",
        "西区西野市民の森",
        "南区中ノ沢1985番101付近",
        "南区定山渓668番付近",
        "南区豊滝336番付近",
        "南区藤野484番1付近",
        "南区簾舞387番付近",
        "南区北ノ沢1804番14付近",
        "南区簾舞459番4付近",
        "南区豊滝40番2付近",
        "手稲区手稲金山104番36付近",
        "南区簾舞341番4付近",
        "西区西野市民の森",
        "中央区盤渓市民の森",
    ]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Function to get latitude and longitude using Google Maps API
def get_coordinates(address):
    geocode_result = gmaps.geocode(address)
    if geocode_result:
        location = geocode_result[0]['geometry']['location']
        return (location['lat'], location['lng'])
    else:
        return (None, None)

# Geocode addresses
df['Coordinates'] = df['Address'].apply(get_coordinates)
df['Latitude'] = df['Coordinates'].apply(lambda x: x[0])
df['Longitude'] = df['Coordinates'].apply(lambda x: x[1])

# Remove rows with None coordinates
df = df.dropna(subset=['Latitude', 'Longitude'])

# Create a map centered around Sapporo
map = folium.Map(location=[43.0621, 141.3544], zoom_start=12)

# Add markers to the map
for idx, row in df.iterrows():
    folium.Marker(
        [row['Latitude'], row['Longitude']],
        popup=f"{row['Address']}"
    ).add_to(map)

# Save the map
map.save("map.html")
