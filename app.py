import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import time
from datetime import datetime
import json

# Page config
st.set_page_config(
    page_title="AI Chat Assistant", 
    page_icon="🤖", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for animations and styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        animation: fadeInDown 1s ease-out;
    }
    
    .chat-message {
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 15px;
        animation: slideInUp 0.5s ease-out;
        max-width: 80%;
    }
    
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin-left: auto;
        text-align: right;
    }
    
    .bot-message {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        margin-right: auto;
    }
    
    .typing-indicator {
        display: inline-block;
        animation: pulse 1.5s infinite;
    }
    
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes slideInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    .stTextInput > div > div > input {
        border-radius: 20px;
        border: 2px solid #667eea;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'model_settings' not in st.session_state:
    st.session_state.model_settings = {}

# Advanced configuration
MODELS = {
    "deepseek-r1:latest": {"icon": "🧠", "desc": "Advanced reasoning model"},
    "llama3": {"icon": "🦙", "desc": "Fast and reliable"},
    "mistral": {"icon": "⚡", "desc": "Efficient performance"}
}

SYSTEM_PROMPTS = {
    "Assistant": "You are a helpful AI assistant. Provide clear, accurate responses.",
    "Creative Writer": "You are a creative writing assistant. Help with storytelling and creative content.",
    "Code Helper": "You are a programming assistant. Help with coding questions and debugging.",
    "Teacher": "You are an educational assistant. Explain concepts clearly with examples."
}

def create_llm_chain(model, system_prompt, temp, max_tokens):
    """Create LangChain pipeline with error handling"""
    try:
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("user", "{question}")
        ])
        llm = Ollama(model=model, temperature=temp, num_predict=max_tokens)
        return prompt | llm | StrOutputParser()
    except Exception as e:
        st.error(f"Error creating model: {e}")
        return None

def generate_response(question, chain):
    """Generate response with streaming effect"""
    if not chain:
        return "Error: Model not available"
    
    try:
        response = chain.invoke({"question": question})
        return response
    except Exception as e:
        return f"Error generating response: {e}"

def display_chat_message(message, role):
    """Display chat message with animation"""
    css_class = "user-message" if role == "user" else "bot-message"
    icon = "👤" if role == "user" else "🤖"
    
    st.markdown(f"""
    <div class="chat-message {css_class}">
        <strong>{icon} {role.title()}:</strong><br>
        {message}
    </div>
    """, unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header"><h1>🤖 Advanced AI Chat Assistant</h1><p>Powered by Ollama & LangChain</p></div>', unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Model selection
    selected_model = st.selectbox(
        "🤖 Model",
        options=list(MODELS.keys()),
        format_func=lambda x: f"{MODELS[x]['icon']} {x} - {MODELS[x]['desc']}"
    )
    
    # System prompt selection
    system_role = st.selectbox("🎭 Assistant Role", list(SYSTEM_PROMPTS.keys()))
    
    # Advanced settings in expander
    with st.expander("🔧 Advanced Settings"):
        temperature = st.slider("🌡️ Temperature", 0.0, 1.0, 0.7, 0.1)
        max_tokens = st.slider("📝 Max Tokens", 50, 500, 150)
        
    # Chat controls
    st.header("💬 Chat Controls")
    
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    # Export chat
    if st.button("💾 Export Chat", use_container_width=True) and st.session_state.messages:
        chat_data = {
            "timestamp": datetime.now().isoformat(),
            "model": selected_model,
            "messages": st.session_state.messages
        }
        st.download_button(
            "📥 Download JSON",
            json.dumps(chat_data, indent=2),
            f"chat_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            "application/json"
        )
    
    # Statistics
    if st.session_state.messages:
        st.header("📊 Chat Stats")
        msg_count = len(st.session_state.messages)
        user_msgs = len([m for m in st.session_state.messages if m['role'] == 'user'])
        st.metric("Total Messages", msg_count)
        st.metric("Your Messages", user_msgs)

# Main chat interface
col1, col2 = st.columns([3, 1])

with col1:
    # Display chat history
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.messages:
            display_chat_message(message['content'], message['role'])

    # Input area
    user_input = st.text_input(
        "💭 Your message:",
        placeholder="Ask me anything...",
        key="user_input"
    )

with col2:
    st.header("🎯 Quick Actions")
    
    quick_prompts = [
        "Explain quantum computing",
        "Write a haiku",
        "Debug my Python code",
        "Summarize latest AI news"
    ]
    
    for prompt in quick_prompts:
        if st.button(f"💡 {prompt}", use_container_width=True):
            user_input = prompt
            break

# Process user input
if user_input and user_input.strip():
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "timestamp": datetime.now()
    })
    
    # Show typing indicator
    with st.spinner("🤔 Thinking..."):
        # Create chain
        chain = create_llm_chain(
            selected_model,
            SYSTEM_PROMPTS[system_role],
            temperature,
            max_tokens
        )
        
        # Generate response
        if chain:
            response = generate_response(user_input, chain)
            
            # Add bot response
            st.session_state.messages.append({
                "role": "assistant",
                "content": response,
                "timestamp": datetime.now()
            })
    
    st.rerun()

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "Built with ❤️ using Streamlit, LangChain & Ollama"
    "</div>", 
    unsafe_allow_html=True
)