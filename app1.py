import streamlit as st

# Function to generate cold email based on inputs
def generate_email(sender_name, recipient_name, company, purpose, custom_message, closing):
    email_template = f"""
    Hi {recipient_name},
    
    I hope this message finds you well. My name is {sender_name}, and I'm reaching out to discuss {purpose}. 
    I’ve been following {company} closely and believe that there’s a great opportunity for us to collaborate 
    or find ways I can add value to your organization.
    
    {custom_message}
    
    Let me know if you’d be open to having a conversation. Looking forward to hearing your thoughts.

    Best regards,
    {sender_name}
    
    {closing}
    """
    return email_template

# Streamlit UI layout with logo and colors
def main():
    # Adding a logo (You can replace this with a custom image URL)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Markdown-mark.svg/1200px-Markdown-mark.svg.png", width=100)

    # Title with color
    st.markdown("<h1 style='text-align: center; color: blue;'>Cold Email Generator</h1>", unsafe_allow_html=True)
    st.write("Generate personalized cold emails quickly and easily!")

    # Background color
    st.markdown("""
        <style>
        .main {
            background-color: #f0f0f0;
        }
        </style>
        """, unsafe_allow_html=True)

    # User input fields with color styling
    sender_name = st.text_input("Your Name", value="Jane Smith")
    recipient_name = st.text_input("Recipient's Name", value="John Doe")
    company = st.text_input("Company Name", value="Acme Corp")
    purpose = st.text_input("Purpose (e.g., partnership, job inquiry)", value="partnership opportunity")
    custom_message = st.text_area("Custom Message", value="I believe my experience in [your expertise] can contribute significantly to your goals.")
    closing = st.text_input("Closing", value="Looking forward to connecting.")

    # Button with custom style
    generate_button = st.markdown("""
        <style>
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
            }
        </style>
    """, unsafe_allow_html=True)

    if st.button("Generate Email"):
        email = generate_email(sender_name, recipient_name, company, purpose, custom_message, closing)
        st.subheader("Generated Email:")
        st.text_area("Cold Email", value=email, height=300)

if __name__ == '__main__':
    main()
