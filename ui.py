import streamlit as st
from youtube_analyzer import build_youtube_agent

st.set_page_config(
    page_title = "Youtube Video Analyzer",
    layout = "centered"
)

st.title("🎥 AI YouTube Video Analyzer")

# st.cache_data is used to cache data or computation results 
# while st.cache_resource is used to cache reusable resources like ML models, database connections, and API clients."


@st.cache_resource # It return resource_object 
def get_agent():
    return build_youtube_agent()

agent =  get_agent()


# Input field for the YouTube video URL

video_url = st.text_input("Enter YouTube Video Link:")
button = st.button("Analyze Video") # True or False depending on whether the button is clicked or not

# print(video_url)
# print(button) 

if video_url and button:
    with st.spinner("Analyzing the Video..."):
        response = agent.run(f"Analyze this video: {video_url}")
    st.markdown("Analysis Report of Video:")
    st.markdown(response.content)
