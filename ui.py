import streamlit as st
api_key = st.secrets.get('GEMINI_API_KEY')
st.write(f'Loaded : {api_key}')
# Email attributes configuration
EMAIL_ATTRIBUTES = {
    "formality": ["informal", "neutral", "formal", "very_formal"],
    "audience": ["friend", "colleague", "professional", "official", "very_official"],
    "language": ["arabic", "english", "french"],
    "length": ["short", "medium", "long"],
    "emotion": ["neutral", "friendly", "respectful", "urgent", "apologetic", "appreciative"],
    "tone": ["neutral", "polite", "angry", "kind", "firm", "friendly"],
    "authority": ["suggesting", "requesting", "instructing", "warning", "demanding"],
    "purpose": ['job_application', "information", "request", "complaint", "follow_up", "confirmation", "invitation", "apology", "thank_you"],
    "directness": ["direct", "moderate", "indirect"],
    "urgency": ["low", "normal", "high"],
    "structure": ["free", "bulleted", "step_by_step"],
    "personalization": ["generic", "semi_personalized", "fully_personalized"],
    "cta": ["reply", "approve", "schedule_meeting", "take_action", "no_action"]
}

from generator import generate_email
# Page configuration
st.set_page_config(
    page_title="AI Email Generator",
    page_icon="✉️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #e4e8ec 100%);
        padding: 0 !important;
    }
    
    /* Header */
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        text-align: center;
        color: white;
        margin: -1rem -1rem 2rem -1rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    
    .header-title {
        font-size: 3rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -1px;
    }
    
    .header-subtitle {
        font-size: 1.2rem;
        font-weight: 300;
        margin-top: 0.5rem;
        opacity: 0.95;
    }
    
    
   
    
    .section-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Textarea Styling */
    .stTextArea textarea {
        border-radius: 12px;
        border: 2px solid #e2e8f0;
        padding: 1rem;
        font-size: 1rem;
        outline: none !important;
        transition: all 0.3s;
        resize: vertical;
    }
    
    .stTextArea textarea:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
        outline: none !important;
    }
    
    .stTextArea textarea:focus-visible {
        outline: none !important;
        border-color: #667eea !important;
    }
    
    /* Select boxes */
    .stSelectbox > div > div {
        border-radius: 10px;
        border: 2px solid #e2e8f0;
        transition: all 0.3s;
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        background-color: transparent;
        border-bottom: none;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: white;
        border-radius: 10px;
        padding: 0.75rem 1.5rem;
        font-weight: 500;
        border: 2px solid #e2e8f0;
        color: #4a5568;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-color: transparent;
    }
    
    .stTabs [data-baseweb="tab-border"] {
        display: none;
    }
    
    .stTabs [data-baseweb="tab-highlight"] {
        display: none;
    }
    
    /* Generate Button */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        height: 3.5rem;
        font-size: 1.2rem;
        font-weight: 600;
        border-radius: 15px;
        border: none;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(102, 126, 234, 0.5);
    }
    
    /* Email Preview Container */
    .email-preview-container {
        background: white;
        border-radius: 20px;
        padding: 0;
        box-shadow: 0 2px 20px rgba(0,0,0,0.08);
        overflow: hidden;
    }
    
    .email-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        color: white;
    }
    
    .email-label {
        font-size: 0.9rem;
        font-weight: 500;
        opacity: 0.9;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.5rem;
    }
    
    .email-subject {
        font-size: 1.8rem;
        font-weight: 700;
        line-height: 1.4;
        margin: 0;
    }
    
    .email-body-container {
        padding: 2.5rem;
        background: #fafbfc;
    }
    
    .email-body {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        border: 1px solid #e2e8f0;
        line-height: 1.8;
        font-size: 1.05rem;
        color: #2d3748;
        white-space: pre-wrap;
        word-wrap: break-word;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    
    /* Action Buttons */
    .action-buttons {
        padding: 1.5rem 2rem;
        background: white;
        border-top: 1px solid #e2e8f0;
        display: flex;
        gap: 1rem;
    }
    
    .stDownloadButton > button {
        background-color: #48bb78;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s;
        width: 100%;
    }
    
    .stDownloadButton > button:hover {
        background-color: #38a169;
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(72, 187, 120, 0.3);
    }
    
    /* Placeholder */
    .placeholder-container {
        text-align: center;
        padding: 6rem 2rem;
        color: #a0aec0;
    }
    
    .placeholder-icon {
        font-size: 5rem;
        margin-bottom: 1rem;
        opacity: 0.3;
    }
    
    .placeholder-title {
        font-size: 1.8rem;
        font-weight: 600;
        color: #4a5568;
        margin-bottom: 0.5rem;
    }
    
    .placeholder-text {
        font-size: 1.1rem;
        color: #718096;
    }
    
    /* Info box */
    .stInfo {
        background-color: #ebf4ff;
        border-left: 4px solid #667eea;
        border-radius: 10px;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="header-container">
        <h1 class="header-title">✉️ AI Email Generator</h1>
        <p class="header-subtitle">Create professional, personalized emails in seconds with AI</p>
    </div>
""", unsafe_allow_html=True)

# Initialize session state
if 'generated_email' not in st.session_state:
    st.session_state.generated_email = None



# Two column layout
col1, col2 = st.columns([5, 7], gap="large")

with col1:
    st.markdown('<p class="section-title">📝 Configuration</p>', unsafe_allow_html=True)
    myName = st.text_input("Email Sender Name", placeholder="John Doe", label_visibility="visible")
    # Context input
    context = st.text_area(
        "What's your email about?",
        placeholder="Example: I need to request a meeting with my manager to discuss the Q4 project timeline and budget allocation...",
        height=180,
        label_visibility="visible"
    )
    receiver_name = st.text_input("Email Receiver Name", placeholder="Jane Smith", label_visibility="visible")
    receiver_title = st.text_input("Email Receiver Title", placeholder="Teacher", label_visibility="visible")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Tabs for attributes
    tab1, tab2, tab3 = st.tabs(["🎯 Essentials", "🎨 Style & Tone", "⚙️ Advanced"])
    
    with tab1:
        st.markdown("<br>", unsafe_allow_html=True)
        col_a, col_b = st.columns(2)
        with col_a:
            language = st.selectbox("🌐 Language", EMAIL_ATTRIBUTES["language"], index=1)
            purpose = st.selectbox("🎯 Purpose", EMAIL_ATTRIBUTES["purpose"])
        with col_b:
            audience = st.selectbox("👥 Audience", EMAIL_ATTRIBUTES["audience"], index=2)
            length = st.selectbox("📏 Length", EMAIL_ATTRIBUTES["length"], index=1)
    
    with tab2:
        st.markdown("<br>", unsafe_allow_html=True)
        col_a, col_b = st.columns(2)
        with col_a:
            formality = st.selectbox("👔 Formality", EMAIL_ATTRIBUTES["formality"], index=2)
            tone = st.selectbox("🗣️ Tone", EMAIL_ATTRIBUTES["tone"], index=1)
        with col_b:
            emotion = st.selectbox("💭 Emotion", EMAIL_ATTRIBUTES["emotion"], index=2)
            directness = st.selectbox("🎯 Directness", EMAIL_ATTRIBUTES["directness"], index=1)
    
    with tab3:
        st.markdown("<br>", unsafe_allow_html=True)
        col_a, col_b = st.columns(2)
        with col_a:
            authority = st.selectbox("⚡ Authority", EMAIL_ATTRIBUTES["authority"], index=1)
            urgency = st.selectbox("⏰ Urgency", EMAIL_ATTRIBUTES["urgency"], index=1)
            structure = st.selectbox("📋 Structure", EMAIL_ATTRIBUTES["structure"])
        with col_b:
            personalization = st.selectbox("✨ Personalization", EMAIL_ATTRIBUTES["personalization"], index=1)
            cta = st.selectbox("📣 Call to Action", EMAIL_ATTRIBUTES["cta"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Generate button
    if st.button("🚀 Generate Email"):
        if not context.strip():
            st.error("⚠️ Please describe what your email is about!")
        else:
            with st.spinner("✨ Crafting your perfect email..."):
                data = {
                    "context": context,
                    "myName": myName,
                    "receiver_name": receiver_name,
                    "receiver_title": receiver_title,
                    "formality": formality,
                    "audience": audience,
                    "language": language,
                    "length": length,
                    "emotion": emotion,
                    "tone": tone,
                    "authority": authority,
                    "purpose": purpose,
                    "directness": directness,
                    "urgency": urgency,
                    "structure": structure,
                    "personalization": personalization,
                    "cta": cta
                }
                email = generate_email(data, api_key)
                
                st.session_state.generated_email = email
                
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if st.session_state.generated_email:
        email = st.session_state.generated_email
        st.write(f'Email : {email}')
        
        st.markdown('<div class="email-preview-container">', unsafe_allow_html=True)
        
        # Email header with subject
        st.markdown(f"""
            <div class="email-header">
                <div class="email-label">Subject Line</div>
                <h2 class="email-subject">{email['subject']}</h2>
            </div>
        """, unsafe_allow_html=True)
        
        # Email body
        st.markdown(f"""
            <div class="email-body-container">
                <div class="email-body">{email['body']}</div>
            </div>
        """, unsafe_allow_html=True)
        
        # Action buttons
        st.markdown('<div class="action-buttons">', unsafe_allow_html=True)
        col_btn1, col_btn2 = st.columns(2)
        
        with col_btn1:
            st.download_button(
                label="📥 Download Email",
                data=f"Subject: {email['subject']}\n\n{email['body']}",
                file_name="generated_email.txt",
                mime="text/plain"
            )
        
        with col_btn2:
            if st.button("📋 Copy Text"):
                st.info("💡 Select and copy the text from the email above")
        
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        # Beautiful placeholder
        st.markdown('<div class="email-preview-container">', unsafe_allow_html=True)
        st.markdown("""
            <div class="placeholder-container">
                <div class="placeholder-icon">✉️</div>
                <h3 class="placeholder-title">No Email Yet</h3>
                <p class="placeholder-text">Configure your preferences and click<br>"Generate Email" to create your message</p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer tip
st.markdown("<br>", unsafe_allow_html=True)
st.info("💡 **Pro Tip:** The more detailed your context, the better your generated email will be!")