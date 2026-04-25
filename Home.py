import streamlit as st

from style import (
    get_icon,
    render_divider,
    render_glass_card,
    render_info_card,
    render_interest_card_html,
    render_section_header,
    render_theme_controls,
    render_typing_hero,
    set_page_style,
)

st.set_page_config(page_title="Home | Rene Portfolio", layout="wide")
mode = render_theme_controls()
set_page_style(mode)

# ── Hero ──
render_typing_hero(
    "Rene",
    "Third-year CS student  ·  Ganda lang",
)

st.markdown("<div style='height:.8rem'></div>", unsafe_allow_html=True)



# ── Quick stats ──
left, right = st.columns(2)
left.metric("Age", "20")
right.metric("Location", "Cawayan, Masbate")


