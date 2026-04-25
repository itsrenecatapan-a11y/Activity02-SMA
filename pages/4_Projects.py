import streamlit as st

from style import (
    get_icon,
    render_divider,
    render_section_header,
    render_theme_controls,
    render_topbar,
    set_page_style,
)

st.set_page_config(page_title="Talents & Events | Rene Portfolio", layout="wide")
mode = render_theme_controls()
set_page_style(mode)
render_topbar("Talents & Events", "A glimpse into Rene's creative journey and events attended", "camera")

st.title("Talents & Events")
st.write("A collection of moments showcasing creative direction, fashion, and visual storytelling.")

render_divider()

# Gallery columns for top 3 pictures
col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.image("pictures/ca750c1e-d208-4976-8fa5-b028fd0815c7.jpeg", use_container_width=True)

with col2:
    st.image("pictures/4b075694-2f27-47ad-95ab-b63dca85b859.jpeg", use_container_width=True)

with col3:
    st.image("pictures/33ec04ea-356f-41ac-9eb7-61bd2e16d84c.jpeg", use_container_width=True)

st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

# Wide picture below (centered and slightly reduced in size)
_, center_col, _ = st.columns([1, 4, 1])
with center_col:
    st.image("pictures/f711fc51-1045-45bd-b695-7cb9ca09cc29.jpeg", use_container_width=True)

render_divider()
st.info("I will continually update this space with pictures of real events and creative projects I attend and manage!")
