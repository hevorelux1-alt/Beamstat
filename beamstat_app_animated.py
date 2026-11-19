import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from PIL import Image

# -----------------------------------------------------------------------------
# BeamStat | Streamlit prototype
# Keep beamstat_app.py, image(4).png, and image(3).png in the same folder.
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
</style>
""", unsafe_allow_html=True)

# Session navigation
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Header: exact uploaded logo file, plus transparent clickable nav.
nav_cols = st.columns([2.5, .8, .9, .7, .9, .8])
with nav_cols[0]:
    if LOGO_PATH.exists():
        st.image(Image.open(LOGO_PATH), width=120)
    else:
        st.markdown('<div class="brand-fallback">▰ BeamStat</div>', unsafe_allow_html=True)
for col, label in zip(nav_cols[1:], ["HOME", "SIMULATOR", "ABOUT", "CONTACT", "⌕"]):
    with col:
        if st.button(label, key=f"nav_{label}", use_container_width=True):
            st.session_state.page = {"HOME":"Home","SIMULATOR":"Simulator","ABOUT":"About","CONTACT":"Contact","⌕":"Contact"}[label]
            st.rerun()
st.markdown('<div class="navline"></div>', unsafe_allow_html=True)


def solve_beam(L, support_A, support_B, point_loads, udl_w, udl_a, udl_b, applied_moment, EI):
    """Euler-Bernoulli beam FE model with vertical and rotational DOFs per node.
    Positive vertical force is upward; positive moment is counterclockwise.
    """
    nodes = sorted(set([0.0, float(L)] + [float(x) for _, x in point_loads] + [float(udl_a), float(udl_b)]))
    n = len(nodes)
    K = np.zeros((2*n, 2*n), dtype=float)
    F = np.zeros(2*n, dtype=float)

    for e in range(n-1):
        le = nodes[e+1] - nodes[e]
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
            # Consistent nodal loads for downward uniform load.
            q = -udl_w
            fe = q * np.array([le/2, le**2/12, le/2, -le**2/12])
            F[dofs] += fe

    for p, x in point_loads:
        idx = min(range(n), key=lambda i: abs(nodes[i]-x))
        F[2*idx] -= p

    # Applied couple is specified at beam midspan in this version.
    mid_idx = min(range(n), key=lambda i: abs(nodes[i] - L/2))
    F[2*mid_idx+1] += applied_moment

    # Both support types restrain vertical translation. Fixed ends also restrain rotation.
    restrained = [0, 2*(n-1)]
    if support_A == "Fixed":
        restrained.append(1)
    if support_B == "Fixed":
        restrained.append(2*(n-1)+1)
    free = [i for i in range(2*n) if i not in restrained]
    d = np.zeros(2*n)
    Kff = K[np.ix_(free, free)]
    if np.linalg.matrix_rank(Kff) < len(free):
        raise np.linalg.LinAlgError("The selected support arrangement is unstable.")
    d[free] = np.linalg.solve(Kff, F[free])
    R = K @ d - F
    return nodes, d, R


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
    st.caption("Start with zero loads, enter your beam data, then calculate the support reactions. This model covers vertical loading and beam bending.")
    input_col, result_col = st.columns([.88, 1.72], gap="medium")
    with input_col:
        st.markdown('<div class="panel-title">⚙️  1. Beam Configuration</div>', unsafe_allow_html=True)
        L = st.number_input("Span length L (m)", min_value=.1, value=6.0, step=.5)
        sa, sb = st.columns(2)
        with sa:
            support_A = st.selectbox("Support at A", ["Pin", "Roller", "Fixed"], index=0)
        with sb:
            support_B = st.selectbox("Support at B", ["Pin", "Roller", "Fixed"], index=1)
        st.markdown('<div class="small-note">Pin: vertical and horizontal restraint. Roller: vertical restraint. Fixed: translation and rotation restraint. Horizontal loading is not included in this prototype.</div>', unsafe_allow_html=True)
        st.markdown("**2. Applied Loads**")
        P1 = st.number_input("Point load P₁ (kN, downward)", min_value=0.0, value=0.0, step=1.0)
        x1 = st.number_input("Position x₁ (m)", min_value=0.0, max_value=float(L), value=0.0, step=.5)
        P2 = st.number_input("Point load P₂ (kN, downward)", min_value=0.0, value=0.0, step=1.0)
        x2 = st.number_input("Position x₂ (m)", min_value=0.0, max_value=float(L), value=0.0, step=.5)
        st.markdown("**Uniformly Distributed Load (UDL)**")
        w = st.number_input("UDL intensity w (kN/m)", min_value=0.0, value=0.0, step=1.0)
        ua, ub = st.columns(2)
        with ua:
            udl_a = st.number_input("Start a (m)", min_value=0.0, max_value=float(L), value=0.0, step=.5)
        with ub:
            udl_b = st.number_input("End b (m)", min_value=0.0, max_value=float(L), value=0.0, step=.5)
        st.markdown("**Applied Moment**")
        moment = st.number_input("Moment M (kN·m; CCW positive)", value=0.0, step=1.0)
        EI = 20000.0  # Internal constant used by the beam stiffness solver; hidden from the user.
        calculate = st.button("▦  Calculate Reactions  →", use_container_width=True)

    with result_col:
        if calculate:
            if udl_b < udl_a:
                st.error("UDL end must be greater than or equal to its start.")
            else:
                try:
                    nodes, displacement, reactions = solve_beam(
                        L, support_A, support_B, [(P1,x1),(P2,x2)], w, udl_a, udl_b, moment, EI)
                    RAy = reactions[0]
                    RBy = reactions[2*(len(nodes)-1)]
                    MA = reactions[1] if support_A == "Fixed" else 0.0
                    MB = reactions[2*(len(nodes)-1)+1] if support_B == "Fixed" else 0.0
                    udl_force = w * (udl_b-udl_a)
                    udl_centroid = (udl_a+udl_b)/2 if udl_b > udl_a else 0.0

                    st.markdown('<div class="panel-title">▥  Support Reactions</div>', unsafe_allow_html=True)
                    metrics = st.columns(4)
                    values = [("Rₐₓ","0.00 kN","Horizontal*"),("Rₐ",f"{RAy:.3f} kN","Vertical reaction at A"),("Rᵦ",f"{RBy:.3f} kN","Vertical reaction at B"),("M support",f"{MA+MB:.3f} kN·m","Sum of fixed-end moments")]
                    for col,(label,value,caption) in zip(metrics,values):
                        with col:
                            st.markdown(f'<div class="metric-card"><div class="metric-label">{label}</div><div class="metric-value">{value}</div><div class="metric-unit">{caption}</div></div>',unsafe_allow_html=True)
                    st.markdown('<div class="panel-title" style="margin-top:16px">✎  Beam Diagram</div>', unsafe_allow_html=True)
                    fig, ax = plt.subplots(figsize=(10,3.15))
                    fig.patch.set_facecolor("white")
                    ax.plot([0,L],[0,0],color="#263b5a",lw=7,solid_capstyle="round",zorder=3)
                    # support drawings
                    def draw_support(x,kind):
                        if kind == "Pin":
                            ax.scatter([x],[-.12],marker="^",s=220,color="#0752b5",zorder=4)
                            ax.plot([x-.17,x+.17],[-.25,-.25],color="#0752b5",lw=1.5)
                        elif kind == "Roller":
                            ax.scatter([x],[-.10],s=115,facecolors="white",edgecolors="#0752b5",linewidths=2,zorder=4)
                            ax.plot([x-.22,x+.22],[-.25,-.25],color="#0752b5",lw=1.5)
                        else:
                            ax.plot([x,x],[-.35,.28],color="#0752b5",lw=5,zorder=4)
                            for yy in np.linspace(-.32,.24,6):
                                ax.plot([x-.15,x],[yy,yy+.08],color="#0752b5",lw=1)
                    draw_support(0,support_A); draw_support(L,support_B)
                    for p,x,label in [(P1,x1,"P₁"),(P2,x2,"P₂")]:
                        if p>0:
                            ax.annotate("",xy=(x,.04),xytext=(x,.78),arrowprops=dict(arrowstyle="-|>",color="#e13b32",lw=2))
                            ax.text(x,.85,f"{p:g} kN",ha="center",fontsize=8,color="#c52e28")
                    if w>0 and udl_b>udl_a:
                        ax.plot([udl_a,udl_b],[.46,.46],color="#1769c2",lw=1.5)
                        for xx in np.linspace(udl_a,udl_b,10):
                            ax.annotate("",xy=(xx,.04),xytext=(xx,.44),arrowprops=dict(arrowstyle="-|>",color="#1769c2",lw=1))
                        ax.text((udl_a+udl_b)/2,.54,f"w = {w:g} kN/m",ha="center",fontsize=8,color="#1769c2")
                    if moment:
                        ax.annotate("",xy=(L/2+.25,.22),xytext=(L/2-.25,.22),arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=-.8",color="#8b36d9",lw=2))
                        ax.text(L/2,.52,f"M = {moment:g} kN·m",ha="center",fontsize=8,color="#8b36d9")
                    ax.text(0,-.48,f"A · {support_A}",ha="center",fontsize=8,color="#173b70")
                    ax.text(L,-.48,f"B · {support_B}",ha="center",fontsize=8,color="#173b70")
                    ax.text(0,-.72,f"RAy = {RAy:.2f} kN",ha="center",fontsize=8,color="#07833b")
                    ax.text(L,-.72,f"RBy = {RBy:.2f} kN",ha="center",fontsize=8,color="#07833b")
                    ax.annotate("",xy=(L,-.9),xytext=(0,-.9),arrowprops=dict(arrowstyle="<->",color="#64748b"))
                    ax.text(L/2,-1.02,f"L = {L:.2f} m",ha="center",fontsize=8,color="#475569")
                    ax.set_xlim(-.4,L+.4); ax.set_ylim(-1.2,1.05); ax.axis("off")
                    st.pyplot(fig,use_container_width=True)
                    plt.close(fig)

                    # Overall vertical force and moment checks about A.
                    sumFy = RAy + RBy - P1 - P2 - udl_force
                    sumMA = MA + MB + RBy*L - P1*x1 - P2*x2 - udl_force*udl_centroid + moment
                    st.markdown('<div class="panel-title">✓  Equilibrium Check</div>',unsafe_allow_html=True)
                    check_cols = st.columns(3)
                    for col,label,val,unit in [(check_cols[0],"ΣFx",0.0,"kN"),(check_cols[1],"ΣFy",sumFy,"kN"),(check_cols[2],"ΣMₐ",sumMA,"kN·m")]:
                        with col:
                            st.metric(label,f"{val:.4f} {unit}")
                    if abs(sumFy)<1e-5 and abs(sumMA)<1e-5:
                        st.success("Static equilibrium verified within numerical tolerance.")
                    else:
                        st.warning("Check the load and support configuration; residuals are not close to zero.")
                    with st.expander("Step-by-Step Calculations",expanded=True):
                        st.markdown("**1. Replace the UDL with an equivalent force**")
                        st.latex(r"W_{eq}=w(b-a)")
                        st.write(f"W_eq = {w:g}({udl_b:g} − {udl_a:g}) = {udl_force:.3f} kN, acting at x̄ = {udl_centroid:.3f} m from A.")
                        st.markdown("**2. Build the beam stiffness model**")
                        st.write(f"The beam is divided into {len(nodes)-1} Euler–Bernoulli elements at the load positions and UDL boundaries. A constant internal EI value is used by the solver.")
                        st.latex(r"\mathbf{K}\mathbf{d}=\mathbf{F}")
                        st.markdown("**3. Apply support restraints**")
                        st.write(f"At A: {support_A}. At B: {support_B}. Pin and roller restrain vertical displacement; fixed supports also restrain rotation.")
                        st.markdown("**4. Solve and recover support reactions**")
                        st.write(f"RAy = {RAy:.4f} kN; RBy = {RBy:.4f} kN.")
                        if support_A=="Fixed": st.write(f"Fixed-end reaction moment at A = {MA:.4f} kN·m.")
                        if support_B=="Fixed": st.write(f"Fixed-end reaction moment at B = {MB:.4f} kN·m.")
                        st.markdown("**5. Verify global equilibrium**")
                        st.write(f"ΣFy = {sumFy:.6f} kN; ΣM about A = {sumMA:.6f} kN·m.")
                    st.caption("*Horizontal reaction is displayed as zero because this prototype models vertical loading only. A pin's horizontal restraint is not activated without horizontal loads.")
                except (np.linalg.LinAlgError, ValueError) as exc:
                    st.error(f"Unable to solve this support arrangement: {exc} Try adding a fixed support or changing the support combination.")
        else:
            st.info("Choose the support at A and B, enter the loads, then click **Calculate Reactions**.")

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
      <li><b>Support configuration:</b> Select Pin, Roller, or Fixed independently at the left support A and right support B.</li>
      <li><b>Point loads:</b> Add two downward point loads and set each load's position along the beam.</li>
      <li><b>Uniformly distributed load:</b> Set the load intensity and the start/end positions. BeamStat converts it to an equivalent resultant force at the load's centroid.</li>
      <li><b>Applied couple:</b> Add a counterclockwise-positive moment at midspan.</li>
      <li><b>Reaction results:</b> View vertical reactions at both ends and reaction moments at fixed supports.</li>
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
    Euler–Bernoulli bending behavior. Loads are vertical, with one applied couple at midspan. It does not yet
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
    for col, creator in zip(cols, CONTACT_CREATORS):
        with col:
            st.markdown(f'<div class="panel"><div style="font-size:30px;color:#0752b5">◉</div><div class="panel-title">{creator["name"]}</div><b>{creator["role"]}</b><p class="small-note">{creator["email"]}</p></div>',unsafe_allow_html=True)
    st.info("To personalize this page, edit CONTACT_CREATORS near the top of beamstat_app.py.")
