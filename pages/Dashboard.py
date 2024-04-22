import streamlit as st
import pandas as pd
import pydeck as pdk

st.title('DDC Mapping Program')

file_url = 'https://raw.githubusercontent.com/bronzekillervan/ddc/main/cdw_csv_sample.csv'

def draw_routes(df):
    valid_routes = df.dropna(subset=['pickup_lat', 'pickup_lng', 'receiving_lat', 'receiving_lng'])

    routes = [
        {
            "from_coordinates": [row['pickup_lng'], row['pickup_lat']],
            "to_coordinates": [row['receiving_lng'], row['receiving_lat']],
            "info": ("<b>Type of Debris:</b> {type_debris}<br>"
                     "<b>Waste Quantity:</b> {waste_quantity}<br>"
                     "<b>Pickup Name:</b> {pickup_name}<br>"
                     "<b>Pickup Address:</b> {pickup_address}<br>"
                     "<b>Generator Name:</b> {generator_name}<br>"
                     "<b>Generator Address:</b> {generator_address}").format(
                         type_debris=row['type_debris'],
                         waste_quantity=row['waste_quantity'],
                         pickup_name=row['pickup_name'],
                         pickup_address=row['pickup_address'],
                         generator_name=row['generator_name'],
                         generator_address=row['generator_address']
                     )
        }
        for _, row in valid_routes.iterrows()
    ]

    layer = pdk.Layer(
        "ArcLayer",
        routes,
        get_source_position="from_coordinates",
        get_target_position="to_coordinates",
        get_width=5,
        get_tilt=15,
        get_color=[255, 182, 193, 255], 
        pickable=True,
        auto_highlight=True,
    )

    view_state = pdk.ViewState(
        latitude=valid_routes['pickup_lat'].mean(),
        longitude=valid_routes['pickup_lng'].mean(),
        zoom=6
    )

    tooltip = {
        "html": "{info}",  
        "style": {
            "backgroundColor": "pink",
            "color": "white"
        }
    }

    st.pydeck_chart(pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip=tooltip,
        map_style='mapbox://styles/mapbox/light-v10'
    ))

df = pd.read_csv(file_url)

if {'type_debris', 'waste_quantity', 'pickup_lat', 'pickup_lng', 'receiving_lat', 'receiving_lng', 'pickup_name', 'pickup_address', 'generator_name', 'generator_address'}.issubset(df.columns):
    draw_routes(df)
else:
    st.error('Column not found.')


