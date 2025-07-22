import streamlit as st
from utilities.product_details import ProductDetailsGenerator
from utilities.image_enhancer import ImageEnhancer
from utils.formatters import display_product_content, format_error_message
from utils.image_utils import display_enhanced_image, validate_image_upload
from prompts.image_enhancer_prompts import SHOT_ANGLES, BACKGROUNDS, CATEGORIES, ASPECT_RATIOS, OUTPUT_FORMATS, CATEGORY_SUGGESTIONS
import os

# Page configuration
st.set_page_config(
    page_title="Business Utilities",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with modern professional theme
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    .stApp {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f2937;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(135deg, #1f2937 0%, #4f46e5 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .utility-card {
        background: linear-gradient(145deg, #ffffff 0%, #f8fafc 100%);
        padding: 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #f8fafc 0%, #ffffff 100%);
    }
    
    .nav-item {
        padding: 12px 16px;
        margin: 4px 0;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.2s ease;
        border: 1px solid transparent;
        font-weight: 500;
        color: #4b5563;
    }
    
    .nav-item:hover {
        background-color: #e0e7ff;
        color: #4f46e5;
        border-color: #c7d2fe;
    }
    
    .nav-item.active {
        background-color: #4f46e5;
        color: white;
        box-shadow: 0 2px 4px rgba(79, 70, 229, 0.3);
    }
    
    .logo-container {
        text-align: center;
        padding: 1rem 0 2rem 0;
        border-bottom: 1px solid #e5e7eb;
        margin-bottom: 1.5rem;
    }
    
    .logo-container img {
        max-width: 120px;
        height: auto;
        border-radius: 8px;
    }
    
    .stButton > button {
        background-color: #4f46e5;
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        padding: 0.5rem 1rem;
        transition: all 0.2s ease;
    }
    
    .stButton > button:hover {
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.4);
        transform: translateY(-1px);
    }
    
    .stSelectbox > div > div {
        border-radius: 8px;
        border-color: #d1d5db;
    }
    
    .stTextInput > div > div > input {
        border-radius: 8px;
        border-color: #d1d5db;
    }
    
    .stTextArea > div > div > textarea {
        border-radius: 8px;
        border-color: #d1d5db;
    }
    
    h1, h2, h3 {
        color: #1f2937;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">Business Utilities</h1>', unsafe_allow_html=True)

# Sidebar for utility selection
with st.sidebar:
    # Logo section - top left positioning
    try:
        st.image("assets/logo.png",use_container_width=False)
    except:
        st.markdown("""
        <div style="background: #f3f4f6; padding: 8px; border: 2px dashed #d1d5db; border-radius: 8px; width: 80px; margin-bottom: 1rem;">
            <p style="margin: 0; color: #6b7280; font-size: 10px; text-align: center;">Logo</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div style="margin-bottom: 1.5rem;"></div>', unsafe_allow_html=True)
    
    # Navigation buttons
    if 'selected_utility' not in st.session_state:
        st.session_state.selected_utility = "Product Details Generator"
    
    # Initialize history if not exists
    if 'image_history' not in st.session_state:
        st.session_state.image_history = []
    
    # Navigation buttons with custom styling
    if st.button("📝 Zyl - Narrato", key="nav_product", use_container_width=True):
        st.session_state.selected_utility = "Product Details Generator"
        st.rerun()
    
    if st.button("🖼️ Zyl - Pixly", key="nav_image", use_container_width=True):
        st.session_state.selected_utility = "Product Image Enhancer"
        st.rerun()
        
    if st.button("📚 History", key="nav_history", use_container_width=True):
        st.session_state.selected_utility = "History"
        st.rerun()
    
    utility = st.session_state.selected_utility
    
    
# Check for API keys
try:
    from config.settings import OPENAI_API_KEY, FAL_KEY
except ValueError as e:
    st.error(f"Configuration Error: {str(e)}")
    st.info("Please set up your API keys in the .env file or Streamlit secrets")
    st.stop()

# Main content area
if utility == "Product Details Generator":
    st.markdown("## Product Details Generator")
    st.markdown("Generate compelling product descriptions and SEO-optimized content")
    
    with st.form("product_details_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            product_name = st.text_input(
                "Product Name *",
                placeholder="e.g., Premium Stainless Steel Water Bottle",
                help="Enter the name of your product"
            )
            
            keywords = st.text_area(
                "Keywords/Features (Optional)",
                placeholder="e.g., BPA-free, insulated, leak-proof, 24oz capacity",
                help="Enter product features or keywords separated by commas"
            )
            
            weight = st.text_input(
                "Weight (Optional)",
                placeholder="e.g., 1.2 lbs",
                help="Enter product weight"
            )
        
        with col2:
            st.markdown("**Product Dimensions (cm)**")
            dim_col1, dim_col2, dim_col3 = st.columns(3)
            
            with dim_col1:
                length = st.number_input(
                    "Length",
                    min_value=0.0,
                    step=0.1,
                    help="Length in centimeters"
                )
            
            with dim_col2:
                breadth = st.number_input(
                    "Breadth",
                    min_value=0.0,
                    step=0.1,
                    help="Breadth in centimeters"
                )
            
            with dim_col3:
                height = st.number_input(
                    "Height",
                    min_value=0.0,
                    step=0.1,
                    help="Height in centimeters"
                )
        
        # Prompt preview functionality
        st.markdown("---")
        show_prompt = st.checkbox("🔍 Preview & Edit System Prompt", help="Preview the prompt that will be sent to the AI model")
        
        custom_prompt = None
        if show_prompt and product_name:
            try:
                generator = ProductDetailsGenerator()
                preview_prompt = generator.preview_prompt(
                    product_name=product_name,
                    keywords=keywords,
                    length=str(length) if length > 0 else "",
                    breadth=str(breadth) if breadth > 0 else "",
                    height=str(height) if height > 0 else "",
                    weight=weight
                )
                
                st.markdown("**System Prompt Preview:**")
                custom_prompt = st.text_area(
                    "Edit the prompt if needed:",
                    value=preview_prompt,
                    height=300,
                    help="You can modify this prompt before sending to the AI model"
                )
                
                if custom_prompt != preview_prompt:
                    st.info("✏️ Using custom edited prompt")
            except Exception as e:
                st.warning(f"Cannot preview prompt: {str(e)}")
        
        col1, col2 = st.columns(2)
        with col1:
            preview_button = st.form_submit_button("👁️ Preview Prompt Only", use_container_width=True)
        with col2:
            submit_button = st.form_submit_button("🚀 Generate Content", use_container_width=True)
    
    if preview_button:
        if not product_name:
            st.error("Please enter a product name")
        else:
            try:
                generator = ProductDetailsGenerator()
                preview_prompt = generator.preview_prompt(
                    product_name=product_name,
                    keywords=keywords,
                    length=str(length) if length > 0 else "",
                    breadth=str(breadth) if breadth > 0 else "",
                    height=str(height) if height > 0 else "",
                    weight=weight
                )
                
                st.markdown("### 👁️ System Prompt Preview")
                st.code(preview_prompt, language="text")
                
            except Exception as e:
                st.markdown(format_error_message(str(e)), unsafe_allow_html=True)
    
    if submit_button:
        if not product_name:
            st.error("Please enter a product name")
        else:
            with st.spinner("Generating product content..."):
                try:
                    generator = ProductDetailsGenerator()
                    content = generator.generate_content(
                        product_name=product_name,
                        keywords=keywords,
                        length=str(length) if length > 0 else "",
                        breadth=str(breadth) if breadth > 0 else "",
                        height=str(height) if height > 0 else "",
                        weight=weight,
                        custom_prompt=custom_prompt if show_prompt and custom_prompt else None
                    )
                    
                    display_product_content(content)
                    
                except Exception as e:
                    st.markdown(format_error_message(str(e)), unsafe_allow_html=True)

elif utility == "Product Image Enhancer":
    st.markdown("## 🖼️ Product Image Enhancer")
    st.markdown("Transform your product images with AI-powered enhancements")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        uploaded_file = st.file_uploader(
            "Upload Product Image",
            type=['png', 'jpg', 'jpeg', 'webp'],
            help="Upload a product image to enhance"
        )
        
        if uploaded_file:
            st.image(uploaded_file, caption="Original Image", use_container_width=True)
    
    with col2:
        # Category-specific prompt suggestions (outside form for interactivity)
        shot_angle = st.selectbox(
            "Shot Angle",
            SHOT_ANGLES,
            help="Select the desired camera angle"
        )
        
        background = st.selectbox(
            "Background Style",
            BACKGROUNDS,
            help="Choose the background style"
        )
        
        category = st.selectbox(
            "Product Category",
            CATEGORIES,
            help="Select your product category"
        )
        
        # Initialize suggestion state
        if 'selected_suggestion' not in st.session_state:
            st.session_state.selected_suggestion = ""
            
        # Show category suggestions
        if category in CATEGORY_SUGGESTIONS:
            st.markdown("**💡 Prompt Suggestions for " + category + ":**")
            
            suggestions = CATEGORY_SUGGESTIONS[category]
            for i, suggestion in enumerate(suggestions):
                # Create a shorter display text for the button
                button_text = suggestion[:60] + "..." if len(suggestion) > 60 else suggestion
                
                if st.button(f"📝 {button_text}", key=f"suggestion_{category}_{i}", use_container_width=True):
                    st.session_state.selected_suggestion = suggestion
                    st.rerun()
            
            st.markdown("*Click any suggestion above to prefill the Additional Instructions field*")
            st.markdown("---")
        
        with st.form("image_enhancement_form"):
            aspect_ratio = st.selectbox(
                "Output Aspect Ratio",
                ASPECT_RATIOS,
                help="Choose the desired aspect ratio"
            )
            
            output_format = st.selectbox(
                "Output Format",
                OUTPUT_FORMATS,
                help="Choose the output image format"
            )
            
            # Use the selected suggestion as default value
            default_instructions = st.session_state.selected_suggestion if st.session_state.selected_suggestion else ""
            
            additional_instructions = st.text_area(
                "Additional Instructions (Optional)",
                value=default_instructions,
                placeholder="e.g., Make colors more vibrant, add subtle shadows",
                help="Any specific requirements for the enhancement"
            )
            
            # Prompt preview functionality
            st.markdown("---")
            show_prompt = st.checkbox("🔍 Preview & Edit Enhancement Prompt", help="Preview the prompt that will be sent to the AI model")
            
            custom_prompt = None
            if show_prompt:
                try:
                    enhancer = ImageEnhancer()
                    preview_prompt = enhancer.preview_prompt(
                        shot_angle=shot_angle,
                        background=background,
                        category=category,
                        additional_instructions=additional_instructions
                    )
                    
                    st.markdown("**Enhancement Prompt Preview:**")
                    custom_prompt = st.text_area(
                        "Edit the prompt if needed:",
                        value=preview_prompt,
                        height=200,
                        help="You can modify this prompt before sending to the AI model"
                    )
                    
                    if custom_prompt != preview_prompt:
                        st.info("✏️ Using custom edited prompt")
                except Exception as e:
                    st.warning(f"Cannot preview prompt: {str(e)}")
            
            col1, col2 = st.columns(2)
            with col1:
                preview_button = st.form_submit_button("👁️ Preview Prompt Only", use_container_width=True)
            with col2:
                enhance_button = st.form_submit_button("✨ Enhance Image", use_container_width=True)
    
    if preview_button:
        try:
            enhancer = ImageEnhancer()
            preview_prompt = enhancer.preview_prompt(
                shot_angle=shot_angle,
                background=background,
                category=category,
                additional_instructions=additional_instructions
            )
            
            st.markdown("### 👁️ Enhancement Prompt Preview")
            st.code(preview_prompt, language="text")
            
        except Exception as e:
            st.markdown(format_error_message(str(e)), unsafe_allow_html=True)
    
    if enhance_button and uploaded_file:
        is_valid, message = validate_image_upload(uploaded_file)
        
        if not is_valid:
            st.error(message)
        else:
            with st.spinner("Enhancing your product image..."):
                try:
                    enhancer = ImageEnhancer()
                    image_bytes = uploaded_file.read()
                    
                    enhanced_image = enhancer.enhance_image(
                        image_bytes=image_bytes,
                        shot_angle=shot_angle,
                        background=background,
                        category=category,
                        aspect_ratio=aspect_ratio,
                        output_format=output_format,
                        additional_instructions=additional_instructions,
                        custom_prompt=custom_prompt if show_prompt and custom_prompt else None
                    )
                    
                    # Add to history
                    import base64
                    from datetime import datetime
                    import requests
                    
                    # Convert images to base64 for storage
                    original_b64 = base64.b64encode(image_bytes).decode()
                    
                    # Handle enhanced image - it's a dict with 'url' key
                    if isinstance(enhanced_image, dict) and 'url' in enhanced_image:
                        response = requests.get(enhanced_image['url'])
                        enhanced_bytes = response.content
                    elif isinstance(enhanced_image, bytes):
                        enhanced_bytes = enhanced_image
                    else:
                        raise Exception("Unexpected enhanced image format")
                    
                    enhanced_b64 = base64.b64encode(enhanced_bytes).decode()
                    
                    history_entry = {
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'original_image': original_b64,
                        'enhanced_image': enhanced_b64,
                        'filename': uploaded_file.name,
                        'shot_angle': shot_angle,
                        'background': background,
                        'category': category,
                        'aspect_ratio': aspect_ratio,
                        'output_format': output_format,
                        'additional_instructions': additional_instructions,
                        'custom_prompt': custom_prompt if show_prompt and custom_prompt else None
                    }
                    
                    st.session_state.image_history.append(history_entry)
                    
                    # Keep only last 10 entries to prevent memory issues
                    if len(st.session_state.image_history) > 10:
                        st.session_state.image_history = st.session_state.image_history[-10:]
                    
                    display_enhanced_image(enhanced_image)
                    
                except Exception as e:
                    st.markdown(format_error_message(str(e)), unsafe_allow_html=True)
    
    elif enhance_button and not uploaded_file:
        st.error("Please upload an image first")

elif utility == "History":
    st.markdown("## 📚 Image Enhancement History")
    st.markdown("View your previous image enhancements and download results")
    
    if not st.session_state.image_history:
        st.info("No image enhancement history found. Generate some images first!")
    else:
        st.markdown(f"**Total Enhancements: {len(st.session_state.image_history)}**")
        st.markdown("---")
        
        # Display history in reverse order (newest first)
        for i, entry in enumerate(reversed(st.session_state.image_history)):
            with st.container():
                st.markdown(f"### Enhancement #{len(st.session_state.image_history) - i}")
                st.markdown(f"**Created:** {entry['timestamp']} | **Original File:** {entry['filename']}")
                
                col1, col2, col3 = st.columns([1, 1, 1])
                
                with col1:
                    st.markdown("**Original Image**")
                    try:
                        import base64
                        original_bytes = base64.b64decode(entry['original_image'])
                        st.image(original_bytes, use_container_width=True)
                        
                        # Download button for original
                        st.download_button(
                            label="⬇️ Download Original",
                            data=original_bytes,
                            file_name=f"original_{entry['filename']}",
                            mime=f"image/{entry['output_format']}"
                        )
                    except Exception as e:
                        st.error("Error loading original image")
                
                with col2:
                    st.markdown("**Enhanced Image**")
                    try:
                        enhanced_bytes = base64.b64decode(entry['enhanced_image'])
                        st.image(enhanced_bytes, use_container_width=True)
                        
                        # Download button for enhanced image
                        st.download_button(
                            label="⬇️ Download Enhanced",
                            data=enhanced_bytes,
                            file_name=f"enhanced_{entry['filename'].split('.')[0]}.{entry['output_format']}",
                            mime=f"image/{entry['output_format']}"
                        )
                    except Exception as e:
                        st.error("Error loading enhanced image")
                
                with col3:
                    st.markdown("**Enhancement Settings**")
                    st.markdown(f"**Category:** {entry['category']}")
                    st.markdown(f"**Shot Angle:** {entry['shot_angle']}")
                    st.markdown(f"**Background:** {entry['background']}")
                    st.markdown(f"**Aspect Ratio:** {entry['aspect_ratio']}")
                    st.markdown(f"**Format:** {entry['output_format']}")
                    
                    if entry['additional_instructions']:
                        st.markdown("**Additional Instructions:**")
                        st.text_area(
                            "Prompt used:",
                            value=entry['additional_instructions'],
                            height=100,
                            disabled=True,
                            key=f"history_prompt_{i}"
                        )
                    
                    if entry['custom_prompt']:
                        st.markdown("**Custom Prompt Used:**")
                        st.text_area(
                            "Custom prompt:",
                            value=entry['custom_prompt'],
                            height=150,
                            disabled=True,
                            key=f"history_custom_prompt_{i}"
                        )
                
                st.markdown("---")
        
        # Clear history button
        if st.button("🗑️ Clear All History", type="secondary"):
            st.session_state.image_history = []
            st.success("History cleared!")
            st.rerun()

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #666;">
        <p>Copyright @Bizzilo | Crafted with ❤️ in India</p>
    </div>
    """,
    unsafe_allow_html=True
)