# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="NYU-MOT-CDW",
        page_icon="👋",
    )

    st.write("# Welcome to CDW Project! 👋")

    st.markdown(
        """
        ### Project Introduction
        This website, as the final phase of the capstone project, will contain all deliverables of the project and serve as a publicly accessible site for displaying maps.
        
        In this web application, based on the Streamlit framework, the team developed an interactive dashboard to visualize CDW flows in a variety of graphical views. This tool is useful in policy development for CDW recycling and reuse, providing insight into annual flow trends by material type, transaction, and destination, potentially facilitating a more sustainable approach to CDW management.
        ### How to Start？    
        """
    )
    st.markdown("""<iframe width="800" height="450" src="https://cdn.pixabay.com/video/2016/12/31/6962-197634410_large.mp4" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
                """, unsafe_allow_html=True)
    

if __name__ == "__main__":
    run()
