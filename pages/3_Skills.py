import streamlit as st

from style import (
    get_icon,
    render_divider,
    render_glass_card,
    render_info_card,
    render_section_header,
    render_theme_controls,
    render_topbar,
    set_page_style,
)

st.set_page_config(page_title="Skills | Rene Portfolio", layout="wide")
mode = render_theme_controls()
set_page_style(mode)
render_topbar("Skills & Talents", "Creative direction, arts, and leadership", "award")

st.title("Skills & Talents")

skills = [
    ("Public Speaking & Communication", "message_circle"),
    ("Dance & Performance Arts", "zap"),
    ("Graphic Design & Visual Storytelling", "camera"),
    ("Interior Design & Space Planning", "layout"),
    ("Fashion Design & Styling", "award"),
    ("Creative Direction", "book"),
    ("Event Planning & Coordination", "calendar"),
    ("Photography & Basic Photo Editing", "camera"),
    ("Team Collaboration & Leadership", "user"),
    ("Time Management & Organization", "clipboard"),
    ("Adaptability & Creative Problem-Solving", "zap"),
]

render_section_header("My Expertise", "award")
st.markdown(
    '<div style="display:flex;flex-wrap:wrap;gap:.6rem;margin-bottom:1rem;" class="reveal-stagger">'
    + "".join(
        f'<span class="chip reveal">{get_icon(icon, 16)} {name}</span>'
        for name, icon in skills
    )
    + "</div>",
    unsafe_allow_html=True,
)

render_divider()

render_section_header("Conferences & Engagements", "calendar")

render_glass_card(f"""
    <p style="margin-bottom:.45rem;"><span style="display:inline-flex;align-items:center;gap:6px;">{get_icon('check_circle',16)} <strong>National Youth Summit</strong></span></p>
    <p style="margin-bottom:.45rem;"><span style="display:inline-flex;align-items:center;gap:6px;">{get_icon('check_circle',16)} <strong>Diocesan Youth Encounter</strong></span></p>
    <p style="margin-bottom:0;"><span style="display:inline-flex;align-items:center;gap:6px;">{get_icon('check_circle',16)} <strong>National Environmental Youth Leader Summit</strong></span></p>
""")

render_divider()

render_info_card("user", '<span style="font-size:1.05rem;">Driven by continuous learning, purposeful creation, and meaningful impact.</span>')
