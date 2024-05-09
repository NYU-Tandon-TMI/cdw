import streamlit as st
import pandas as pd
import pydeck as pdk

st.title('DDC Mapping Program')

df = pd.read_csv('data/cdw_csv_processed_example.csv', encoding='unicode_escape')

st.write("Data loaded successfully!")

unique_debris_types = ['All types of debris'] + list(df['type_debris'].unique())
selected_debris = st.selectbox('Select Type of Debris:', unique_debris_types)

unique_pickup_addresses = ['All pickup addresses'] + list(df['pickup_address'].unique())
selected_pickup_address = st.selectbox('Select Pickup Address:', unique_pickup_addresses)

unique_receiving_addresses = ['All receiving addresses'] + list(df['receiving_address'].unique())
selected_receiving_address = st.selectbox('Select Receiving Address:', unique_receiving_addresses)

pickup_color = st.color_picker('Choose a color for pickup addresses', '#FF6347')  
receiving_color = st.color_picker('Choose a color for receiving addresses', '#4682B4')  

filtered_data = df[
    ((df['type_debris'] == selected_debris) | (selected_debris == 'All types of debris')) &
    ((df['pickup_address'] == selected_pickup_address) | (selected_pickup_address == 'All pickup addresses')) &
    ((df['receiving_address'] == selected_receiving_address) | (selected_receiving_address == 'All receiving addresses'))
]

def draw_routes(filtered_data, pickup_color, receiving_color):
    if not filtered_data.empty:
        routes = [
            {
                "from_coordinates": [row['pickup_lng'], row['pickup_lat']],
                "to_coordinates": [row['receiving_lng'], row['receiving_lat']],
                "info": f"Type of Debris: {row['type_debris']}<br>"
                        f"Waste Quantity: {row['waste_quantity']}<br>"
                        f"Pickup Name: {row['pickup_name']}<br>"
                        f"Pickup Address: {row['pickup_address']}<br>"
                        f"Receiving Name: {row['receiving_name']}<br>"
                        f"Receiving Address: {row['receiving_address']}"
            }
            for _, row in filtered_data.iterrows()
        ]

        pickup_color_rgba = [int(pickup_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)] + [255]
        receiving_color_rgba = [int(receiving_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)] + [255]

        layer = pdk.Layer(
            "ArcLayer",
            routes,
            get_source_position="from_coordinates",
            get_target_position="to_coordinates",
            get_width=5,
            get_tilt=15,
            get_source_color=pickup_color_rgba,
            get_target_color=receiving_color_rgba,
            pickable=True,
            auto_highlight=True,
        )

        view_state = pdk.ViewState(
            latitude=filtered_data['pickup_lat'].mean(),
            longitude=filtered_data['pickup_lng'].mean(),
            zoom=6
        )

        st.pydeck_chart(pdk.Deck(
            layers=[layer],
            initial_view_state=view_state,
            tooltip={"html": "<b>Route Information:</b> {info}"},
            map_style='mapbox://styles/mapbox/light-v10'
        ))
    else:
        st.error('No routes found for the selected options.')

draw_routes(filtered_data, pickup_color, receiving_color)
