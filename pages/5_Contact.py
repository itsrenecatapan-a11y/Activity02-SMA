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

st.set_page_config(page_title="Contact | Rene Portfolio", layout="wide")
mode = render_theme_controls()
set_page_style(mode)
render_topbar("Contact", "Reach out for collaboration, projects, or opportunities", "mail")

st.title("Contact")

left, right = st.columns(2, gap="large")
with left:
    render_glass_card(f"""
        <h3 style="display:flex;align-items:center;gap:0.6rem;margin-top:0;"><div class="card-icon-badge" style="margin:0;width:40px;height:40px;">{get_icon('phone', 20)}</div> Direct Info</h3>
        <div style="min-height: 100px; display:flex; flex-direction:column; justify-content:center; gap: 0.5rem;">
            <p style="margin:0; display:flex;align-items:center;gap:6px;">{get_icon('phone',16)} +639107323578</p>
            <p style="margin:0; display:flex;align-items:center;gap:6px;">{get_icon('mail',16)} hello@rene.com</p>
            <p style="margin:0; display:flex;align-items:center;gap:6px;">{get_icon('map_pin',16)} Masbate, PH</p>
        </div>
    """)

with right:
    render_glass_card(f"""
        <h3 style="display:flex;align-items:center;gap:0.6rem;margin-top:0;"><div class="card-icon-badge" style="margin:0;width:40px;height:40px;">{get_icon('link', 20)}</div> Profiles</h3>
        <div style="min-height: 100px; display:flex;flex-wrap:wrap;align-content:center;gap:.35rem;">
            <a class="social-link" href="https://facebook.com/linrennocap" target="_blank">{get_icon('external_link',14)} Facebook</a>
            <a class="social-link" href="https://www.instagram.com/lilrennocap" target="_blank">{get_icon('external_link',14)} Instagram</a>
            <a class="social-link" href="https://www.github.com" target="_blank">{get_icon('github',14)} GitHub</a>
        </div>
    """)


