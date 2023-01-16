import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to streamlit! 👋")

st.sidebar.success("Movie recommendation system")
 
st.markdown(
    """
    Streamlit is an open-source app framework built specifically for 
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what streamlit can do!
    ### Want to learn more?
    - Check out  [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a questions in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [TMBD_5000 dataset](https:github.com/streamlit/demo-uber-nyc-pickups)

    """
)