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

// Store the PWA install event
let deferredPrompt;
window.addEventListener('beforeinstallprompt', (event) => {
    event.preventDefault();
    deferredPrompt = event;
    document.getElementById('installPWA').style.display = 'block';
});

// Function to show the install prompt
function installPWA() {
    if (deferredPrompt) {
        deferredPrompt.prompt();
        deferredPrompt.userChoice.then((choiceResult) => {
            if (choiceResult.outcome === 'accepted') {
                console.log('User accepted the PWA installation');
            } else {
                console.log('User dismissed the PWA installation');
            }
            deferredPrompt = null;
        });
    }
}
</script>
""", unsafe_allow_html=True)

# Add a button to trigger installation
st.markdown("""
<button id="installPWA" onclick="installPWA()" style="display: none; padding: 10px; font-size: 16px; border-radius: 8px; background-color: #007bff; color: white; border: none; cursor: pointer;">
    Install App
</button>
""", unsafe_allow_html=True)

# Your Streamlit app content
st.title("Welcome to Streamlit PWA!")
st.write("This is a Progressive Web App built with Streamlit.")
