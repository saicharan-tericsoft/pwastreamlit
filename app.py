import streamlit as st

# Set the page title and icon
st.set_page_config(
    page_title="Streamlit PWA",
    page_icon="📱",
    layout="centered"
)

# Add the manifest file
st.markdown("""
<link rel="manifest" href="/static/manifest.json">
""", unsafe_allow_html=True)

# Register the service worker
st.markdown("""
<script>
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/static/service-worker.js')
    .then((registration) => {
      console.log('Service Worker registered with scope:', registration.scope);
    })
    .catch((error) => {
      console.error('Service Worker registration failed:', error);
    });
}
</script>
""", unsafe_allow_html=True)

# Your Streamlit app content
st.title("Welcome to Streamlit PWA!")
st.write("This is a Progressive Web App built with Streamlit.")
