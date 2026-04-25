"""
Modern portfolio UI system — elegant, soft girly aesthetics, Playfair display, jelly animations, squircle layouts.
"""
import streamlit as st
import streamlit.components.v1 as components
from typing import Dict, Optional

# ═══════════════════════════════════════════════════════════════
# SVG ICONS  (Lucide-style, 24×24, stroke-based)
# ═══════════════════════════════════════════════════════════════
ICONS: Dict[str, str] = {
    "code": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>',
    "shield": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    "globe": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10A15.3 15.3 0 0 1 12 2z"/></svg>',
    "mail": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>',
    "user": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
    "folder": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg>',
    "tool": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>',
    "map_pin": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "phone": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    "calendar": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>',
    "external_link": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>',
    "github": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.565 21.796 24 17.3 24 12c0-6.627-5.373-12-12-12z"/></svg>',
    "terminal": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg>',
    "database": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>',
    "layout": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg>',
    "server": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"/><rect x="2" y="14" width="20" height="8" rx="2" ry="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg>',
    "award": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>',
    "send": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>',
    "zap": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
    "book": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>',
    "briefcase": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>',
    "link": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>',
    "arrow_right": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
    "layers": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>',
    "clipboard": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg>',
    "bar_chart": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="20" x2="12" y2="10"/><line x1="18" y1="20" x2="18" y2="4"/><line x1="6" y1="20" x2="6" y2="16"/></svg>',
    "camera": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>',
    "message_circle": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>',
    "gamepad": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="6" y1="12" x2="10" y2="12"/><line x1="8" y1="10" x2="8" y2="14"/><line x1="15" y1="13" x2="15.01" y2="13"/><line x1="18" y1="11" x2="18.01" y2="11"/><rect x="2" y="6" width="20" height="12" rx="2"/></svg>',
    "dollar": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>',
    "hash": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="9" x2="20" y2="9"/><line x1="4" y1="15" x2="20" y2="15"/><line x1="10" y1="3" x2="8" y2="21"/><line x1="16" y1="3" x2="14" y2="21"/></svg>',
    "check_circle": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>',
}


def get_icon(name: str, size: int = 24) -> str:
    svg = ICONS.get(name, "")
    if size != 24:
        svg = svg.replace('width="24"', f'width="{size}"').replace('height="24"', f'height="{size}"')
    return svg


# ═══════════════════════════════════════════════════════════════
# THEME
# ═══════════════════════════════════════════════════════════════
def render_theme_controls() -> str:
    if "theme_mode" not in st.session_state:
        st.session_state.theme_mode = "Light"
    st.sidebar.title("Appearance")
    
    # Bind the toggle exactly to session state using a key to fix the two-clicks bug
    if "theme_toggle_key" not in st.session_state:
        st.session_state.theme_toggle_key = (st.session_state.theme_mode == "Dark")
        
    st.sidebar.toggle("🔆 / 🌙 Switch Theme", key="theme_toggle_key")
    
    mode = "Dark" if st.session_state.theme_toggle_key else "Light"
    st.session_state.theme_mode = mode
    return mode


# ═══════════════════════════════════════════════════════════════
# MASTER STYLE  (CSS + floating‑bg + scroll JS)
# ═══════════════════════════════════════════════════════════════
def set_page_style(mode: str) -> None:
    is_light = mode == "Light"
    p = _palette(is_light)
    bg_gradient = f"linear-gradient(135deg, {p['bg']} 0%, {p['surface']} 100%)"

    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,500;0,700;1,500&display=swap');

    :root {{
        --bg:{p['bg']};--surface:{p['surface']};--card:{p['card']};
        --text:{p['text']};--muted:{p['muted']};--border:{p['border']};
        --accent:{p['accent']};--accent2:{p['accent2']};--accent-subtle:{p['accent_subtle']};
        --shadow:{p['shadow']};--shadow-hover:{p['shadow_hover']};
        --navtext:{p['nav_text']};--navhover:{p['nav_hover']};--navactive:{p['nav_active']};
        --inputbg:{p['input_bg']};--inputtext:{p['input_text']};
    }}

    /* ── RESET & BASE ── */
    *, *::before, *::after {{ box-sizing:border-box; }}

    .stApp {{
        background: var(--bg);
        background-image: {bg_gradient};
        color: var(--text);
        font-family: 'Outfit', sans-serif;
    }}

    .stApp h1,.stApp h2,.stApp h3,.stApp h4 {{
        font-family: 'Playfair Display', serif;
        color: var(--text);
        font-weight: 700;
        letter-spacing: -0.5px;
    }}
    .stApp p,.stApp li,.stApp label {{
        font-family: 'Outfit', sans-serif;
        color: var(--text);
        font-weight: 300;
        line-height: 1.6;
    }}
    .stApp h1 {{ font-size:2.8rem; }}
    .stApp h2 {{ font-size:2.2rem; }}
    .stApp h3 {{ font-size:1.6rem; }}

    #MainMenu {{ visibility:hidden; }}
    footer {{ visibility:hidden; }}
    [data-testid="stHeader"] {{ background:transparent; }}

    [data-testid="collapsedControl"],
    [data-testid="collapsedControl"] *,
    button[kind="header"],
    button[kind="header"] * {{
        color:var(--text)!important;
        fill:var(--text)!important;
    }}

    ::-webkit-scrollbar {{ width:8px; }}
    ::-webkit-scrollbar-track {{ background:var(--bg); }}
    ::-webkit-scrollbar-thumb {{ background:var(--accent-subtle);border-radius:10px; }}
    ::-webkit-scrollbar-thumb:hover {{ background:var(--accent); }}

    ::selection {{ background:var(--accent);color:#fff; }}

    /* ── ANIMATIONS ── */
    @keyframes fadeInUp {{
        from {{ opacity:0;transform:translateY(30px); }}
        to {{ opacity:1;transform:translateY(0); }}
    }}
    @keyframes fadeIn {{ from {{ opacity:0; }} to {{ opacity:1; }} }}
    @keyframes typing {{
        from {{ max-width:0; }}
        to {{ max-width:100%; }}
    }}
    @keyframes blinkCursor {{
        0%,100% {{ border-right-color:var(--accent); }}
        50% {{ border-right-color:transparent; }}
    }}
    @keyframes floatSoft {{
        0%,100% {{ transform:translateY(0) rotate(0deg); }}
        50% {{ transform:translateY(-15px) rotate(2deg); }}
    }}
    @keyframes pulseSoft {{
        0%,100% {{ opacity: 0.6; transform: scale(1); }}
        50% {{ opacity: 1; transform: scale(1.05); }}
    }}

    /* ── REVEAL EFFECTS ── */
    .reveal {{
        animation: fadeInUp 0.8s cubic-bezier(0.22, 1, 0.36, 1) both;
    }}
    .reveal-stagger > .reveal:nth-child(1) {{ animation-delay: 0.1s; }}
    .reveal-stagger > .reveal:nth-child(2) {{ animation-delay: 0.2s; }}
    .reveal-stagger > .reveal:nth-child(3) {{ animation-delay: 0.3s; }}
    .reveal-stagger > .reveal:nth-child(4) {{ animation-delay: 0.4s; }}
    .reveal-stagger > .reveal:nth-child(5) {{ animation-delay: 0.5s; }}
    .reveal-stagger > .reveal:nth-child(6) {{ animation-delay: 0.6s; }}
    .reveal-stagger > .reveal:nth-child(7) {{ animation-delay: 0.7s; }}
    .reveal-stagger > .reveal:nth-child(8) {{ animation-delay: 0.8s; }}
    .reveal-stagger > .reveal:nth-child(9) {{ animation-delay: 0.9s; }}
    .reveal-stagger > .reveal:nth-child(10) {{ animation-delay: 1.0s; }}

    .stMainBlockContainer {{ animation:fadeIn .8s ease-out; position:relative;z-index:1; }}

    /* ── AESTHETIC BACKGROUND ORBS ── */
    .bg-shapes {{ position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden; }}
    .bg-shape {{ position:absolute;border-radius:50%; filter:blur(60px); }}
    .bg-s1 {{
        width:50vw;height:50vw;top:-10%;right:-10%;
        background:var(--accent);opacity:0.15;
        animation:pulseSoft 15s infinite ease-in-out;
    }}
    .bg-s2 {{
        width:40vw;height:40vw;bottom:-5%;left:-10%;
        background:var(--accent2);opacity:0.12;
        animation:floatSoft 20s infinite ease-in-out;
    }}

    /* ── SIDEBAR ── */
    [data-testid="stSidebar"] {{
        background:var(--surface);border-right:1px solid var(--border);
    }}
    [data-testid="collapsedControl"], [data-testid="collapsedControl"] svg,
    [data-testid="stSidebarCollapseButton"], [data-testid="stSidebarCollapseButton"] svg {{
        color: var(--text) !important;
        fill: var(--text) !important;
    }}
    [data-testid="stSidebarNav"] a, [data-testid="stSidebarNavLink"], [data-testid="stSidebarNavLink"] span {{
        color:var(--navtext)!important;
        border-radius: 20px;
        margin: 4px 10px;
        padding-left: 1rem;
        transition:all .3s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    [data-testid="stSidebarNav"] a:hover, [data-testid="stSidebarNavLink"]:hover, [data-testid="stSidebarNavLink"]:hover span {{
        background:var(--navhover)!important;
        transform:scale(1.02);
    }}
    [data-testid="stSidebarNavLink"][aria-current="page"], [data-testid="stSidebarNavLink"][aria-current="page"] span {{
        background:var(--accent-subtle)!important;
        color:var(--accent)!important;
        font-weight:600;
    }}

    /* ── TOPBAR ── */
    .topbar {{
        background:var(--card);
        backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
        border:1px solid var(--border);border-radius:40px;
        padding:1rem 1.5rem;margin-bottom:1.5rem;
        box-shadow:0 8px 32px var(--shadow);
        animation:fadeInUp .7s cubic-bezier(0.22,1,0.36,1);
        display:flex;align-items:center;gap:1.2rem;
        transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    .topbar:hover {{ transform: scale(1.01); }}
    .topbar .topbar-icon {{
        width: 48px; height: 48px; border-radius: 50%;
        background: var(--accent-subtle); color: var(--accent);
        display:flex; align-items:center; justify-content:center;
    }}
    .topbar .topbar-body strong {{ font-family:'Playfair Display',serif; font-size:1.3rem; font-weight:700; }}
    .topbar .topbar-body p {{ margin:0!important; color:var(--muted); font-size:0.95rem; }}

    /* ── HERO / TYPING ── */
    .hero-section {{ padding:3rem 0 2rem; text-align:center; animation:fadeIn .8s ease-out; }}
    
    .typing-wrapper {{ display:inline-block;position:relative; }}
    .typing-text {{
        font-family:'Playfair Display',serif;
        font-size:clamp(2.5rem,7vw,4.5rem);font-weight:700;
        background: linear-gradient(135deg, var(--text), var(--accent));
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        overflow:hidden;white-space:nowrap;display:inline-block;
        border-right:3px solid var(--accent);
        max-width:0;
        animation: typing 1.6s steps(13,end) .6s forwards, blinkCursor .7s step-end infinite .6s;
    }}
    
    .hero-title-static {{
        font-family:'Playfair Display',serif;
        font-size:clamp(2.5rem,7vw,4.5rem);font-weight:700;
        background: linear-gradient(135deg, var(--text), var(--accent));
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}
    .hero-subtitle {{
        margin-top:1rem;font-size:1.15rem;color:var(--muted);
        font-weight:300;letter-spacing:0.5px;
        opacity:0;animation:fadeInUp .8s ease-out 0.5s forwards;
    }}
    .hero-subtitle-static {{
        margin-top:1rem;font-size:1.15rem;color:var(--muted);
        font-weight:300;letter-spacing:0.5px;
    }}

    /* ── ELEGANT GLASS CARD ── */
    .glass-card {{
        background:var(--card);
        backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);
        border:1px solid var(--border);border-radius:32px;
        padding:1.8rem;margin-bottom:1rem;
        box-shadow:0 10px 30px var(--shadow);
        transition:all .4s cubic-bezier(0.34, 1.56, 0.64, 1);
        position:relative;overflow:hidden;
    }}
    .glass-card:hover {{
        transform:translateY(-5px) scale(1.01);
        box-shadow:0 20px 40px var(--shadow-hover);
        border-color:var(--accent);
    }}
    .card-icon-badge {{
        width:56px;height:56px;border-radius:50%;
        background:var(--accent-subtle);
        display:flex;align-items:center;justify-content:center;
        margin-bottom:1rem;color:var(--accent);
        transition:transform .4s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    .glass-card:hover .card-icon-badge {{ transform:scale(1.15) rotate(-5deg); }}
    .glass-card h3 {{ margin:0 0 0.8rem; font-family:'Playfair Display',serif; font-size:1.4rem; }}
    .glass-card p {{ color:var(--muted); font-size:1rem; }}

    /* ── SECTION HEADER ── */
    .section-hdr {{ display:flex;align-items:center;gap:0.8rem; margin:2.5rem 0 1.5rem; justify-content:center; }}
    .section-hdr .sh-icon {{
        color:var(--accent); display:flex; align-items:center;
        background:var(--accent-subtle); padding:10px; border-radius:50%;
    }}
    .section-hdr h2 {{ margin:0; font-family:'Playfair Display',serif; font-size:1.8rem; }}

    /* ── METRIC CARDS ── */
    div[data-testid="stMetric"] {{
        background:var(--card);
        backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);
        border:1px solid var(--border);border-radius:24px;
        padding:1.2rem;box-shadow:0 6px 20px var(--shadow);
        transition:transform .4s cubic-bezier(0.34, 1.56, 0.64, 1),box-shadow .4s;
    }}
    div[data-testid="stMetric"]:hover {{
        transform:translateY(-4px) scale(1.02);
        box-shadow:0 12px 30px var(--shadow-hover);
    }}
    div[data-testid="stMetricValue"], div[data-testid="stMetricLabel"] {{
        color: var(--text) !important;
        font-family: 'Playfair Display', serif !important;
    }}
    div[data-testid="stMetricLabel"] {{
        font-family: 'Outfit', sans-serif !important;
        color: var(--muted) !important;
    }}

    /* ── CHIP / TAG ── */
    .chip {{
        display:inline-flex;align-items:center;gap:.4rem;
        border:1px solid var(--accent-subtle);background:var(--surface);
        border-radius:30px;padding:0.4rem 1rem;
        margin:.3rem .3rem .3rem 0;font-size:0.9rem;font-weight:400;
        color:var(--text);
        transition:all .3s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    .chip:hover {{
        transform:translateY(-3px) scale(1.05);
        background:var(--accent-subtle);
        color:var(--accent);
        border-color:var(--accent);
    }}
    .chip svg {{ width:14px;height:14px; }}

    /* ── INFO / EXPLORE CARD ── */
    .info-card {{
        background:var(--card);
        backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);
        border:1px solid var(--border);border-radius:24px;
        padding:1.2rem;box-shadow:0 8px 24px var(--shadow);
        transition:all .4s cubic-bezier(0.34, 1.56, 0.64, 1);
        display:flex;align-items:center;gap:1.2rem;
    }}
    .info-card:hover {{
        transform:translateY(-4px);box-shadow:0 12px 30px var(--shadow-hover);
        border-color:var(--accent);
    }}
    .info-card .ic-icon {{
        width: 44px; height: 44px; border-radius: 50%;
        background: var(--accent-subtle); color: var(--accent);
        display:flex; align-items:center; justify-content:center; flex-shrink: 0;
    }}

    /* ── SOCIAL LINK ── */
    .social-link {{
        display:inline-flex;align-items:center;justify-content:center;gap:.5rem;
        color:var(--text);text-decoration:none;
        padding:0.6rem 1.2rem;border-radius:40px;
        border:1px solid var(--border);margin:.3rem;
        font-size:0.95rem;font-weight:500;
        background:var(--surface);
        transition:all .4s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    .social-link:hover {{
        background:var(--accent); color:#fff;
        border-color:var(--accent);
        transform:translateY(-3px) scale(1.05);box-shadow:0 8px 20px var(--shadow);
    }}
    .social-link svg {{ width:14px;height:14px; }}

    /* ── PROGRESS / SKILL BAR ── */
    .skill-bar {{ margin-bottom:1.5rem; }}
    .skill-bar-header {{ display:flex;justify-content:space-between;align-items:center; margin-bottom:.5rem; }}
    .skill-bar-label {{ font-weight:500;font-size:1rem; display:flex;align-items:center;gap:6px; }}
    .skill-bar-value {{ font-weight:600;font-size:0.95rem;color:var(--accent); }}
    .skill-bar-track {{ height:10px;background:var(--border);border-radius:10px;overflow:hidden; }}
    .skill-bar-fill {{
        height:100%;background:linear-gradient(90deg, var(--accent2), var(--accent));
        border-radius:10px;width:var(--bar-w);
        transition: width 1.5s cubic-bezier(0.22, 1, 0.36, 1);
    }}

    /* ── PROJECT ENHANCEMENT ROW ── */
    .project-row {{
        background:var(--card);
        backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);
        border:1px solid var(--border);border-radius:30px;
        padding:1.4rem;margin-bottom:1rem;
        box-shadow:0 8px 24px var(--shadow);
        transition:all .4s cubic-bezier(0.34, 1.56, 0.64, 1);
        display:flex;align-items:flex-start;gap:1.2rem;
    }}
    .project-row:hover {{
        transform:translateY(-4px) scale(1.01);
        box-shadow:0 16px 36px var(--shadow-hover);
        border-color:var(--accent);
    }}
    .project-row .proj-icon {{
        flex-shrink:0;width:52px;height:52px;border-radius:50%;
        background:var(--accent-subtle);
        display:flex;align-items:center;justify-content:center;
        color:var(--accent);
        transition:transform .4s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    .project-row:hover .proj-icon {{ transform:rotate(-10deg) scale(1.1); }}
    .project-row h4 {{ margin:0 0 .3rem;font-family:'Playfair Display',serif;font-size:1.2rem; font-weight: 700; }}
    .project-row p {{ margin:0 0 .4rem;font-size:.95rem;color:var(--muted); }}

    /* ── DIVIDER ── */
    .styled-hr {{ border:none;height:1px;background:var(--border);margin:3rem 0; opacity: 0.6; }}
    
    /* ── STATUS DOT ── */
    .status-dot {{
        display:inline-block;width:10px;height:10px;border-radius:50%;
        background:var(--accent);margin-right:8px;
        box-shadow: 0 0 10px var(--accent);
    }}

    /* ── BUTTONS & INPUTS ── */
    .stButton > button, [data-testid="stFormSubmitButton"] > button {{
        border: none!important;
        background: linear-gradient(135deg, var(--accent), var(--accent2))!important;
        color: #fff!important;
        border-radius: 40px!important;
        font-family: 'Outfit', sans-serif!important; font-weight: 500!important;
        padding: 0.8rem 2rem!important;
        transition: all .4s cubic-bezier(0.34, 1.56, 0.64, 1)!important;
        box-shadow: 0 8px 20px var(--shadow)!important;
    }}
    .stButton > button:hover, [data-testid="stFormSubmitButton"] > button:hover {{
        transform: translateY(-3px) scale(1.04)!important;
        box-shadow: 0 12px 28px var(--shadow-hover)!important;
    }}
    [data-testid="stLinkButton"] a {{
        border: none!important;
        background: linear-gradient(135deg, var(--accent), var(--accent2))!important;
        color: #fff!important;
        border-radius: 40px!important;
        font-family: 'Outfit', sans-serif!important; font-weight: 500!important;
        padding: 0.8rem 2rem!important;
        text-decoration:none!important;
        transition: all .4s cubic-bezier(0.34, 1.56, 0.64, 1)!important;
        box-shadow: 0 8px 20px var(--shadow)!important;
    }}
    [data-testid="stLinkButton"] a:hover {{
        transform: translateY(-3px) scale(1.04)!important;
        box-shadow: 0 12px 28px var(--shadow-hover)!important;
    }}

    .stTextInput input,.stTextArea textarea {{
        border-radius:20px!important; border:1px solid var(--border)!important;
        background:var(--inputbg)!important; color:var(--text)!important;
        padding: 0.8rem 1.2rem!important; font-family:'Outfit',sans-serif!important;
        transition:all .3s!important;
    }}
    .stTextInput input:focus,.stTextArea textarea:focus {{
        border-color:var(--accent)!important;
        box-shadow:0 0 0 4px var(--accent-subtle)!important;
    }}
    .stTextInput input::placeholder,.stTextArea textarea::placeholder {{
        color:var(--muted)!important;opacity:0.8;
    }}
    
    .stSelectbox div[data-baseweb="select"] > div {{
        border-radius:20px!important;border:1px solid var(--border)!important;
        background:var(--inputbg)!important;transition:border-color .3s;
    }}
    .stSelectbox div[data-baseweb="select"] > div:hover {{
        border-color:var(--accent)!important;
    }}
    
    /* ── TABS ── */
    .stTabs [data-baseweb="tab-list"] {{ gap:.3rem; }}
    .stTabs [data-baseweb="tab"] {{
        border-radius:20px 20px 0 0;font-family:'Outfit',sans-serif;font-weight:500;
        transition:all .3s;
    }}

    /* ── TOGGLE FIX ── */
    [data-testid="stToggle"] {{
        background-color: var(--card) !important;
        border: 1px solid var(--border) !important;
        border-radius: 20px !important;
        padding: 5px 15px !important;
        display: inline-flex !important;
        align-items: center !important;
        box-shadow: 0 4px 10px var(--shadow) !important;
    }}


    /* ── RESPONSIVE ── */
    @media (max-width:768px) {{
        .topbar {{ padding:1rem;border-radius:24px; }}
        .glass-card {{ padding:1.2rem; border-radius:24px; }}
    }}
    </style>

    <div class="bg-shapes">
        <div class="bg-shape bg-s1"></div>
        <div class="bg-shape bg-s2"></div>
    </div>
    """, unsafe_allow_html=True)

def _palette(light: bool) -> dict:
    if light:
        return {
            "bg": "#faf5f5",
            "surface": "#ffffff",
            "card": "rgba(255, 255, 255, 0.8)",
            "card_solid": "#ffffff",
            "text": "#2d2327",
            "muted": "#6a575e",
            "border": "rgba(232, 187, 198, 0.6)",
            "accent": "#d87a93",
            "accent2": "#e2a999",
            "accent_subtle": "rgba(216, 122, 147, 0.15)",
            "shadow": "rgba(216, 122, 147, 0.12)",
            "shadow_hover": "rgba(216, 122, 147, 0.25)",
            "nav_text": "#4d3d44",
            "nav_hover": "rgba(216, 122, 147, 0.15)",
            "nav_active": "rgba(216, 122, 147, 0.3)",
            "input_bg": "rgba(255,255,255,0.9)",
            "input_text": "#2d2327",
            "button_bg": "#d87a93",
            "button_text": "#ffffff",
        }
    return {
        "bg": "#1e171a",
        "surface": "#2a2125",
        "card": "rgba(42, 33, 37, 0.6)",
        "card_solid": "#2a2125",
        "text": "#fcf5f7",
        "muted": "#aa929a",
        "border": "rgba(232, 135, 160, 0.2)",
        "accent": "#f092ab",
        "accent2": "#f5c3b3",
        "accent_subtle": "rgba(240, 146, 171, 0.15)",
        "shadow": "rgba(0, 0, 0, 0.4)",
        "shadow_hover": "rgba(240, 146, 171, 0.3)",
        "nav_text": "#ccb8bf",
        "nav_hover": "rgba(240, 146, 171, 0.15)",
        "nav_active": "rgba(240, 146, 171, 0.25)",
        "input_bg": "rgba(42, 33, 37, 0.8)",
        "input_text": "#fcf5f7",
        "button_bg": "#f092ab",
        "button_text": "#1e171a",
    }

def _inject_scroll_observer():
    components.html("""
    <script>
    (function(){
        const doc = window.parent.document;
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(e => {
                if (e.isIntersecting) {
                    e.target.classList.add('revealed');
                }
            });
        }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
        doc.querySelectorAll('.reveal').forEach(el => observer.observe(el));
        const mo = new MutationObserver(() => {
            doc.querySelectorAll('.reveal:not(.revealed)').forEach(el => observer.observe(el));
        });
        mo.observe(doc.body, { childList: true, subtree: true });
    })();
    </script>
    """, height=0)

def _clean_html(html_str: str) -> str:
    import re
    return re.sub(r'^\s+', '', html_str, flags=re.MULTILINE).strip()

def render_topbar(title: str, subtitle: str, icon_name: str = "zap") -> None:
    icon = get_icon(icon_name, 22)
    st.markdown(_clean_html(f"""
    <div class="topbar">
        <div class="topbar-icon">{icon}</div>
        <div class="topbar-body">
            <strong>{title}</strong>
            <p>{subtitle}</p>
        </div>
    </div>
    """), unsafe_allow_html=True)

def render_typing_hero(name: str, subtitle: str) -> None:
    played = st.session_state.get("_typing_played", False)
    if not played:
        st.session_state["_typing_played"] = True
        st.markdown(_clean_html(f"""
        <div class="hero-section">
            <div class="typing-wrapper">
                <span class="typing-text">Hi, I'm {name}</span>
            </div>
            <div class="hero-subtitle">{subtitle}</div>
        </div>
        """), unsafe_allow_html=True)
    else:
        st.markdown(_clean_html(f"""
        <div class="hero-section">
            <div class="hero-title-static">Hi, I'm {name}</div>
            <div class="hero-subtitle-static">{subtitle}</div>
        </div>
        """), unsafe_allow_html=True)

def render_section_header(text: str, icon_name: str = "hash") -> None:
    icon = get_icon(icon_name, 20)
    st.markdown(_clean_html(f"""
    <div class="section-hdr">
        <div class="sh-icon">{icon}</div>
        <h2>{text}</h2>
    </div>
    """), unsafe_allow_html=True)

def render_glass_card(content_html: str, icon_name: Optional[str] = None) -> None:
    content_html = _clean_html(content_html)
    icon_block = ""
    if icon_name:
        icon_block = f'<div class="card-icon-badge">{get_icon(icon_name, 22)}</div>'
    st.markdown(_clean_html(f"""
    <div class="glass-card reveal">
        {icon_block}
        {content_html}
    </div>
    """), unsafe_allow_html=True)

def render_interest_card_html(icon_name: str, title: str, desc: str) -> str:
    icon = get_icon(icon_name, 22)
    return _clean_html(f"""
    <div class="glass-card reveal">
        <div class="card-icon-badge">{icon}</div>
        <h3>{title}</h3>
        <p>{desc}</p>
    </div>
    """)

def render_skill_bar(label: str, value: int, icon_name: str = "zap") -> None:
    icon = get_icon(icon_name, 16)
    st.markdown(_clean_html(f"""
    <div class="skill-bar reveal">
        <div class="skill-bar-header">
            <span class="skill-bar-label">{icon} {label}</span>
            <span class="skill-bar-value">{value}%</span>
        </div>
        <div class="skill-bar-track">
            <div class="skill-bar-fill" style="--bar-w:{value}%;"></div>
        </div>
    </div>
    """), unsafe_allow_html=True)

def render_divider() -> None:
    st.markdown('<hr class="styled-hr">', unsafe_allow_html=True)

def render_info_card(icon_name: str, text_html: str) -> None:
    text_html = _clean_html(text_html)
    icon = get_icon(icon_name, 20)
    st.markdown(_clean_html(f"""
    <div class="info-card reveal">
        <div class="ic-icon">{icon}</div>
        <div>{text_html}</div>
    </div>
    """), unsafe_allow_html=True)
