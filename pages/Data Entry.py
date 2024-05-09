import streamlit as st
import pandas as pd
import csv

st.write("# Data Input")

st.markdown(
    """
    **This page is designed for users to input data.**
    """
)

def load_data():
    return pd.read_csv('data/template.csv')

def load_pickup_book():
    return pd.read_csv('data/pickup_address_book.csv')

def load_gene_book():
    return pd.read_csv('data/generator_address_book.csv')

if 'selected_pickup' not in st.session_state:
    st.session_state.selected_pickup = ""
if 'pickup_name' not in st.session_state:
    st.session_state.pickup_name = ""
if 'pickup_add' not in st.session_state:
    st.session_state.pickup_add = ""
if 'pickup_state' not in st.session_state:
    st.session_state.pickup_state = ""
if 'pickup_city' not in st.session_state:
    st.session_state.pickup_city = ""
if 'pickup_zip' not in st.session_state:
    st.session_state.pickup_zip = ""
if 'pickup_lat' not in st.session_state:
    st.session_state.pickup_lat = ""
if 'pickup_lng' not in st.session_state:
    st.session_state.pickup_lng = ""

if 'selected_gene' not in st.session_state:
    st.session_state.selected_gene = ""
if 'gene_name' not in st.session_state:
    st.session_state.gene_name = ""
if 'gene_add' not in st.session_state:
    st.session_state.gene_add = ""
if 'gene_state' not in st.session_state:
    st.session_state.gene_state = ""
if 'gene_city' not in st.session_state:
    st.session_state.gene_city = ""
if 'gene_zip' not in st.session_state:
    st.session_state.gene_zip = ""



pickup_book = load_pickup_book()
pickup_book['display'] = pickup_book['name'] + ' - ' + pickup_book['address']

pickup_option = st.selectbox('Choose Existing Pickup Location', [''] + pickup_book['display'].tolist(), on_change=lambda: update_pickup(pickup_option), key="pickup")
gene_option = st.selectbox('Choose Existing Receiving Location', [''] + pickup_book['display'].tolist(), on_change=lambda: update_gene(gene_option), key="generator")

def update_pickup(option):
    st.session_state.selected_pickup = option
    if option:
        selected_pickup = pickup_book[pickup_book['display'] == option]
        st.session_state.pickup_name = selected_pickup['name'].iloc[0]
        st.session_state.pickup_add = selected_pickup['address'].iloc[0]
        st.session_state.pickup_city = selected_pickup['city'].iloc[0]
        st.session_state.pickup_state = selected_pickup['state'].iloc[0]
        st.session_state.pickup_zip = selected_pickup['zip'].iloc[0]
        st.session_state.pickup_lat = selected_pickup['lat'].iloc[0]
        st.session_state.pickup_lng = selected_pickup['lng'].iloc[0]
    st.experimental_rerun()

def update_gene(option):
    st.session_state.selected_gene = option
    if option:
        selected_gene = pickup_book[pickup_book['display'] == option]
        st.session_state.gene_name = selected_gene['name'].iloc[0]
        st.session_state.gene_add = selected_gene['address'].iloc[0]
        st.session_state.gene_city = selected_gene['city'].iloc[0]
        st.session_state.gene_state = selected_gene['state'].iloc[0]
        st.session_state.gene_zip = selected_gene['zip'].iloc[0]
    st.experimental_rerun()

if pickup_option != st.session_state.selected_pickup:
    update_pickup(pickup_option)

if gene_option != st.session_state.selected_gene:
    update_gene(gene_option)

with st.form("my_form"):
    st.write("### Pickup Location")
    pk_name = st.text_input("Location Name", value=st.session_state.pickup_name, key="pkn")
    pk_add = st.text_input("Address", value=st.session_state.pickup_add, key="pka")
    pk_city = st.text_input("City", value=st.session_state.pickup_city, key="pkc")
    pk_state = st.text_input("State", value=st.session_state.pickup_state, key="pks")
    pk_zip = st.text_input("Zip", value=st.session_state.pickup_zip, key="pkz")
    pk_lat = st.text_input("Latitude", value=st.session_state.pickup_lat, key="pkt")
    pk_lng = st.text_input("Longtitude", value=st.session_state.pickup_lng, key="pkg")

    st.write("### Generator Location")
    gn_name = st.text_input("Location Name", value=st.session_state.gene_name, key="gnn")
    gn_add = st.text_input("Address", value=st.session_state.gene_add, key="gna")
    gn_city = st.text_input("City", value=st.session_state.gene_city, key="gnc")
    gn_state = st.text_input("State", value=st.session_state.gene_state, key="gns")
    gn_zip = st.text_input("Zip", value=st.session_state.gene_zip, key="gnz")
    
    st.write("#### Waste Info")
    waste_quantity = st.text_input("Waste Quantity", value='', key='waste_quantity')
    waste_type = st.text_input("Type of Debris", value='', key='waste_type')
    trans_name = st.text_input("Transporter Name", value='', key='trans_name')

    
    submitted = st.form_submit_button("Submit")

if submitted:
    with open('data/template.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([waste_type,waste_quantity,pk_name, pk_add, pk_city, pk_state, pk_zip,trans_name, pk_lat, pk_lng, gn_name, gn_add, gn_city, gn_state, gn_zip])
        st.success("Submit Success")

st.write("### Input Results", load_data())
