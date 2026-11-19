import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from PIL import Image

# -----------------------------------------------------------------------------
# BeamStat | Streamlit prototype
# Keep this Python file, COMPROG.png, and COMPROG.jpg in the same folder.
# Replace the creator placeholders in CONTACT_CREATORS with your actual names.
# -----------------------------------------------------------------------------
st.set_page_config(page_title="BeamStat | Beam Analysis Simulator", page_icon="🏗️", layout="wide")
BASE = Path(__file__).resolve().parent
LOGO_PATH = BASE / "COMPROG.png"       
HERO_PATH = BASE / "COMPROG.jpg"       # original BeamStat construction hero image

CONTACT_CREATORS = [
    {"name": "Creator 1", "role": "Project Lead / Developer", "email": "Add contact details"},
    {"name": "Creator 2", "role": "UI/UX Designer", "email": "Add contact details"},
    {"name": "Creator 3", "role": "Engineering Researcher", "email": "Add contact details"},
]

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Poppins:wght@500;600;700;800;900&display=swap');
:root{--blue:#0752b5;--navy:#102c61;--pale:#f4f8ff;--line:#dce8f8;--muted:#64748b}
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
.hero-title{font-family:'Poppins',sans-serif;font-size:88px;line-height:1.02;color:var(--blue);font-weight:900;letter-spacing:-4px;margin:0 0 8px;animation:heroFadeUp 1.15s ease-out both}
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
.panel-title{font-size:16px;font-weight:800;color:var(--navy);margin-bottom:10px}
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
  --bs-blue: #3985ed;
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

</style>
""", unsafe_allow_html=True)

# Session navigation
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Header: exact uploaded logo file, plus transparent clickable nav.
nav_cols = st.columns([2.5, .8, .9, .7, .9])
with nav_cols[0]:
    if LOGO_PATH.exists():
        st.image(Image.open(LOGO_PATH), width=155)
    else:
        st.markdown('<div class="brand-fallback">▰ BeamStat</div>', unsafe_allow_html=True)
for col, label in zip(nav_cols[1:], ["HOME", "SIMULATOR", "ABOUT", "CONTACT"]):
    with col:
        if st.button(label, key=f"nav_{label}", use_container_width=True):
            st.session_state.page = {"HOME":"Home","SIMULATOR":"Simulator","ABOUT":"About","CONTACT":"Contact"}[label]
            st.rerun()
st.markdown('<div class="navline"></div>', unsafe_allow_html=True)


def solve_beam(L, supports, point_loads, udl_w, udl_a, udl_b, applied_moment, EI):
    """Euler-Bernoulli beam FE model with any number of vertical supports.
    Positive vertical force is upward; positive moment is counterclockwise.
    Each support restrains vertical displacement; Fixed also restrains rotation.
    """
    support_positions = [float(s["x"]) for s in supports]
    nodes = sorted(set([0.0, float(L)] + support_positions
                       + [float(x) for _, x in point_loads]
                       + [float(udl_a), float(udl_b)] + [float(L)/2]))
    n = len(nodes)
    K = np.zeros((2*n, 2*n), dtype=float)
    F = np.zeros(2*n, dtype=float)

    for e in range(n-1):
        le = nodes[e+1] - nodes[e]
        if le <= 1e-10:
            continue
        ke = EI / le**3 * np.array([
            [12, 6*le, -12, 6*le],
            [6*le, 4*le**2, -6*le, 2*le**2],
            [-12, -6*le, 12, -6*le],
            [6*le, 2*le**2, -6*le, 4*le**2]
        ], dtype=float)
        dofs = [2*e, 2*e+1, 2*(e+1), 2*(e+1)+1]
        K[np.ix_(dofs, dofs)] += ke
        midpoint = (nodes[e] + nodes[e+1]) / 2
        if udl_w > 0 and udl_b > udl_a and udl_a-1e-9 <= midpoint <= udl_b+1e-9:
            q = -udl_w
            F[dofs] += q * np.array([le/2, le**2/12, le/2, -le**2/12])

    for p, x in point_loads:
        idx = min(range(n), key=lambda i: abs(nodes[i]-x))
        F[2*idx] -= p

    mid_idx = min(range(n), key=lambda i: abs(nodes[i] - L/2))
    F[2*mid_idx+1] += applied_moment

    restrained = []
    support_node_indices = []
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
        support_reactions.append({
            "label": support["label"], "x": float(support["x"]),
            "type": support["type"], "Ry": float(R[2*idx]),
            "M": float(R[2*idx+1]) if support["type"] == "Fixed" else 0.0
        })
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

        st.markdown("**5. Uniformly Distributed Load (UDL)**")
        w = st.number_input("UDL intensity w (kN/m)", min_value=0.0, value=0.0, step=1.0, key="multi_udl_w")
        ua, ub = st.columns(2)
        with ua:
            udl_a = st.number_input("Start a (m)", min_value=0.0, max_value=float(L), value=0.0, step=0.5, key="multi_udl_a")
        with ub:
            udl_b = st.number_input("End b (m)", min_value=0.0, max_value=float(L), value=0.0, step=0.5, key="multi_udl_b")
        st.markdown("**6. Applied Moment**")
        moment = st.number_input("Moment M at beam midpoint (kN·m; CCW positive)", value=0.0, step=1.0, key="multi_moment")
        EI = 20000.0  # Internal constant used by the solver.
        calculate = st.button("▦  Calculate Reactions  →", use_container_width=True, type="primary", key="multi_calculate")

    with result_col:
        if calculate:
            try:
                if len(edited_supports) < 2:
                    raise ValueError("Please add at least two supports.")
                if udl_b < udl_a:
                    raise ValueError("UDL end must be greater than or equal to its start.")
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
                    float(L), supports, point_loads, float(w), float(udl_a), float(udl_b), float(moment), EI)
                udl_force = float(w) * (float(udl_b)-float(udl_a))
                udl_centroid = (float(udl_a)+float(udl_b))/2 if udl_b > udl_a else 0.0
                total_Ry = sum(r["Ry"] for r in support_reactions)
                total_Msupport = sum(r["M"] for r in support_reactions)
                sumFy = total_Ry - sum(p for p, _ in point_loads) - udl_force
                sumMA = sum(r["M"] + r["Ry"]*r["x"] for r in support_reactions) - sum(p*x for p,x in point_loads) - udl_force*udl_centroid + float(moment)

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
                    udl_left = max(0.0, min(xsec, float(udl_b)) - float(udl_a)) if xsec > float(udl_a) else 0.0
                    if float(w) > 0 and udl_left > 0:
                        udl_resultant = float(w) * udl_left
                        udl_centroid_left = float(udl_a) + udl_left/2
                        Vsec -= udl_resultant
                        Msec -= udl_resultant * (xsec-udl_centroid_left)
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
                fig.patch.set_facecolor("white")
                ax.plot([0,L],[0,0],color="#263b5a",lw=7,solid_capstyle="round",zorder=3)
                for support_index, reaction in enumerate(support_reactions):
                    sx, kind, label = reaction["x"], reaction["type"], reaction["label"]
                    if kind == "Pin":
                        ax.scatter([sx],[-.12],marker="^",s=190,color="#0752b5",zorder=4)
                        ax.plot([sx-.18,sx+.18],[-.25,-.25],color="#0752b5",lw=1.5)
                    elif kind == "Roller":
                        ax.scatter([sx],[-.10],s=105,facecolors="white",edgecolors="#0752b5",linewidths=2,zorder=4)
                        ax.plot([sx-.22,sx+.22],[-.25,-.25],color="#0752b5",lw=1.5)
                    else:
                        ax.plot([sx,sx],[-.38,.27],color="#0752b5",lw=5,zorder=4)
                        for yy in np.linspace(-.35,.22,6):
                            ax.plot([sx-.15,sx],[yy,yy+.08],color="#0752b5",lw=1)
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
                if w > 0 and udl_b > udl_a:
                    ax.plot([udl_a,udl_b],[.46,.46],color="#1769c2",lw=1.5)
                    for xx in np.linspace(udl_a,udl_b,10):
                        ax.annotate("",xy=(xx,.04),xytext=(xx,.44),arrowprops=dict(arrowstyle="-|>",color="#1769c2",lw=1))
                    ax.text((udl_a+udl_b)/2,.54,f"w = {w:g} kN/m",ha="center",fontsize=8,color="#1769c2")
                if moment:
                    ax.annotate("",xy=(L/2+.25,.22),xytext=(L/2-.25,.22),arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=-.8",color="#8b36d9",lw=2))
                    ax.text(L/2,.52,f"M = {moment:g} kN·m",ha="center",fontsize=8,color="#8b36d9")
                ax.annotate("",xy=(L,-1.12),xytext=(0,-1.12),arrowprops=dict(arrowstyle="<->",color="#64748b"))
                ax.text(L/2,-1.25,f"L = {L:.2f} m",ha="center",fontsize=8,color="#475569")
                ax.set_xlim(-.45,L+.45); ax.set_ylim(-1.48,1.08); ax.axis("off")
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
                    st.markdown("**1. Convert the UDL into an equivalent force**")
                    st.latex(r"W_{eq}=w(b-a)")
                    st.write(f"W_eq = {w:g}({udl_b:g} − {udl_a:g}) = {udl_force:.3f} kN, acting at x̄ = {udl_centroid:.3f} m from A.")
                    st.markdown("**2. Apply support restraints**")
                    for r in support_reactions:
                        st.write(f"Support {r['label']} ({r['type']}) at x = {r['x']:.3f} m: Ry = {r['Ry']:.4f} kN" + (f", M = {r['M']:.4f} kN·m" if r['type']=="Fixed" else ""))
                    st.markdown("**3. Verify global equilibrium**")
                    st.write(f"ΣFy = {sumFy:.6f} kN; ΣM about A = {sumMA:.6f} kN·m.")
                    st.caption("The beam is modeled with Euler–Bernoulli elements and constant internal EI. Reactions are recovered at every entered support location.")
            except (np.linalg.LinAlgError, ValueError, KeyError, TypeError) as exc:
                st.error(f"Unable to solve this support arrangement: {exc}")
        else:
            st.info("Add at least two supports, add any analysis points (including points without supports), enter loads, then click **Calculate Reactions**. Load values default to zero.")

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
    st.write("BeamStat is a student-developed simulation project. Replace the sample entries below with your team's actual names and contact information.")
    cols = st.columns(len(CONTACT_CREATORS))
       
