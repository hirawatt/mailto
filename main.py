import streamlit as st

st.set_page_config(
    page_title='Mailto generator',
    page_icon='📧',
    layout='centered',
    initial_sidebar_state='collapsed',
    menu_items={
        'About': "# Thsi is a mailto generator app!"
    }
)

st.title('📧 Mailto generator')

# string operations
def string_clean(s: str) -> str:
    b = s.replace(" ", "%")
    return b

youremail = st.text_input("📩 Enter your email id", "yourmail@gmail.com,mailto@hirawat.in")
subject = string_clean(st.text_input("📖 Enter Subject", "Analyst Role"))



with st.expander("Extra fields"):
    cc = st.text_input("Enter CC", "cc@gmail.com")
    bcc = st.text_input("Enter BCC", "bcc@gmail.com")
    body = string_clean(st.text_area("Enter Body", "Hello,"))
    mailto_link = f"mailto:{youremail}?subject={subject}&cc={cc}&bcc={bcc}&body={body}"
    st.code(mailto_link)


yourmailto_link = f'mailto:{youremail}?subject={subject}'
st.write("✨ Your mailto link is:")
st.code(yourmailto_link, language="html")