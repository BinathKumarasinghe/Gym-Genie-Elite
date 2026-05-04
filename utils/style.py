import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&display=swap');

        :root {
            --primary-color: #00F2FE;
            --secondary-color: #4FACFE;
            --accent-color: #FF007A;
            --assistant-bg: linear-gradient(135deg, rgba(255, 0, 122, 0.15), rgba(139, 92, 246, 0.15));
            --user-bg: linear-gradient(135deg, rgba(0, 242, 254, 0.15), rgba(79, 172, 254, 0.15));
            --bg-dark: #020617;
            --card-bg: rgba(15, 23, 42, 0.8);
            --text-main: #FFFFFF;
            --glow: 0 0 25px rgba(0, 242, 254, 0.6);
        }

        /* Elite Moving Background */
        .stApp {
            background: #020617;
            background-image: 
                radial-gradient(at 0% 0%, rgba(0, 242, 254, 0.15) 0, transparent 50%), 
                radial-gradient(at 50% 0%, rgba(79, 172, 254, 0.1) 0, transparent 50%), 
                radial-gradient(at 100% 0%, rgba(255, 0, 122, 0.1) 0, transparent 50%);
            background-attachment: fixed;
            font-family: 'Outfit', sans-serif;
            color: var(--text-main) !important;
            font-size: 1.3rem !important;
            overflow-x: hidden;
        }

        /* Animated Moving Spheres */
        .stApp::before {
            content: "";
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: 
                radial-gradient(circle at 20% 30%, rgba(0, 242, 254, 0.05) 0%, transparent 40%),
                radial-gradient(circle at 80% 70%, rgba(255, 0, 122, 0.05) 0%, transparent 40%);
            animation: moveSpheres 20s linear infinite;
            z-index: -1;
        }

        @keyframes moveSpheres {
            0% { transform: translate(0, 0) scale(1); }
            33% { transform: translate(5%, 5%) scale(1.1); }
            66% { transform: translate(-5%, 10%) scale(0.9); }
            100% { transform: translate(0, 0) scale(1); }
        }

        /* Improved Global Text Visibility */
        p, li, label, div, span, .stMarkdown, .stText, .stTextArea, .stSelectbox, .stSlider {
            color: #FFFFFF !important;
            font-weight: 500 !important;
            line-height: 1.8 !important;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
            font-size: 1.3rem !important;
        }

        /* Specifically target the sidebar text */
        [data-testid="stSidebar"] * {
            font-size: 1.1rem !important;
            color: #FFFFFF !important;
        }

        /* Vibrant Interactive Cards - Only apply to items in tabs or specific sections */
        .stTabs [data-testid="stVerticalBlock"] > div:has(div.stMarkdown),
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:has(div.stMarkdown) {
            background: var(--card-bg);
            padding: 2.5rem;
            border-radius: 25px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(15px);
            margin-bottom: 2rem;
            box-shadow: 0 15px 35px rgba(0,0,0,0.4);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        /* Sidebar Header Highlights */
        [data-testid="stSidebar"] h1 {
            font-size: 2.5rem !important;
            background: linear-gradient(to right, #FFFFFF, var(--primary-color)) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            text-shadow: 0 0 15px rgba(0, 242, 254, 0.5) !important;
            margin-top: 1rem !important;
            margin-bottom: 2rem !important;
        }

        [data-testid="stSidebar"] h3 {
            font-size: 1.5rem !important;
            color: var(--primary-color) !important;
            -webkit-text-fill-color: var(--primary-color) !important;
            border-bottom: 1px solid rgba(0, 242, 254, 0.3);
            padding-bottom: 5px;
            margin-top: 2rem !important;
        }

        /* Elite Chat Interface */
        [data-testid="stChatMessage"] {
            border-radius: 25px !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            padding: 2rem !important;
            margin-bottom: 1.5rem !important;
            backdrop-filter: blur(10px) !important;
            box-shadow: 0 8px 25px rgba(0,0,0,0.3) !important;
        }

        /* User Message (Even) */
        [data-testid="stChatMessage"]:nth-child(even) {
            background: var(--user-bg) !important;
            border-right: 4px solid var(--primary-color) !important;
            animation: slideInRight 0.5s ease-out;
        }

        /* Assistant Message (Odd) */
        [data-testid="stChatMessage"]:nth-child(odd) {
            background: var(--assistant-bg) !important;
            border-left: 4px solid var(--accent-color) !important;
            animation: slideInLeft 0.5s ease-out;
        }

        @keyframes slideInLeft {
            from { opacity: 0; transform: translateX(-20px); }
            to { opacity: 1; transform: translateX(0); }
        }
        @keyframes slideInRight {
            from { opacity: 0; transform: translateX(20px); }
            to { opacity: 1; transform: translateX(0); }
        }

        /* Buttons with Elite Glow */
        .stButton > button {
            background: linear-gradient(135deg, var(--secondary-color), var(--primary-color)) !important;
            color: #020617 !important;
            border: none !important;
            padding: 1.2rem 2.5rem !important;
            border-radius: 18px !important;
            font-weight: 800 !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            width: 100%;
            text-transform: uppercase;
            letter-spacing: 3px;
            box-shadow: var(--glow);
            font-size: 1.1rem !important;
        }

        .stButton > button:hover {
            transform: scale(1.05);
            box-shadow: 0 0 45px rgba(0, 242, 254, 0.9);
            color: white !important;
        }

        /* Pulsing Injury Button */
        div.stButton > button:has(div:contains("🆘")) {
            animation: pulse 2s infinite !important;
            background: linear-gradient(135deg, var(--accent-color), #8B5CF6) !important;
        }

        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(255, 0, 122, 0.7); }
            70% { box-shadow: 0 0 0 20px rgba(255, 0, 122, 0); }
            100% { box-shadow: 0 0 0 0 rgba(255, 0, 122, 0); }
        }

        /* Elite Titles */
        h1, h2, h3 {
            background: linear-gradient(to right, #FFFFFF, var(--primary-color), var(--secondary-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 900 !important;
            letter-spacing: -2px !important;
            margin-bottom: 1.5rem !important;
            text-transform: uppercase;
        }

        /* Slider and Widgets */
        .stSlider [data-baseweb="slider"] { margin-bottom: 2rem; }
        
        /* Metric Styling */
        [data-testid="stMetricValue"] {
            color: var(--primary-color) !important;
            font-size: 2.5rem !important;
            font-weight: 800 !important;
        }

        /* Hide Default Footer */
        footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)
