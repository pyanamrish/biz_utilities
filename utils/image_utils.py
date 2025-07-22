import streamlit as st
from PIL import Image
import io
import requests
from datetime import datetime

def display_enhanced_image(image_data):
    if isinstance(image_data, dict) and 'url' in image_data:
        response = requests.get(image_data['url'])
        img = Image.open(io.BytesIO(response.content))
    elif isinstance(image_data, bytes):
        img = Image.open(io.BytesIO(image_data))
    else:
        st.error("Invalid image data format")
        return
    
    # Display image in a fixed container
    st.markdown("### 🖼️ Enhanced Product Image")
    
    # Create a container with fixed aspect ratio
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image(img, use_container_width=True, caption="Enhanced Product Image")
    
    # Download options
    st.markdown("### 💾 Download Options")
    col1, col2, col3 = st.columns(3)
    
    # Convert image to different formats
    with col1:
        png_bytes = io.BytesIO()
        img.save(png_bytes, format='PNG')
        png_bytes.seek(0)
        st.download_button(
            label="Download as PNG",
            data=png_bytes,
            file_name=f"enhanced_product_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png",
            mime="image/png"
        )
    
    with col2:
        jpg_bytes = io.BytesIO()
        rgb_img = img.convert('RGB')
        rgb_img.save(jpg_bytes, format='JPEG', quality=95)
        jpg_bytes.seek(0)
        st.download_button(
            label="Download as JPG",
            data=jpg_bytes,
            file_name=f"enhanced_product_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg",
            mime="image/jpeg"
        )
    
    with col3:
        webp_bytes = io.BytesIO()
        img.save(webp_bytes, format='WEBP', quality=95)
        webp_bytes.seek(0)
        st.download_button(
            label="Download as WebP",
            data=webp_bytes,
            file_name=f"enhanced_product_{datetime.now().strftime('%Y%m%d_%H%M%S')}.webp",
            mime="image/webp"
        )
    
def validate_image_upload(uploaded_file):
    if uploaded_file is None:
        return False, "Please upload an image"
    
    # Check file size (limit to 10MB)
    if uploaded_file.size > 10 * 1024 * 1024:
        return False, "Image size should be less than 10MB"
    
    # Check file type
    allowed_types = ['image/png', 'image/jpeg', 'image/jpg', 'image/webp']
    if uploaded_file.type not in allowed_types:
        return False, "Please upload a PNG, JPG, or WebP image"
    
    return True, "Valid image"