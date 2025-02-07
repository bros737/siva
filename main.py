import streamlit as st
from streamlit_chat import message
import random
import streamlit_custome_css as siva


# Sample school-related Q&A
def chatbot_response(user_input):
    responses = {
        "What are the school timings?": "Our school operates from 8:00 AM to 3:00 PM, Monday to Friday.",
        "What courses are available?": "We offer Science, Commerce, and Arts streams with various electives.",
        "How to apply for admission?": "Visit our school website and fill out the admission form under the Admissions section.",
        "Who is the principal?": "Dr. John Doe is the current principal of our school.",
        "What is the future of this school?": "We aim to integrate AI-driven learning and smart classrooms in the next five years.",
        "Is there a school transport facility?": "Yes, we provide bus services covering various routes across the city.",
        "What is the student-teacher ratio?": "Our student-teacher ratio is approximately 25:1, ensuring personalized attention.",
        "Are scholarships available?": "Yes, we offer merit-based and need-based scholarships. Please check our website for details.",
        "How can parents communicate with teachers?": "Parents can schedule meetings through the school portal or contact teachers via email.",
        "hi":"hi da mappla",
        "hello":"hello nice to meet you",
        "school name":"CVD School"
    }
    return responses.get(user_input, "I'm not sure about that. Please contact the school administration.")

# Page Navigation
st.set_page_config(page_title="School Chatbot", layout="wide")

menu = ["Chatbot", "Login", "Send Feedback"]
choice = st.sidebar.radio("Navigation", menu)

# Chatbot Page
if choice == "Chatbot":
    siva.bg_image("https://th.bing.com/th/id/OIP.zzZEZfijmgA1wZhJvh_bWwHaEK?rs=1&pid=ImgDetMain")
    st.title("School Chatbot 🤖")
    

    
    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    
    st.markdown("<div class='chat-box'>", unsafe_allow_html=True)
    for i, (user_msg, bot_msg) in enumerate(st.session_state["messages"]):
        message(user_msg, is_user=True, key=str(i) + "_user")
        message(bot_msg, is_user=False, key=str(i) + "_bot")
    st.markdown("</div>", unsafe_allow_html=True)
    
    user_input = st.text_input("", placeholder="Ask me a question about the school...", key="chat_input", help="Type your message here",)
    if st.button("Send"):
        if user_input:
            response = chatbot_response(user_input)
            st.session_state["messages"].append((user_input, response))
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Login link on top right
    st.sidebar.write("[Login](#Login)")

# Login Page
elif choice == "Login":
    st.title("Login Page 🔑")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "password":
            st.success("Logged in successfully!")
        else:
            st.error("Invalid credentials")

# Feedback Page
elif choice == "Send Feedback":
    st.title("Send Feedback 📝")
    feedback = st.text_area("Enter your feedback about the chatbot or school services:")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")