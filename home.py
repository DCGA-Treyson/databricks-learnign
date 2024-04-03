import streamlit as st
#from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title("Select Search Method")
#st.write(
#    """Replace this example with your own code!
#    **And if you're new to Streamlit,** check
#    out our easy-to-follow guides at
#    [docs.streamlit.io](https://docs.streamlit.io).
#    """
#)

# Get the current credentials
#session = get_active_session()

option = st.selectbox('Part Search Method',('Single Part', 'Part List','Brand'))
