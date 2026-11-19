import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import base64
from pathlib import Path
from PIL import Image

# -----------------------------------------------------------------------------
# BeamStat | Streamlit prototype
# Keep this Python file, COMPROG.png, and COMPROG.jpg in the same folder.
# Replace the creator placeholders in CONTACT_CREATORS with your actual names.
# -----------------------------------------------------------------------------
st.set_page_config(page_title="BeamStat | Beam Analysis Simulator", page_icon="🏗️", layout="wide")
BASE = Path(__file__).resolve().parent
LOGO_PATH = BASE / "COMPROG.png"       # legacy/fallback logo
LIGHT_LOGO_PATH = BASE / "comprog (2).png"
DARK_LOGO_PATH = BASE / "comprog (3).png"
HERO_PATH = BASE / "COMPROG.jpg"       # original BeamStat construction hero image

CONTACT_CREATORS = [
     {"name": "Ramirez, John Emmanuel", "role": "Project Manager & Workflow lead", "email": "johnemmanuelr1@gmail.com"},
  {"name": "Lagunzad, John Roldan", "role": "Project Manager & Workflow Lead", "email": "lagunzad.johnroldan.ce@gmail.com"},
   {"name": "Miranda, Chester Kyle", "role": "CE Technical Specialist / Formulas Analysis", "email": "miranda.chesterkyle.ce@gmail.com"},
    {"name": "Lahora, Jasmine Blythe", "role": "CE Technical Specialist / Formulas Analys", "email": "jlahora11@gmail.com"},
    {"name": "Bullon, Ella", "role": "UI/UX Designer", "email": "bullonella023@gmail.com"},
    {"name": "Reago, Princess Camille T. ", "role": "Quality Assurance & Testing Engineer", "email": "camillereago25@gmail.com"},
    {"name": "Benavidez, Rued Aeislley", "role": "Data & I/O Integration Specialist", "email": "Ruedaeislley@gmail.com"},
    {"name": "Darilag, Rizza Joy C. ", "role": "Documentation & Presentation Lead", "email": "rizzajoydarilag@gmail.com"},
]

def image_to_base64(path):
    """Encode a local logo so both theme variants can be embedded in the header."""
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# Load whichever theme logos are available. The old COMPROG.png remains a fallback.
light_logo_path = LIGHT_LOGO_PATH if LIGHT_LOGO_PATH.exists() else LOGO_PATH
dark_logo_path = DARK_LOGO_PATH if DARK_LOGO_PATH.exists() else LOGO_PATH
light_logo_data = image_to_base64(light_logo_path) if light_logo_path.exists() else None
dark_logo_data = image_to_base64(dark_logo_path) if dark_logo_path.exists() else None

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Poppins:wght@500;600;700;800;900&display=swap');
:root{--blue:#08519C;--navy:#173B5E;--pale:#EFF3FF;--line:#C6DBEF;--muted:#49677F;--palette-1:#EFF3FF;--palette-2:#C6DBEF;--palette-3:#9ECAE1;--palette-4:#6BAED6;--palette-5:#3182BD;--palette-6:#08519C}
html,body,[class*="css"]{font-family:'Inter',sans-serif}
.stApp{background:#fff;color:#10213d}
.block-container{max-width:1500px;padding-top:1.1rem;padding-bottom:2rem}
#MainMenu,footer{visibility:hidden}
header[data-testid="stHeader"]{background:transparent}
/* Navigation buttons intentionally have no filled background. */
div.stButton>button{background:transparent!important;color:#111827!important;border:0!important;
 box-shadow:none!important;border-radius:0!important;font-size:12px;font-weight:700;padding:.35rem .25rem}
div.stButton>button:hover{color:var(--blue)!important;border-bottom:2px solid var(--blue)!important}
.navline{border-bottom:1px solid #e8eef7;margin:0 0 1rem 0}
.brand-fallback{font-size:19px;font-weight:900;color:#111;display:flex;align-items:center;gap:8px}
.hero{display:grid;grid-template-columns:1.02fr 1fr;min-height:420px;align-items:center;gap:1rem;margin-bottom:1.3rem}
.hero-copy{padding:30px 0 30px 12px;z-index:2;animation:heroFadeUp 1.05s ease-out both}
.eyebrow{font-style:italic;color:#064ca8;font-size:15px;margin-bottom:10px;animation:heroFadeUp 1s ease-out both}
.hero-title{font-family:'Poppins',sans-serif;font-size:85px;line-height:1.02;color:var(--blue);font-weight:900;letter-spacing:-4px;margin:0 0 8px;animation:heroFadeUp 1.15s ease-out both}
.hero-tag{font-family:'Poppins',sans-serif;font-size:39px;line-height:1.08;font-weight:700;color:#050505;letter-spacing:-1.5px;margin:0 0 14px;animation:heroFadeUp 1.2s .12s ease-out both}
.hero-desc{font-size:15px;line-height:1.65;max-width:470px;color:#1f2937;animation:heroFadeUp 1.2s .22s ease-out both}
.hero-photo{height:410px;background-position:center;background-size:cover;position:relative;animation:heroFadeIn 1.5s .2s ease-out both}
.hero-photo:before{content:"";position:absolute;inset:0;background:linear-gradient(90deg,#fff 0%,rgba(255,255,255,.88) 8%,rgba(255,255,255,.12) 45%,transparent 68%)}
@keyframes heroFadeUp{
  from{opacity:0;transform:translateY(24px)}
  to{opacity:1;transform:translateY(0)}
}
@keyframes heroFadeIn{
  from{opacity:0}
  to{opacity:1}
}
@media(prefers-reduced-motion:reduce){
  .hero-copy,.eyebrow,.hero-title,.hero-tag,.hero-desc,.hero-photo{
    animation:none!important;opacity:1!important;transform:none!important
  }
}
.section-title{font-size:27px;font-weight:800;color:var(--navy);margin:.2rem 0 1rem}
.panel{background:#fff;border:1px solid var(--line);border-radius:12px;padding:15px 16px;margin-bottom:12px;box-shadow:0 2px 10px rgba(15,65,130,.025)}
.panel-title{font-size:35px;font-weight:800;color:var(--navy);margin-bottom:10px}
.metric-card{background:linear-gradient(145deg,#f7faff,#edf5ff);border:1px solid #e0ebfa;border-radius:10px;padding:12px 14px;min-height:90px}
.metric-label{font-size:12px;color:#23416d;font-weight:700}.metric-value{font-size:22px;color:#064bb0;font-weight:800;margin-top:4px}.metric-unit{font-size:11px;color:#64748b}
.small-note{font-size:12px;color:#64748b}
div[data-testid="stSelectbox"] label,div[data-testid="stNumberInput"] label{font-size:12px;font-weight:600;color:#20395f}
.stAlert{border-radius:10px}
@media(max-width:900px){.hero{grid-template-columns:1fr}.hero-photo{height:260px}.hero-title{font-size:62px;letter-spacing:-2.5px}.hero-tag{font-size:30px}}

/* ================= THEME + RESPONSIVE ACCESSIBILITY OVERRIDES ================= */
/* Use Streamlit's active theme variables so text follows the selected app theme. */
:root {
  color-scheme: light dark;
  --bs-bg: var(--background-color, #ffffff);
  --bs-secondary: var(--secondary-background-color, #f4f7fb);
  --bs-text: var(--text-color, #172033);
  --bs-muted: color-mix(in srgb, var(--bs-text) 68%, transparent);
  --bs-border: color-mix(in srgb, var(--bs-text) 18%, transparent);
  --bs-blue: #3182BD;
  --bs-panel: var(--secondary-background-color, #f7faff);
}
.stApp, [data-testid="stAppViewContainer"] {
  background: var(--bs-bg) !important;
  color: var(--bs-text) !important;
}
.stApp p, .stApp li, .stApp label, .stApp span, .stApp small,
.stApp [data-testid="stMarkdownContainer"] {
  color: inherit;
}
.stApp h1, .stApp h2, .stApp h3, .stApp h4,
.section-title, .panel-title {
  color: var(--bs-text) !important;
}
.panel, .metric-card {
  background: var(--bs-secondary) !important;
  color: var(--bs-text) !important;
  border-color: var(--bs-border) !important;
  box-shadow: 0 2px 10px rgba(0,0,0,.06);
}
.metric-label, .metric-unit, .small-note,
div[data-testid="stSelectbox"] label,
div[data-testid="stNumberInput"] label {
  color: var(--bs-muted) !important;
}
.metric-value, .hero-title { color: var(--bs-blue) !important; }
.hero-tag { color: var(--bs-text) !important; }
.hero-desc { color: var(--bs-text) !important; }
.eyebrow { color: var(--bs-blue) !important; }
.navline { border-color: var(--bs-border) !important; }
.brand-fallback { color: var(--bs-text) !important; }

/* Streamlit inputs, dropdowns, tabs and buttons */
.stApp input, .stApp textarea,
.stApp [data-baseweb="select"] > div,
.stApp [data-baseweb="input"] > div,
.stApp [data-baseweb="textarea"] > div {
  color: var(--bs-text) !important;
  background-color: var(--bs-secondary) !important;
  border-color: var(--bs-border) !important;
}
.stApp [data-baseweb="select"] *,
.stApp [data-baseweb="popover"] *,
.stApp [role="listbox"] *,
.stApp [role="option"] {
  color: var(--bs-text) !important;
}
.stApp button[kind], .stApp .stButton > button {
  color: var(--bs-text);
  border-color: var(--bs-border);
}
.stApp .stButton > button[kind="primary"] {
  color: white !important;
}
.stApp [data-testid="stDataFrame"],
.stApp [data-testid="stTable"] {
  color: var(--bs-text);
}
.stApp hr { border-color: var(--bs-border) !important; }

/* Hero image overlay adapts to dark backgrounds. */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) .hero-photo:before,
  body:not([data-theme="light"]) .hero-photo:before {
    background: linear-gradient(90deg, rgba(14,18,28,.98) 0%,
      rgba(14,18,28,.82) 8%, rgba(14,18,28,.18) 48%, transparent 72%);
  }
}
/* Explicit dark theme selectors used by Streamlit versions. */
[data-theme="dark"] .hero-photo:before,
body[data-theme="dark"] .hero-photo:before,
html[data-theme="dark"] .hero-photo:before {
  background: linear-gradient(90deg, rgba(14,18,28,.98) 0%,
    rgba(14,18,28,.82) 8%, rgba(14,18,28,.18) 48%, transparent 72%) !important;
}
[data-theme="dark"] .hero-tag,
[data-theme="dark"] .hero-desc { color: #f1f5f9 !important; }

/* Small-screen layout: prevent horizontal overflow and make controls tappable. */
@media (max-width: 760px) {
  .block-container {
    padding-left: 1rem !important;
    padding-right: 1rem !important;
    padding-top: .6rem !important;
  }
  .hero { display: flex !important; flex-direction: column !important; gap: .5rem !important; min-height: 0 !important; }
  .hero-copy { padding: 18px 2px 8px !important; width: 100% !important; }
  .hero-title { font-size: clamp(2.8rem, 14vw, 4.2rem) !important; letter-spacing: -2px !important; overflow-wrap: anywhere; }
  .hero-tag { font-size: clamp(1.55rem, 7vw, 2rem) !important; }
  .hero-desc { font-size: 14px !important; }
  .hero-photo { width: 100% !important; height: 210px !important; border-radius: 12px; }
  .section-title { font-size: 23px !important; }
  .panel { padding: 12px !important; }
  .metric-card { min-height: 76px !important; padding: 10px !important; }
  .metric-value { font-size: 19px !important; overflow-wrap: anywhere; }
  .stButton > button { min-height: 42px !important; white-space: normal !important; }
  .stNumberInput input, .stTextInput input, .stSelectbox [role="combobox"] {
    min-height: 42px !important;
  }
  [data-testid="stHorizontalBlock"] { flex-wrap: wrap !important; gap: .45rem !important; }
  [data-testid="column"] { min-width: min(100%, 145px) !important; flex: 1 1 145px !important; }
  [data-testid="stPlotlyChart"], [data-testid="stImage"] { max-width: 100% !important; }
  .stDataFrame, [data-testid="stDataFrame"] { overflow-x: auto !important; }
}
@media (max-width: 420px) {
  .block-container { padding-left: .7rem !important; padding-right: .7rem !important; }
  .hero-photo { height: 175px !important; }
  .panel-title { font-size: 15px !important; }
  .small-note { font-size: 11px !important; }
}
/* ============================================================================ */


/* Slightly larger logo, with mobile-safe header spacing. */
div[data-testid="stImage"] img { max-width: 100%; height: auto; }
@media (max-width: 760px) {
  div[data-testid="stImage"] img { max-width: 118px; }
}


/* ================= BEAMSTAT PALETTE + HIGH-CONTRAST CONTROLS ================= */
:root {
  --bs-palette-1: #EFF3FF;
  --bs-palette-2: #C6DBEF;
  --bs-palette-3: #9ECAE1;
  --bs-palette-4: #6BAED6;
  --bs-palette-5: #3182BD;
  --bs-palette-6: #08519C;
  --bs-action: #08519C;
  --bs-action-hover: #3182BD;
}
.stApp {
  --bs-readable: #000000;
}
.stApp [data-testid="stExpander"] summary,
.stApp [data-testid="stExpander"] summary *,
.stApp [data-testid="stWidgetLabel"],
.stApp [data-testid="stWidgetLabel"] *,
.stApp label,
.stApp .stMarkdown,
.stApp .stMarkdown p,
.stApp .stMarkdown li,
.stApp [data-testid="stCaptionContainer"],
.stApp [data-testid="stCaptionContainer"] *,
.stApp [data-testid="stNumberInput"] *,
.stApp [data-testid="stTextInput"] *,
.stApp [data-testid="stSelectbox"] *,
.stApp [data-testid="stMultiSelect"] * {
  color: var(--bs-readable) !important;
  opacity: 1 !important;
}
.stApp [data-testid="stExpander"] summary {
  font-weight: 700 !important;
}
.stApp .stButton > button[kind="primary"],
.stApp button[kind="primary"],
.stApp [data-testid="stFormSubmitButton"] button {
  background: var(--bs-action) !important;
  color: #FFFFFF !important;
  border: 1px solid var(--bs-action) !important;
  font-weight: 800 !important;
  opacity: 1 !important;
}
.stApp .stButton > button[kind="primary"] *,
.stApp button[kind="primary"] *,
.stApp [data-testid="stFormSubmitButton"] button * {
  color: #FFFFFF !important;
  opacity: 1 !important;
}
.stApp .stButton > button[kind="primary"]:hover,
.stApp button[kind="primary"]:hover {
  background: var(--bs-action-hover) !important;
  border-color: var(--bs-action-hover) !important;
}
.stApp .stButton > button:not([kind="primary"]) {
  color: var(--bs-readable) !important;
  border-color: var(--bs-palette-2) !important;
}
.stApp input, .stApp textarea,
.stApp [data-baseweb="select"] > div,
.stApp [data-baseweb="input"] > div {
  color: var(--bs-readable) !important;
  caret-color: var(--bs-readable) !important;
}
.stApp [data-testid="stExpander"] {
  border-color: var(--bs-palette-2) !important;
}
.stApp a { color: var(--bs-palette-5) !important; }
[data-theme="light"] .stApp {
  --bs-readable: #000000;
  --bs-action: #08519C;
  --bs-action-hover: #3182BD;
}
[data-theme="dark"] .stApp,
body[data-theme="dark"] .stApp {
  --bs-readable: #FFFFFF;
  --bs-action: #3182BD;
  --bs-action-hover: #6BAED6;
}
[data-theme="dark"] .stApp .stButton > button[kind="primary"]:hover,
body[data-theme="dark"] .stApp .stButton > button[kind="primary"]:hover {
  color: #102B45 !important;
}
[data-theme="dark"] .stApp .stButton > button[kind="primary"]:hover * {
  color: #102B45 !important;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) .stApp {
    --bs-readable: #FFFFFF;
    --bs-action: #3182BD;
    --bs-action-hover: #6BAED6;
  }
}
/* ============================================================================ */


/* FINAL TEXT CONTRAST: BLACK IN LIGHT MODE, WHITE IN DARK MODE */
[data-theme="light"] .stApp,
[data-theme="light"] .stApp p,
[data-theme="light"] .stApp span,
[data-theme="light"] .stApp label,
[data-theme="light"] .stApp li,
[data-theme="light"] .stApp [data-testid="stMarkdownContainer"],
[data-theme="light"] .stApp [data-testid="stWidgetLabel"],
[data-theme="light"] .stApp [data-testid="stExpander"] summary,
[data-theme="light"] .stApp [data-testid="stCaptionContainer"] {
  color: #000000 !important;
}
[data-theme="dark"] .stApp,
[data-theme="dark"] .stApp p,
[data-theme="dark"] .stApp span,
[data-theme="dark"] .stApp label,
[data-theme="dark"] .stApp li,
[data-theme="dark"] .stApp [data-testid="stMarkdownContainer"],
[data-theme="dark"] .stApp [data-testid="stWidgetLabel"],
[data-theme="dark"] .stApp [data-testid="stExpander"] summary,
[data-theme="dark"] .stApp [data-testid="stCaptionContainer"] {
  color: #FFFFFF !important;
}
.stApp .stButton > button[kind="primary"],
.stApp .stButton > button[kind="primary"] *,
.stApp [data-testid="stFormSubmitButton"] button,
.stApp [data-testid="stFormSubmitButton"] button * {
  color: #FFFFFF !important;
}

</style>
""", unsafe_allow_html=True)

# A final theme-aware layer. Streamlit exposes its active theme colors as CSS
# variables on the app; the fallback colors cover versions where they are absent.
_THEME_BASE = (st.get_option("theme.base") or "light").lower()
_DARK_FALLBACK = _THEME_BASE == "dark"
if _DARK_FALLBACK:
    _FALLBACK_BG = "#101827"
    _FALLBACK_SECONDARY = "#1B2A40"
    _FALLBACK_TEXT = "#EFF3FF"
    _FALLBACK_MUTED = "#C6DBEF"
else:
    _FALLBACK_BG = "#FFFFFF"
    _FALLBACK_SECONDARY = "#EFF3FF"
    _FALLBACK_TEXT = "#000000"
    _FALLBACK_MUTED = "#334155"

st.markdown(f"""
<style>
/* ================= FINAL BEAMSTAT THEME FIX ================= */
.stApp {{
  --bs-bg: var(--background-color, {_FALLBACK_BG});
  --bs-secondary: var(--secondary-background-color, {_FALLBACK_SECONDARY});
  --bs-text: var(--text-color, {_FALLBACK_TEXT});
  --bs-muted: color-mix(in srgb, var(--bs-text) 76%, transparent);
  --bs-border: color-mix(in srgb, var(--bs-text) 24%, transparent);
  --bs-accent: #3182BD;
  background: var(--bs-bg) !important;
  color: var(--bs-text) !important;
}}

/* App canvas and all standard text surfaces */
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"],
[data-testid="stHeader"] {{
  background-color: var(--bs-bg) !important;
  color: var(--bs-text) !important;
}}
.stApp h1, .stApp h2, .stApp h3, .stApp h4,
.stApp p, .stApp li, .stApp label, .stApp small,
.stApp [data-testid="stMarkdownContainer"],
.stApp [data-testid="stWidgetLabel"],
.stApp [data-testid="stCaptionContainer"],
.stApp [data-testid="stExpander"] summary,
.stApp [data-testid="stExpander"] summary span {{
  color: var(--bs-text) !important;
  opacity: 1 !important;
}}

/* Custom BeamStat cards */
.stApp .panel, .stApp .metric-card,
.stApp [data-testid="stVerticalBlockBorderWrapper"],
.stApp [data-testid="stExpander"] {{
  background: var(--bs-secondary) !important;
  color: var(--bs-text) !important;
  border-color: var(--bs-border) !important;
}}
.stApp .panel-title, .stApp .metric-label,
.stApp .metric-unit, .stApp .small-note {{
  color: var(--bs-text) !important;
}}
.stApp .metric-value, .stApp .hero-title, .stApp .eyebrow {{
  color: var(--bs-accent) !important;
}}
.stApp .hero-tag, .stApp .hero-desc, .stApp .section-title {{
  color: var(--bs-text) !important;
}}

/* Text, number, and select inputs: readable text on a matching surface */
.stApp input, .stApp textarea,
.stApp [data-baseweb="input"] > div,
.stApp [data-baseweb="textarea"] > div,
.stApp [data-baseweb="select"] > div,
.stApp [data-testid="stNumberInput"] input,
.stApp [data-testid="stTextInput"] input {{
  background-color: var(--bs-secondary) !important;
  color: var(--bs-text) !important;
  -webkit-text-fill-color: var(--bs-text) !important;
  border-color: var(--bs-border) !important;
  caret-color: var(--bs-text) !important;
  opacity: 1 !important;
}}
.stApp input::placeholder, .stApp textarea::placeholder {{
  color: var(--bs-muted) !important;
  -webkit-text-fill-color: var(--bs-muted) !important;
  opacity: 1 !important;
}}
.stApp [data-baseweb="select"] *,
.stApp [role="listbox"] *, .stApp [role="option"] {{
  color: var(--bs-text) !important;
}}
.stApp [data-baseweb="popover"],
.stApp [data-baseweb="menu"] {{
  background: var(--bs-secondary) !important;
}}

/* Number-input stepper controls */
.stApp [data-testid="stNumberInput"] button {{
  background: var(--bs-secondary) !important;
  color: var(--bs-text) !important;
  border-color: var(--bs-border) !important;
}}

/* Buttons: blue primary action with white text; other buttons follow theme */
.stApp .stButton > button {{
  color: var(--bs-text) !important;
  border-color: var(--bs-border) !important;
}}
.stApp .stButton > button[kind="primary"],
.stApp [data-testid="stFormSubmitButton"] button {{
  background: #08519C !important;
  color: #FFFFFF !important;
  border: 1px solid #08519C !important;
}}
.stApp .stButton > button[kind="primary"] *,
.stApp [data-testid="stFormSubmitButton"] button * {{
  color: #FFFFFF !important;
}}

/* Alerts, separators, and tables */
.stApp [data-testid="stAlert"],
.stApp [data-testid="stMetric"] {{
  color: var(--bs-text) !important;
}}
.stApp hr, .stApp table, .stApp th, .stApp td {{
  border-color: var(--bs-border) !important;
  color: var(--bs-text) !important;
}}
.stApp a {{ color: #3182BD !important; }}
.stApp .navline {{ border-color: var(--bs-border) !important; }}

/* Dark mode: explicitly override legacy white backgrounds and black text. */
[data-theme="dark"] .stApp,
html[data-theme="dark"] .stApp,
body[data-theme="dark"] .stApp {{
  --bs-bg: #101827;
  --bs-secondary: #1B2A40;
  --bs-text: #EFF3FF;
  --bs-muted: #C6DBEF;
  --bs-border: #49677F;
  --bs-accent: #9ECAE1;
}}
[data-theme="dark"] .stApp .hero-photo:before,
html[data-theme="dark"] .stApp .hero-photo:before,
body[data-theme="dark"] .stApp .hero-photo:before {{
  background: linear-gradient(90deg, rgba(16,24,39,.98) 0%,
    rgba(16,24,39,.82) 8%, rgba(16,24,39,.18) 48%, transparent 72%) !important;
}}

/* Also respect operating-system dark mode when Streamlit theme is set to Auto. */
@media (prefers-color-scheme: dark) {{
  html:not([data-theme="light"]) .stApp {{
    --bs-bg: #101827;
    --bs-secondary: #1B2A40;
    --bs-text: #EFF3FF;
    --bs-muted: #C6DBEF;
    --bs-border: #49677F;
    --bs-accent: #9ECAE1;
  }}
  html:not([data-theme="light"]) .stApp .hero-photo:before {{
    background: linear-gradient(90deg, rgba(16,24,39,.98) 0%,
      rgba(16,24,39,.82) 8%, rgba(16,24,39,.18) 48%, transparent 72%) !important;
  }}
}}
/* Theme-aware logo: light logo by default, dark logo for dark theme. */
.beamstat-logo-wrap {{ display:flex; align-items:center; min-height:48px; }}
.beamstat-theme-logo {{ width:155px; max-width:100%; height:auto; object-fit:contain; }}
.beamstat-logo-dark {{ display:none !important; }}
.beamstat-logo-light {{ display:block !important; }}
html[data-theme="dark"] .beamstat-logo-light,
body[data-theme="dark"] .beamstat-logo-light,
[data-theme="dark"] .beamstat-logo-light {{ display:none !important; }}
html[data-theme="dark"] .beamstat-logo-dark,
body[data-theme="dark"] .beamstat-logo-dark,
[data-theme="dark"] .beamstat-logo-dark {{ display:block !important; }}
@media (prefers-color-scheme: dark) {{
  html:not([data-theme="light"]) .beamstat-logo-light {{ display:none !important; }}
  html:not([data-theme="light"]) .beamstat-logo-dark {{ display:block !important; }}
}}
@media (max-width:760px) {{ .beamstat-theme-logo {{ width:118px; }} }}
/* ============================================================= */
</style>
""", unsafe_allow_html=True)

# Session navigation
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Header: exact uploaded logo file, plus transparent clickable nav.
nav_cols = st.columns([2.5, .8, .9, .7, .9])
with nav_cols[0]:
    if light_logo_data and dark_logo_data:
        st.markdown(
            f'''
            <div class="beamstat-logo-wrap">
              <img class="beamstat-theme-logo beamstat-logo-light"
                   src="data:image/png;base64,{light_logo_data}" alt="BeamStat logo for light mode">
              <img class="beamstat-theme-logo beamstat-logo-dark"
                   src="data:image/png;base64,{dark_logo_data}" alt="BeamStat logo for dark mode">
            </div>
            ''',
            unsafe_allow_html=True,
        )
    else:
        st.markdown('<div class="brand-fallback">▰ BeamStat</div>', unsafe_allow_html=True)
for col, label in zip(nav_cols[1:], ["HOME", "SIMULATOR", "ABOUT", "CONTACT"]):
    with col:
        if st.button(label, key=f"nav_{label}", use_container_width=True):
            st.session_state.page = {"HOME":"Home","SIMULATOR":"Simulator","ABOUT":"About","CONTACT":"Contact"}[label]
            st.session_state["_beamstat_nav_fade"] = True
            st.rerun()
st.markdown('<div class="navline"></div>', unsafe_allow_html=True)

# Apply the page transition only after a navigation action. Ordinary widget
# changes (such as editing loads or calculating reactions) will not replay it.
if st.session_state.pop("_beamstat_nav_fade", False):
    st.markdown("""
    <style>
    @keyframes beamstatPageFade {
      from { opacity: 0; transform: translateY(10px); }
      to   { opacity: 1; transform: translateY(0); }
    }
    div[data-testid="stMainBlockContainer"] {
      animation: beamstatPageFade 480ms ease-out both;
    }
    @media (prefers-reduced-motion: reduce) {
      div[data-testid="stMainBlockContainer"] { animation: none !important; }
    }
    </style>
    """, unsafe_allow_html=True)


def distributed_intensity(load, x):
    """Return the nonnegative load intensity (kN/m) at coordinate x."""
    a, b = float(load["a"]), float(load["b"])
    x = np.asarray(x, dtype=float)
    shape = load.get("type", "rectangular")
    wmax = float(load.get("wmax", max(load.get("w0", 0.0), load.get("w1", 0.0))))
    if shape == "tent":
        peak = float(load["peak_x"])
        left_ratio = np.clip((x-a) / max(peak-a, 1e-12), 0.0, 1.0)
        right_ratio = np.clip((b-x) / max(b-peak, 1e-12), 0.0, 1.0)
        return wmax * np.where(x <= peak, left_ratio, right_ratio)
    if shape == "triangular_increasing":
        return wmax * np.clip((x-a) / max(b-a, 1e-12), 0.0, 1.0)
    if shape == "triangular_decreasing":
        return wmax * np.clip((b-x) / max(b-a, 1e-12), 0.0, 1.0)
    if shape == "triangular":  # backward compatibility with earlier saved settings
        w0, w1 = float(load.get("w0", 0.0)), float(load.get("w1", wmax))
        return w0 + (w1-w0)*(x-a)/max(b-a, 1e-12)
    return np.full_like(x, wmax, dtype=float)


def distributed_load_integrals(load, x0=None, x1=None):
    """Return signed resultant, moment about A, and moment about section x1."""
    a, b = float(load["a"]), float(load["b"])
    lo = a if x0 is None else max(a, float(x0))
    hi = b if x1 is None else min(b, float(x1))
    if hi <= lo or b <= a:
        return 0.0, 0.0, 0.0
    direction = 1.0 if load.get("direction", "Downward") == "Upward" else -1.0
    # Split at the tent peak so each integration interval has a linear intensity.
    cuts = [lo, hi]
    if load.get("type") == "tent":
        peak = float(load["peak_x"])
        if lo < peak < hi:
            cuts.insert(1, peak)
    pts = np.array([-np.sqrt(3/5), 0.0, np.sqrt(3/5)])
    weights = np.array([5/9, 8/9, 5/9])
    force = moment_A = moment_cut = 0.0
    for left, right in zip(cuts[:-1], cuts[1:]):
        xs = (right+left)/2 + (right-left)/2*pts
        signed_q = direction * distributed_intensity(load, xs)
        scale = (right-left)/2
        force += scale * np.sum(weights*signed_q)
        moment_A += scale * np.sum(weights*signed_q*xs)
        if x1 is not None:
            moment_cut += scale * np.sum(weights*signed_q*(float(x1)-xs))
    return float(force), float(moment_A), float(moment_cut)


def solve_beam(L, supports, point_loads, distributed_loads, applied_moment, EI):
    """Euler-Bernoulli beam FE model with point and linearly varying loads."""
    support_positions = [float(s["x"]) for s in supports]
    load_bounds = [v for load in distributed_loads for v in (float(load["a"]), float(load["b"]))]
    load_peaks = [float(load["peak_x"]) for load in distributed_loads if load.get("type") == "tent"]
    nodes = sorted(set([0.0, float(L)] + support_positions
                       + [float(x) for _, x in point_loads] + load_bounds + load_peaks + [float(L)/2]))
    n = len(nodes)
    K = np.zeros((2*n, 2*n), dtype=float)
    F = np.zeros(2*n, dtype=float)
    gauss_pts = np.array([-np.sqrt(3/5), 0.0, np.sqrt(3/5)])
    gauss_weights = np.array([5/9, 8/9, 5/9])

    for e in range(n-1):
        xL, xR = nodes[e], nodes[e+1]
        le = xR - xL
        if le <= 1e-10:
            continue
        ke = EI / le**3 * np.array([
            [12, 6*le, -12, 6*le], [6*le, 4*le**2, -6*le, 2*le**2],
            [-12, -6*le, 12, -6*le], [6*le, 2*le**2, -6*le, 4*le**2]
        ], dtype=float)
        dofs = [2*e, 2*e+1, 2*(e+1), 2*(e+1)+1]
        K[np.ix_(dofs, dofs)] += ke
        # Consistent element load vector: integrate Hermite shape functions
        # against the actual linear intensity over this element.
        for load in distributed_loads:
            if xL >= load["a"]-1e-9 and xR <= load["b"]+1e-9:
                direction = 1.0 if load.get("direction", "Downward") == "Upward" else -1.0
                for gp, gw in zip(gauss_pts, gauss_weights):
                    xi = (gp+1)/2
                    x = xL + xi*le
                    wmag = float(distributed_intensity(load, x))
                    q = direction*wmag
                    N = np.array([1-3*xi**2+2*xi**3,
                                  le*(xi-2*xi**2+xi**3),
                                  3*xi**2-2*xi**3,
                                  le*(-xi**2+xi**3)])
                    F[dofs] += N*q*gw*le/2

    for p, x in point_loads:
        idx = min(range(n), key=lambda i: abs(nodes[i]-x))
        F[2*idx] -= p
    mid_idx = min(range(n), key=lambda i: abs(nodes[i] - L/2))
    F[2*mid_idx+1] += applied_moment

    restrained, support_node_indices = [], []
    for support in supports:
        idx = min(range(n), key=lambda i: abs(nodes[i]-float(support["x"])))
        support_node_indices.append(idx)
        restrained.append(2*idx)
        if support["type"] == "Fixed":
            restrained.append(2*idx+1)
    restrained = sorted(set(restrained))
    free = [i for i in range(2*n) if i not in restrained]
    d = np.zeros(2*n)
    Kff = K[np.ix_(free, free)]
    if np.linalg.matrix_rank(Kff) < len(free):
        raise np.linalg.LinAlgError("The selected support arrangement is unstable. Check support spacing and consider a Fixed support.")
    d[free] = np.linalg.solve(Kff, F[free])
    R = K @ d - F
    support_reactions = []
    for support, idx in zip(supports, support_node_indices):
        support_reactions.append({"label": support["label"], "x": float(support["x"]),
            "type": support["type"], "Ry": float(R[2*idx]),
            "M": float(R[2*idx+1]) if support["type"] == "Fixed" else 0.0})
    return nodes, d, R, support_reactions


if st.session_state.page == "Home":
    if HERO_PATH.exists():
        import base64
        encoded = base64.b64encode(HERO_PATH.read_bytes()).decode()
        hero_style = f"background-image:url(data:image/png;base64,{encoded});"
    else:
        hero_style = "background:linear-gradient(135deg,#e8eef7,#b8c6d6);"
    st.markdown(f"""
    <div class="hero"><div class="hero-copy">
      <div class="eyebrow">Structural Engineering / Statics</div>
      <h1 class="hero-title">BeamStat</h1>
      <div class="hero-tag">Calculate. Visualize.<br>Understand.</div>
      <p class="hero-desc">An interactive simulator for beam reaction and static equilibrium analysis.
      Solve, check, and build your understanding of structural behavior — one beam at a time.</p>
    </div><div class="hero-photo" style="{hero_style}"></div></div>
    """, unsafe_allow_html=True)
    action_cols = st.columns([1, 1, 3])
    with action_cols[0]:
        if st.button("▶  Simulate Here", key="home_simulate", type="primary", use_container_width=True):
            st.session_state.page = "Simulator"
            st.session_state["_beamstat_nav_fade"] = True
            st.rerun()
    with action_cols[1]:
        if st.button("How It Works", key="home_how", use_container_width=True):
            st.session_state.show_how_it_works = not st.session_state.get("show_how_it_works", False)
    if st.session_state.get("show_how_it_works", False):
        with st.container(border=True):
            st.markdown("### How to use BeamStat")
            st.markdown("""
            1. **Set the beam span** in meters.
            2. **Choose the supports** at A and B (Pin, Roller, or Fixed).
            3. **Enter the loads:** point-load magnitudes and positions, UDL intensity and its start/end positions, and an applied moment.
            4. **Click Calculate Reactions** to solve the beam.
            5. **Read the reaction cards** for the vertical reactions and any fixed-support moments.
            6. **Review the beam diagram, equilibrium check, and step-by-step calculations** to understand the result.

            All load inputs start at **zero**, so you can build a problem from scratch. The beam span must remain greater than zero.
            """)
    st.markdown('<h2 class="section-title">What you can do with BeamStat</h2>', unsafe_allow_html=True)
    c1,c2,c3 = st.columns(3)
    for col, title, desc in [
        (c1,"Configure supports","Choose a pin, roller, or fixed support independently at the left and right ends."),
        (c2,"Apply different loads","Enter point loads, a uniformly distributed load, and an applied couple."),
        (c3,"Check your analysis","View support reactions, the beam diagram, equilibrium checks, and calculation steps.")]:
        with col:
            st.markdown(f'<div class="panel"><div class="panel-title">{title}</div><div class="small-note">{desc}</div></div>', unsafe_allow_html=True)

elif st.session_state.page == "Simulator":
    st.markdown('<h1 class="section-title">Beam Reaction Simulator</h1>', unsafe_allow_html=True)
    st.caption("Add two or more supports at any position along the beam, then enter loads and calculate the reactions. This model covers vertical loading and beam bending.")
    input_col, result_col = st.columns([.95, 1.65], gap="medium")
    with input_col:
        st.markdown('<div class="panel-title">⚙️  1. Beam Configuration</div>', unsafe_allow_html=True)
        L = st.number_input("Total beam length L (m)", min_value=0.1, value=8.0, step=0.5, key="beam_length_multi")
        st.markdown("**2. Supports (minimum 2)**")
        st.caption("Click Add Support, then choose its support type and enter its distance from the left end of the beam.")
        if "beamstat_support_rows" not in st.session_state:
            st.session_state.beamstat_support_rows = [
                {"uid": "A", "label": "A", "x": 0.0, "type": "Pin"},
                {"uid": "B", "label": "B", "x": min(6.5, float(L)), "type": "Roller"},
            ]
        if "beamstat_support_counter" not in st.session_state:
            st.session_state.beamstat_support_counter = 0
        if st.button("＋ Add Support", key="add_beam_support", use_container_width=True):
            next_index = len(st.session_state.beamstat_support_rows)
            next_label = chr(65 + next_index) if next_index < 26 else f"S{next_index+1}"
            new_uid = f"support_new_{st.session_state.beamstat_support_counter}"
            st.session_state.beamstat_support_counter += 1
            st.session_state.beamstat_support_rows.append({
                "uid": new_uid,
                "label": next_label,
                "x": round(float(L) * 0.5, 2),
                "type": "Roller",
            })
            st.rerun()

        support_rows_for_solver = []
        for i, support in enumerate(st.session_state.beamstat_support_rows):
            with st.container(border=True):
                st.markdown(f"**Support {i+1}**")
                c_label, c_pos, c_type, c_remove = st.columns([0.8, 1.35, 1.1, 0.65])
                with c_label:
                    label = st.text_input("Label", value=support["label"], key=f"support_label_{support['uid']}", max_chars=8)
                with c_pos:
                    x_value = min(max(float(support["x"]), 0.0), float(L))
                    x = st.number_input("Distance from A (m)", min_value=0.0, max_value=float(L), value=x_value, step=0.5, key=f"support_x_{support['uid']}")
                with c_type:
                    support_type = st.selectbox("Support type", ["Pin", "Roller", "Fixed"], index=["Pin", "Roller", "Fixed"].index(support["type"]), key=f"support_type_{support['uid']}")
                with c_remove:
                    st.write("")
                    st.write("")
                    remove_clicked = st.button("✕", key=f"remove_support_{support['uid']}", disabled=len(st.session_state.beamstat_support_rows) <= 2, help="Remove this support (at least two are required)")
                support_rows_for_solver.append({"Label": label, "Distance from A (m)": x, "Support type": support_type})
                if remove_clicked:
                    st.session_state.beamstat_support_rows.pop(i)
                    st.rerun()
        import pandas as pd
        edited_supports = pd.DataFrame(support_rows_for_solver)

        st.markdown("**3. Analysis Points (with or without supports)**")
        st.caption("These are locations where BeamStat reports internal shear and bending moment. A point does not need to have a support.")
        if "beamstat_analysis_points" not in st.session_state:
            st.session_state.beamstat_analysis_points = [
                {"label": "A", "x": 0.0}, {"label": "B", "x": 2.0},
                {"label": "C", "x": 4.0}, {"label": "D", "x": min(6.5, float(L))}
            ]
        if st.button("＋ Add Analysis Point", key="add_analysis_point", use_container_width=True):
            idx = len(st.session_state.beamstat_analysis_points)
            st.session_state.beamstat_analysis_points.append({"label": chr(65+idx) if idx < 26 else f"P{idx+1}", "x": round(float(L)*0.5, 2)})
            st.rerun()
        analysis_points = []
        for i, point in enumerate(st.session_state.beamstat_analysis_points):
            with st.container(border=True):
                pc1, pc2, pc3 = st.columns([0.8, 1.3, 0.6])
                with pc1:
                    point_label = st.text_input("Point label", value=point["label"], key=f"analysis_label_{i}", max_chars=8)
                with pc2:
                    px = st.number_input("Distance x (m)", min_value=0.0, max_value=float(L), value=min(max(float(point["x"]), 0.0), float(L)), step=0.5, key=f"analysis_x_{i}")
                with pc3:
                    st.write("")
                    if st.button("✕", key=f"remove_analysis_{i}", disabled=len(st.session_state.beamstat_analysis_points) <= 1):
                        st.session_state.beamstat_analysis_points.pop(i)
                        st.rerun()
                analysis_points.append({"label": point_label.strip() or f"P{i+1}", "x": float(px)})

        st.markdown("**4. Applied Point Loads**")
        point_count = st.number_input("Number of point loads", min_value=0, max_value=10, value=2, step=1, key="point_load_count_multi")
        point_loads = []
        for i in range(int(point_count)):
            with st.expander(f"Point Load {i+1}", expanded=(i < 2)):
                pc1, pc2 = st.columns(2)
                with pc1:
                    p = st.number_input(f"P{i+1} (kN, downward)", min_value=0.0, value=0.0, step=1.0, key=f"multi_p_{i}")
                with pc2:
                    x = st.number_input(f"Position x{i+1} (m)", min_value=0.0, max_value=float(L), value=0.0, step=0.5, key=f"multi_x_{i}")
                point_loads.append((p, x))

        st.markdown("**5. Distributed Loads**")
        st.caption("Choose a load shape. BeamStat automatically creates its intensity profile; only the maximum intensity is needed.")
        distributed_count = st.number_input("Number of distributed loads", min_value=0, max_value=10, value=1, step=1, key="multi_distributed_count")
        distributed_loads = []
        shape_options = ["Rectangular (uniform)", "Triangular – increasing", "Triangular – decreasing", "Tent-shaped (peak in middle/inside)"]
        shape_map = {
            "Rectangular (uniform)": "rectangular",
            "Triangular – increasing": "triangular_increasing",
            "Triangular – decreasing": "triangular_decreasing",
            "Tent-shaped (peak in middle/inside)": "tent",
        }
        for i in range(int(distributed_count)):
            with st.expander(f"Distributed Load {i+1}", expanded=(i == 0)):
                shape_label = st.selectbox("Load shape", shape_options, key=f"dist_shape_{i}")
                shape = shape_map[shape_label]
                c1, c2 = st.columns(2)
                with c1:
                    a = st.number_input("Start position a (m)", min_value=0.0, max_value=float(L), value=0.0, step=0.5, key=f"dist_a_{i}")
                with c2:
                    b = st.number_input("End position b (m)", min_value=0.0, max_value=float(L), value=float(L), step=0.5, key=f"dist_b_{i}")
                peak_x = None
                if shape == "tent":
                    peak_x = st.number_input("Peak position (m)", min_value=float(a), max_value=float(b), value=float((a+b)/2), step=0.5, key=f"dist_peak_{i}")
                    st.caption("The load starts at zero, rises to the maximum at the peak, then returns to zero.")
                wmax = st.number_input("Maximum intensity (kN/m)", min_value=0.0, value=10.0, step=1.0, key=f"dist_wmax_{i}")
                direction = st.selectbox("Direction", ["Downward", "Upward"], key=f"dist_dir_{i}")
                distributed_loads.append({"type": shape, "a": float(a), "b": float(b),
                    "peak_x": None if peak_x is None else float(peak_x), "wmax": float(wmax),
                    "w0": 0.0 if shape in ("triangular_increasing", "tent") else float(wmax),
                    "w1": 0.0 if shape in ("triangular_decreasing", "tent") else float(wmax),
                    "direction": direction})
        st.markdown("**6. Applied Moment**")
        moment = st.number_input("Moment M at beam midpoint (kN·m; CCW positive)", value=0.0, step=1.0, key="multi_moment")
        EI = 20000.0  # Internal constant used by the solver.
        calculate = st.button("▦  Calculate Reactions  →", use_container_width=True, type="primary", key="multi_calculate")

    with result_col:
        if calculate:
            try:
                if len(edited_supports) < 2:
                    raise ValueError("Please add at least two supports.")
                for i, load in enumerate(distributed_loads):
                    if load["b"] <= load["a"]:
                        raise ValueError(f"Distributed Load {i+1}: end position must be greater than start position.")
                    if load.get("type") == "tent" and not (load["a"] < load["peak_x"] < load["b"]):
                        raise ValueError(f"Distributed Load {i+1}: peak position must be between the start and end positions.")
                supports = []
                for i, row in edited_supports.reset_index(drop=True).iterrows():
                    sx = float(row["Distance from A (m)"])
                    stype = str(row["Support type"])
                    label = str(row.get("Label", "")).strip() or chr(65+i)
                    if not 0 <= sx <= float(L):
                        raise ValueError(f"Support {i+1} must be between 0 and {L:g} m.")
                    if any(abs(sx - old["x"]) < 1e-8 for old in supports):
                        raise ValueError("Two supports cannot occupy the same position. Enter different distances.")
                    supports.append({"label": label, "x": sx, "type": stype})
                if len({round(s["x"], 8) for s in supports}) < 2:
                    raise ValueError("At least two supports at different positions are required.")

                nodes, displacement, reactions, support_reactions = solve_beam(
                    float(L), supports, point_loads, distributed_loads, float(moment), EI)
                dist_force = sum(distributed_load_integrals(load)[0] for load in distributed_loads)
                dist_moment_A = sum(distributed_load_integrals(load)[1] for load in distributed_loads)
                total_Ry = sum(r["Ry"] for r in support_reactions)
                sumFy = total_Ry - sum(p for p, _ in point_loads) + dist_force
                sumMA = sum(r["M"] + r["Ry"]*r["x"] for r in support_reactions) - sum(p*x for p,x in point_loads) + dist_moment_A + float(moment)

                st.markdown('<div class="panel-title">▥  Support Reactions</div>', unsafe_allow_html=True)
                reaction_cols = st.columns(min(3, len(support_reactions)))
                for i, reaction in enumerate(support_reactions):
                    with reaction_cols[i % len(reaction_cols)]:
                        st.markdown(
                            f'<div class="metric-card"><div class="metric-label">Support {reaction["label"]} · {reaction["type"]}</div>'
                            f'<div class="metric-value">R{reaction["label"]} = {reaction["Ry"]:.3f} kN</div>'
                            f'<div class="metric-unit">Vertical reaction · x = {reaction["x"]:.2f} m</div>'
                            + (f'<div class="metric-unit">M{reaction["label"]} = {reaction["M"]:.3f} kN·m</div>' if reaction["type"] == "Fixed" else "")
                            + '</div>', unsafe_allow_html=True)

                # Internal section actions at every requested coordinate (support or no support).
                st.markdown('<div class="panel-title" style="margin-top:18px">⌖  Results at Analysis Points</div>', unsafe_allow_html=True)
                section_results = []
                for point in analysis_points:
                    xsec = point["x"]
                    # Use the left-hand section convention. Loads exactly at the cut are excluded;
                    # users can inspect the point immediately to either side by adjusting x slightly.
                    Vsec = sum(r["Ry"] for r in support_reactions if r["x"] < xsec - 1e-9)
                    Msec = sum(r["Ry"] * (xsec-r["x"]) for r in support_reactions if r["x"] < xsec - 1e-9)
                    Msec -= sum(p * (xsec-xp) for p, xp in point_loads if xp < xsec - 1e-9)
                    Msec += sum(r["M"] for r in support_reactions if r["x"] < xsec - 1e-9) * -1.0
                    for load in distributed_loads:
                        force_left, _, moment_about_cut = distributed_load_integrals(load, x1=xsec)
                        Vsec += force_left
                        Msec += moment_about_cut
                    if xsec > float(L)/2 + 1e-9:
                        Msec -= float(moment)
                    has_support = any(abs(r["x"]-xsec) < 1e-7 for r in support_reactions)
                    section_results.append({"label": point["label"], "x": xsec, "V": Vsec, "M": Msec, "has_support": has_support})
                section_cols = st.columns(min(3, max(1, len(section_results))))
                for i, result in enumerate(section_results):
                    with section_cols[i % len(section_cols)]:
                        status = "Support location" if result["has_support"] else "No support · section only"
                        st.markdown(
                            f'<div class="metric-card"><div class="metric-label">Point {result["label"]} · x = {result["x"]:.2f} m</div>'
                            f'<div class="metric-unit">{status}</div>'
                            f'<div class="metric-value">V = {result["V"]:.3f} kN</div>'
                            f'<div class="metric-unit">Internal shear force</div>'
                            f'<div class="metric-value">M = {result["M"]:.3f} kN·m</div>'
                            f'<div class="metric-unit">Internal bending moment</div></div>', unsafe_allow_html=True)

                st.markdown('<div class="panel-title" style="margin-top:16px">✎  Beam Diagram</div>',unsafe_allow_html=True)
                fig, ax = plt.subplots(figsize=(11, 3.8))
                chart_dark = _DARK_FALLBACK
                chart_bg = "#101827" if chart_dark else "#FFFFFF"
                chart_fg = "#EFF3FF" if chart_dark else "#173B5E"
                fig.patch.set_facecolor(chart_bg)
                ax.set_facecolor(chart_bg)
                ax.plot([0,L],[0,0],color="#263b5a",lw=7,solid_capstyle="round",zorder=3)
                for support_index, reaction in enumerate(support_reactions):
                    sx, kind, label = reaction["x"], reaction["type"], reaction["label"]
                    if kind == "Pin":
                        ax.scatter([sx],[-.12],marker="^",s=190,color="#08519C",zorder=4)
                        ax.plot([sx-.18,sx+.18],[-.25,-.25],color="#08519C",lw=1.5)
                    elif kind == "Roller":
                        ax.scatter([sx],[-.10],s=105,facecolors="white",edgecolors="#0752b5",linewidths=2,zorder=4)
                        ax.plot([sx-.22,sx+.22],[-.25,-.25],color="#08519C",lw=1.5)
                    else:
                        ax.plot([sx,sx],[-.38,.27],color="#08519C",lw=5,zorder=4)
                        for yy in np.linspace(-.35,.22,6):
                            ax.plot([sx-.15,sx],[yy,yy+.08],color="#08519C",lw=1)
                    ax.annotate(f"R{label} = {reaction['Ry']:.2f} kN", xy=(sx,-.31), xytext=(sx,-.72-(0.22*(support_index%2))), ha="center", fontsize=8, color="#07833b")
                    ax.text(sx,-.48,f"{label} · {kind}",ha="center",fontsize=8,color="#173b70")
                    if reaction["type"] == "Fixed" and abs(reaction["M"]) > 1e-8:
                        ax.text(sx,.48,f"M{label}={reaction['M']:.2f} kN·m",ha="center",fontsize=8,color="#8b36d9")
                for point in analysis_points:
                    px = point["x"]
                    ax.axvline(px, ymin=.28, ymax=.72, color="#94a3b8", lw=1, ls="--", alpha=.8, zorder=1)
                    ax.text(px, .16, point["label"], ha="center", va="bottom", fontsize=8, color="#7c3aed", fontweight="bold")
                for i, (p,x) in enumerate(point_loads):
                    if p > 0:
                        ax.annotate("",xy=(x,.04),xytext=(x,.78),arrowprops=dict(arrowstyle="-|>",color="#e13b32",lw=2))
                        ax.text(x,.85,f"{p:g} kN",ha="center",fontsize=8,color="#c52e28")
                for load_index, load in enumerate(distributed_loads):
                    if load["b"] > load["a"] and float(load.get("wmax", max(load.get("w0", 0), load.get("w1", 0)))) > 0:
                        if load.get("type") == "tent":
                            xs = np.linspace(load["a"], load["b"], 25)
                            xs = np.unique(np.append(xs, load["peak_x"]))
                        else:
                            xs = np.linspace(load["a"], load["b"], 17)
                        intensities = distributed_intensity(load, xs)
                        max_intensity = max(float(np.max(intensities)), 1e-9)
                        arrow_tops = .04 + (.08 + .42*intensities/max_intensity)
                        envelope_color = "#3182BD" if load["direction"] == "Downward" else "#07833b"
                        # Draw arrows first, then a closed outline so the envelope remains visible.
                        for xx, arrow_top in zip(xs, arrow_tops):
                            if load["direction"] == "Downward":
                                ax.annotate("", xy=(xx,.045), xytext=(xx,arrow_top-.025),
                                    arrowprops=dict(arrowstyle="-|>", color=envelope_color, lw=1.0), zorder=4)
                            else:
                                ax.annotate("", xy=(xx,arrow_top-.025), xytext=(xx,.045),
                                    arrowprops=dict(arrowstyle="-|>", color=envelope_color, lw=1.0), zorder=4)
                        # Closed boundary: vertical ends and a continuous top profile.
                        ax.plot([load["a"], load["a"]], [.045, arrow_tops[0]], color=envelope_color, lw=2.2, zorder=8)
                        ax.plot(xs, arrow_tops, color=envelope_color, lw=2.2, zorder=8)
                        ax.plot([load["b"], load["b"]], [arrow_tops[-1], .045], color=envelope_color, lw=2.2, zorder=8)
                        shape_labels = {
                            "rectangular": "Rectangular",
                            "triangular_increasing": "Triangle increasing",
                            "triangular_decreasing": "Triangle decreasing",
                            "tent": "Tent-shaped triangle",
                            "triangular": "Triangle",
                        }
                        label = shape_labels.get(load["type"], "Distributed load")
                        label_y = float(np.max(arrow_tops)) + .12
                        ax.text((load["a"]+load["b"])/2, label_y,
                            f"{label}: {load.get('wmax', max(load.get('w0', 0), load.get('w1', 0))):g} kN/m",
                            ha="center", fontsize=8, color=envelope_color)
                if moment:
                    ax.annotate("",xy=(L/2+.25,.22),xytext=(L/2-.25,.22),arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=-.8",color="#8b36d9",lw=2))
                    ax.text(L/2,.52,f"M = {moment:g} kN·m",ha="center",fontsize=8,color="#8b36d9")
                ax.annotate("",xy=(L,-1.12),xytext=(0,-1.12),arrowprops=dict(arrowstyle="<->",color="#64748b"))
                ax.text(L/2,-1.25,f"L = {L:.2f} m",ha="center",fontsize=8,color="#475569")
                ax.set_xlim(-.45,L+.45); ax.set_ylim(-1.48,1.35); ax.axis("off")
                ax.tick_params(colors=chart_fg)
                st.pyplot(fig,use_container_width=True)
                plt.close(fig)

                st.markdown('<div class="panel-title">✓  Equilibrium Check</div>',unsafe_allow_html=True)
                check_cols = st.columns(2)
                for col,label,val,unit in [(check_cols[0],"ΣFy",sumFy,"kN"),(check_cols[1],"ΣMₐ",sumMA,"kN·m")]:
                    with col:
                        st.metric(label,f"{val:.4f} {unit}")
                if abs(sumFy)<1e-5 and abs(sumMA)<1e-5:
                    st.success("Static equilibrium verified within numerical tolerance.")
                else:
                    st.warning("Check the load and support configuration; residuals are not close to zero.")
                with st.expander("Step-by-Step Calculations",expanded=True):
                    st.markdown("**1. Convert distributed loads into equivalent forces**")
                    for load_index, load in enumerate(distributed_loads):
                        force_signed, moment_A_signed, _ = distributed_load_integrals(load)
                        resultant = abs(force_signed)
                        centroid = moment_A_signed/force_signed if abs(force_signed) > 1e-12 else (load["a"]+load["b"])/2
                        if load["type"] in ("triangular", "triangular_increasing", "triangular_decreasing"):
                            st.latex(r"W=\frac{1}{2}w_{max}L")
                            st.write(f"Load {load_index+1} (triangular): resultant = {resultant:.3f} kN, centroid at x = {centroid:.3f} m from A.")
                        elif load["type"] == "tent":
                            st.write(f"Load {load_index+1} (tent-shaped): integrated resultant = {resultant:.3f} kN, centroid at x = {centroid:.3f} m from A. The two triangular halves are calculated separately.")
                        else:
                            st.latex(r"W=wL")
                            st.write(f"Load {load_index+1} (rectangular): resultant = {resultant:.3f} kN, centroid at x = {centroid:.3f} m from A.")
                    st.markdown("**2. Apply support restraints**")
                    for r in support_reactions:
                        st.write(f"Support {r['label']} ({r['type']}) at x = {r['x']:.3f} m: Ry = {r['Ry']:.4f} kN" + (f", M = {r['M']:.4f} kN·m" if r['type']=="Fixed" else ""))
                    st.markdown("**3. Verify global equilibrium**")
                    st.write(f"ΣFy = {sumFy:.6f} kN; ΣM about A = {sumMA:.6f} kN·m.")
                    st.caption("The beam is modeled with Euler–Bernoulli elements and constant internal EI. Reactions are recovered at every entered support location.")
            except (np.linalg.LinAlgError, ValueError, KeyError, TypeError) as exc:
                st.error(f"Unable to solve this support arrangement: {exc}")
        else:
            st.info("Add at least two supports, add analysis points, enter point or distributed loads, then click **Calculate Reactions**. Load values default to zero.")

elif st.session_state.page == "About":
    st.markdown('<h1 class="section-title">About BeamStat</h1>',unsafe_allow_html=True)
    st.markdown("""
    <div class="panel">
    <div class="panel-title">What is BeamStat?</div>
    BeamStat is an interactive educational simulator for studying beam reactions and static equilibrium.
    It helps civil engineering students explore how support conditions and external loads affect the behavior
    of a beam. Instead of solving every configuration by hand, users can adjust the beam setup and observe
    the calculated support reactions alongside a labeled beam diagram and calculation walkthrough.
    </div>
    <div class="panel">
    <div class="panel-title">Simulation features</div>
    <ul>
      <li><b>Beam span:</b> Set the total length of the beam in meters.</li>
      <li><b>Support configuration:</b> Add at least two Pin, Roller, or Fixed supports at user-defined distances along the beam.</li>
      <li><b>Point loads:</b> Add up to ten downward point loads and set each load's position along the beam.</li>
      <li><b>Uniformly distributed load:</b> Set the load intensity and the start/end positions. BeamStat converts it to an equivalent resultant force at the load's centroid.</li>
      <li><b>Applied couple:</b> Add a counterclockwise-positive moment at midspan.</li>
      <li><b>Reaction and section results:</b> View support reactions and internal shear force and bending moment at any labeled analysis point, including locations without supports.</li>
      <li><b>Beam diagram:</b> See the selected supports, applied loads, UDL, applied moment, and reaction labels.</li>
      <li><b>Equilibrium check:</b> Review the vertical-force and moment residuals to check overall equilibrium.</li>
      <li><b>Step-by-step details:</b> Inspect the equivalent UDL calculation, stiffness-model setup, support restraints, reactions, and verification.</li>
    </ul>
    </div>
    <div class="panel">
    <div class="panel-title">How the calculation works</div>
    The simulator uses the Euler–Bernoulli beam stiffness method. The beam is divided into elements at load positions
    and UDL boundaries. Element stiffness matrices and equivalent nodal loads are assembled into a global system,
    support restraints are applied, and the unknown nodal displacements are solved. Support reactions are then
    recovered from the global stiffness equation. This allows the prototype to analyze determinate and selected
    indeterminate vertical-bending support arrangements, including fixed-end moments.
    </div>
    <div class="panel">
    <div class="panel-title">Scope and limitations</div>
    This version assumes a straight, prismatic beam with constant flexural rigidity EI and small-deflection
    Euler–Bernoulli bending behavior. Loads are vertical, with one applied couple at midspan and two or more user-positioned supports. It does not yet
    model horizontal loads, axial deformation, shear deformation, varying EI, settlement, distributed moments,
    or multiple arbitrary applied couples. Pin and roller supports have the same vertical-bending restraint in
    this model; their horizontal restraint distinction matters only when horizontal loading is added.
    BeamStat is for learning and preliminary checking, not for final structural design or construction decisions.
    </div>
    """,unsafe_allow_html=True)

elif st.session_state.page == "Contact":
    st.markdown('<h1 class="section-title">Meet the Creators</h1>',unsafe_allow_html=True)
    st.write("BeamStat is a collaborative, student-built simulation project created to make complex structural or particle/beam analysis more accessible and interactive. Combining foundational engineering principles with modern software tools, the project lets researchers, classmates, and enthusiasts run scenarios, visualize results, and iterate quickly on designs—serving both as a practical learning tool and a showcase of student innovation.")
    # Display eight contacts in a responsive 4-column, 2-row layout.
    for start in range(0, len(CONTACT_CREATORS), 4):
        cols = st.columns(4, gap="medium")
        for col, creator in zip(cols, CONTACT_CREATORS[start:start + 4]):
            with col:
                st.markdown(
                    f'<div class="panel" style="min-height:170px; margin-bottom:14px;">'
                    f'<div style="font-size:30px;color:#3182BD">◉</div>'
                    f'<div class="panel-title">{creator["name"]}</div>'
                    f'<b>{creator["role"]}</b>'
                    f'<p class="small-note">{creator["email"]}</p>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
    st.info("Professor: Engr. Ella Kristina Delima")
