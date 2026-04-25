import streamlit as st

from style import (
    get_icon,
    render_divider,
    render_glass_card,
    render_section_header,
    render_theme_controls,
    render_topbar,
    set_page_style,
)

st.set_page_config(page_title="About | Rene Portfolio", layout="wide")
mode = render_theme_controls()
set_page_style(mode)
render_topbar("About Me", "Profile, education, interests, and experience", "user")

st.title("About")

render_glass_card(
    f"""
    <h3 style="display:flex;align-items:center;gap:0.6rem;margin-top:0;"><div class="card-icon-badge" style="margin:0;width:40px;height:40px;">{get_icon('user', 20)}</div> About Me</h3>
    <p>hi im rene, I advocate and aspire to lead in conserving and protecting biodiversity while pursuing my goals with purpose and determination. I am driven to explore the world, expand my perspective, and grow both personally and professionally.</p>
    <p>I aim to channel my creativity into designing sustainable fashion that promotes ethical practices and environmental responsibility. Through leadership, innovation, and perseverance, I strive to create meaningful impact and contribute to a more sustainable and forward-thinking future.</p>
    """
)

info_left, info_right = st.columns(2, gap="large")
with info_left:
    render_glass_card(f"""
        <p style="margin-bottom:.45rem;"><span style="display:inline-flex;align-items:center;gap:6px;">{get_icon('calendar',16)} <strong>Birthday:</strong></span> 2004</p>
        <p style="margin-bottom:0;"><span style="display:inline-flex;align-items:center;gap:6px;">{get_icon('phone',16)} <strong>Phone:</strong></span> +63981 388 5022</p>
    """)
with info_right:
    render_glass_card(f"""
        <p style="margin-bottom:.45rem;"><span style="display:inline-flex;align-items:center;gap:6px;">{get_icon('map_pin',16)} <strong>City:</strong></span> Masbate, PH</p>
        
    """)
render_divider()

render_section_header("Schools Attended", "book")

render_glass_card(f"""
    <p style="margin-bottom:.45rem;"><span style="display:inline-flex;align-items:center;gap:6px;">{get_icon('check_circle',16)} <strong>College:</strong></span> Dr. Emilio B. Espinosa Sr. Memorial State College of Agriculture and Technology</p>
    <p style="margin-bottom:.45rem;"><span style="display:inline-flex;align-items:center;gap:6px;">{get_icon('check_circle',16)} <strong>High School:</strong></span> Del Carmen National High School</p>
    <p style="margin-bottom:0;"><span style="display:inline-flex;align-items:center;gap:6px;">{get_icon('check_circle',16)} <strong>Elementary:</strong></span> San Jose Elementary School</p>
""")
