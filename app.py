import streamlit as st
from utils.style import apply_custom_style
from agent.coach_agent import CoachAgent
from utils.visuals import create_macro_chart, create_intensity_gauge, create_burn_radar, create_meal_timeline, create_pain_gauge

# Page config
st.set_page_config(page_title="AI Gym Trainer Elite v3.0", page_icon="💎", layout="wide")

# Apply custom elite styling
apply_custom_style()

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = []
if "workout_plan" not in st.session_state:
    st.session_state.workout_plan = None
if "profile" not in st.session_state:
    st.session_state.profile = {}
if "pain_level" not in st.session_state:
    st.session_state.pain_level = 0

# Sidebar: Advanced Profile Configuration
with st.sidebar:
    st.title("🏃 ELITE COACH PROFILE")
    
    st.subheader("📊 PHYSICAL METRICS")
    age = st.number_input("AGE", 14, 100, 25)
    weight = st.slider("WEIGHT (KG)", 40, 150, 70)
    
    st.subheader("🎯 TRAINING GOALS")
    level = st.selectbox("FITNESS LEVEL", ["Beginner", "Intermediate", "Advanced"])
    goal = st.selectbox("GOAL", ["Lose Weight", "Gain Muscle", "Stay Fit"])
    days = st.select_slider("TRAINING DAYS PER WEEK", options=[1, 2, 3, 4, 5, 6, 7], value=4)
    
    st.subheader("🥗 LIFESTYLE")
    meals = st.radio("MEALS PER DAY", [2, 3, 4, 5, 6], index=1, horizontal=True)
    equipment = st.selectbox("EQUIPMENT ACCESS", ["Full Gym", "Home (No Equipment)", "Home (Dumbbells/Bands)"])
    
    st.subheader("🩹 INJURY MANAGEMENT")
    notes = st.text_area("SPECIFIC CONSTRAINTS / INJURIES", placeholder="e.g., Lower back pain, knee strain...")
    if notes:
        st.session_state.pain_level = st.select_slider(
            "INJURY PAIN LEVEL (0=NONE, 10=EXTREME)",
            options=list(range(11)),
            value=st.session_state.pain_level
        )

    if st.button("💎 GENERATE ELITE PLAN"):
        with st.spinner("🚀 OUR EXPERT TEAM IS CRAFTING YOUR STRATEGY..."):
            try:
                profile = {
                    "age": age,
                    "weight": weight,
                    "level": level,
                    "goal": goal,
                    "days": days,
                    "meals": meals,
                    "equipment": equipment,
                    "notes": notes,
                    "pain_level": st.session_state.pain_level
                }
                st.session_state.profile = profile
                agent = CoachAgent()
                st.session_state.workout_plan = agent.generate_plan(profile)
                st.success("ELITE PLAN READY!")
            except Exception as e:
                st.error("FAILED TO GENERATE PLAN. PLEASE CHECK YOUR .ENV FILE.")

# Main Content
st.markdown("""
    <div style='text-align: center; margin-top: -80px; margin-bottom: 60px;'>
        <h1 style='font-size: 10rem; letter-spacing: -8px; margin-bottom: 0px; 
            text-shadow: 0 0 50px rgba(0, 242, 254, 0.8); line-height: 0.8; font-weight: 900;'>
            GYM GENIE ELITE
        </h1>
        <p style='font-size: 1.8rem; color: #4FACFE; letter-spacing: 12px; margin-top: 10px; font-weight: 800; opacity: 1; text-transform: uppercase;'>
            AI-POWERED PERFORMANCE HUB
        </p>
    </div>
""", unsafe_allow_html=True)
st.divider()

tabs = ["📋 DASHBOARD", "💬 FITBOT CHAT", "📉 MACRO INTEL"]
if notes:
    tabs.append("🛡️ SAFE ZONE")

tab_objs = st.tabs(tabs)

with tab_objs[0]:
    if st.session_state.workout_plan:
        col_info, col_chart = st.columns([2, 1])
        with col_info:
            st.markdown(st.session_state.workout_plan)
        with col_chart:
            st.subheader("VISUAL INSIGHTS 📈")
            st.plotly_chart(create_macro_chart(st.session_state.profile.get('goal')), width='stretch')
            st.plotly_chart(create_intensity_gauge(st.session_state.profile.get('level')), width='stretch')
    else:
        st.markdown("""
            <div style='text-align: center; padding: 100px; background: rgba(0,0,0,0);'>
                <h2 style='opacity: 0.5;'>AWAITING YOUR PROFILE COMMANDS</h2>
                <p style='opacity: 0.3;'>USE THE SIDEBAR TO INITIALIZE THE GENIE</p>
            </div>
        """, unsafe_allow_html=True)

with tab_objs[1]:
    st.subheader("🤖 ELITE COACHING SWARM")
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("ASK YOUR TEAM ANYTHING..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            agent = CoachAgent()
            current_profile = st.session_state.profile if st.session_state.profile else {
                "age": age, "weight": weight, "level": level, "goal": goal, 
                "days": days, "meals": meals, "equipment": equipment, "notes": notes,
                "pain_level": st.session_state.pain_level
            }
            response_placeholder = st.empty()
            full_response = ""
            for chunk in agent.stream_chat_response(st.session_state.messages[:-1], prompt, current_profile):
                full_response += chunk
                response_placeholder.markdown(full_response + "▌")
            response_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})

with tab_objs[2]:
    st.subheader("📉 ELITE MACRO INTELLIGENCE")
    if not st.session_state.profile:
        st.warning("GENERATE A PLAN FIRST TO UNLOCK THESE METRICS.")
    else:
        p = st.session_state.profile
        bmr = 10 * p['weight'] + 6.25 * 175 - 5 * p['age'] + 5
        tdee = bmr * 1.5
        
        mcol1, mcol2, mcol3 = st.columns(3)
        mcol1.metric("BMR 🔥", f"{int(bmr)} KCAL", help="BASAL METABOLIC RATE")
        mcol2.metric("TDEE ⚡", f"{int(tdee)} KCAL", help="TOTAL DAILY ENERGY EXPENDITURE")
        mcol3.metric("TARGET 🥣", f"{int(tdee/p['meals'])} KCAL/MEAL")
        
        st.divider()
        
        vcol1, vcol2 = st.columns(2)
        with vcol1:
            st.write("### 🛰️ METABOLIC DRIVER RADAR")
            st.plotly_chart(create_burn_radar(p['age'], p['weight'], p['goal']), width='stretch')
        with vcol2:
            st.write("### ⏰ DAILY CALORIC TIMELINE")
            st.plotly_chart(create_meal_timeline(tdee, p['meals']), width='stretch')

if notes:
    with tab_objs[3]:
        st.subheader("🛡️ SAFE ZONE: INJURY RECOVERY PROTOCOL")
        sc1, sc2 = st.columns([1, 1])
        with sc1:
            st.plotly_chart(create_pain_gauge(st.session_state.pain_level), width='stretch')
        with sc2:
            st.markdown(f"### 🩹 INJURY ANALYSIS: {notes.upper()}")
            pain = st.session_state.pain_level
            
            if pain >= 8:
                st.error("🛑 **CRITICAL STATUS:** EXTREME PAIN DETECTED.")
                st.markdown("""
                **ELITE RECOVERY PROTOCOL:**
                - ❌ **ABSOLUTE ZERO:** NO TRAINING ALLOWED.
                - ⚠️ **NO PUSHING:** LIFTING WILL CAUSE PERMANENT DAMAGE.
                - 🩺 **MEDICAL ALERT:** CONSULT A PROFESSIONAL IMMEDIATELY.
                - 🧊 **FOCUS:** RICE METHOD (REST, ICE, COMPRESSION, ELEVATION).
                """)
            elif pain >= 5:
                st.warning("⚠️ **MODERATE STATUS:** SIGNIFICANT INJURY RISK.")
                st.markdown("""
                **MODIFIED TRAINING RULES:**
                - 📉 **LOAD REDUCTION:** REDUCE ALL WEIGHTS BY 50-70%.
                - 🚫 **NO COMPRESSION:** AVOID LIKELY STRESS POINTS ON THE INJURY.
                - 🧘 **MOBILITY FIRST:** FOCUS ON CONTROLLED RANGE OF MOTION.
                - 🛑 **STOP ON PINCH:** IF YOU FEEL A PINCH, THE SET IS OVER.
                """)
            else:
                st.info("✅ **MILD STATUS:** PROCEED WITH CAUTION.")
                st.markdown("""
                **PREVENTATIVE GUIDELINES:**
                - 🔥 **EXTENDED WARMUP:** SPEND 15 MINS WARMING UP THE AREA.
                - ⚖️ **FORM OVER LOAD:** ZERO EGO LIFTING. PERFECT REPS ONLY.
                - 🌊 **STAY HYDRATED:** RECOVERY REQUIRES OPTIMAL FLUIDS.
                - 🧪 **TESTING:** GRADUALLY TEST LOAD CAPABILITY EACH WEEK.
                """)
            
            st.divider()
            st.divider()
            if st.button("🆘 GET ELITE INJURY GUIDANCE"):
                st.markdown("### 🤖 COACH'S EMERGENCY PROTOCOL:")
                response_placeholder = st.empty()
                full_response = ""
                agent = CoachAgent()
                
                # Context for the injury
                injury_query = f"I have an injury: {notes}. My pain level is {st.session_state.pain_level}/10. Give me a 5-point 'Do and Don't' protocol for today's session."
                
                profile = {
                    "age": age, "weight": weight, "level": level, "goal": goal, 
                    "days": days, "meals": meals, "equipment": equipment, "notes": notes,
                    "pain_level": st.session_state.pain_level
                }
                
                for chunk in agent.stream_chat_response([], injury_query, profile):
                    full_response += chunk
                    response_placeholder.markdown(full_response + "▌")
                response_placeholder.markdown(full_response)
                
                # Also save to chat history for continuity
                st.session_state.messages.append({"role": "user", "content": injury_query})
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                st.info("💡 *This protocol has been saved to your FitBot Chat for reference.*")

            st.info("💡 **COACH'S ADVICE:** NEVER SACRIFICE LONG-TERM HEALTH FOR A SHORT-TERM GAIN. LISTEN TO YOUR BODY!")

# Footer
st.divider()
st.caption("⚡ POWERED BY GROQ ELITE INTELLIGENCE | DESIGNED FOR PEAK PERFORMANCE")
