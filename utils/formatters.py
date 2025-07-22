import streamlit as st
import streamlit.components.v1 as components

def display_product_content(content):
    # Product Description Section
    col1, col2 = st.columns([10, 1])
    with col1:
        st.markdown("### 📝 Product Description")
    with col2:
        _create_copy_button("description", content.get('description', ''), "desc")
    
    st.markdown(
        f"""
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
            <p style="line-height: 1.6;">{content.get('description', 'No description generated')}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Features Section
    if content.get('features'):
        col1, col2 = st.columns([10, 1])
        with col1:
            st.markdown("### ✨ Product Features")
        with col2:
            _create_copy_button("features", content.get('features', ''), "feat")
        
        st.markdown(
            f"""
            <div style="background-color: #e8f5e8; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
                <div style="line-height: 1.8;">{content['features'].replace('• ', '✓ ')}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Specifications Section
    if content.get('specifications'):
        col1, col2 = st.columns([10, 1])
        with col1:
            st.markdown("### 📏 Product Specifications")
        with col2:
            _create_copy_button("specifications", content.get('specifications', ''), "spec")
        
        st.markdown(
            f"""
            <div style="background-color: #fff3e0; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
                <div style="line-height: 1.8;">{content['specifications']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # SEO Meta Information
    col1, col2 = st.columns(2)
    
    with col1:
        col1_1, col1_2 = st.columns([8, 1])
        with col1_1:
            st.markdown("### 🏷️ Meta Title")
        with col1_2:
            _create_copy_button("meta_title", content.get('meta_title', ''), "title")
        
        st.markdown(f"**{content.get('meta_title', 'No title generated')}**")
        st.caption(f"Character count: {len(content.get('meta_title', ''))}/80")
        
    with col2:
        col2_1, col2_2 = st.columns([8, 1])
        with col2_1:
            st.markdown("### 📋 Meta Description")
        with col2_2:
            _create_copy_button("meta_description", content.get('meta_description', ''), "desc_meta")
        
        st.markdown(f"*{content.get('meta_description', 'No description generated')}*")
        st.caption(f"Character count: {len(content.get('meta_description', ''))}/160")
    
    # Copy All Content functionality
    full_content = f"""Product Description:
{content.get('description', '')}

Product Features:
{content.get('features', '')}

Product Specifications:
{content.get('specifications', '')}

Meta Title:
{content.get('meta_title', '')}

Meta Description:
{content.get('meta_description', '')}"""
    
    st.markdown("---")
    st.markdown("### 📋 Copy All Content")
    
    # Display content in a text area for easy copying
    st.text_area(
        "Select all text below and copy (Ctrl+C / Cmd+C):",
        value=full_content,
        height=200,
        help="Click inside the text area, press Ctrl+A (or Cmd+A on Mac) to select all, then Ctrl+C (or Cmd+C) to copy"
    )
    
    # Alternative: Add a copy button with JavaScript
    escaped_content = full_content.replace('`', '\\`').replace('\n', '\\n').replace('\r', '\\r')
    copy_button_html = f"""
    <button onclick="copyAllToClipboard()" style="
        background-color: #FF6B6B;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
    ">📋 Copy All Content</button>
    
    <script>
    function copyAllToClipboard() {{
        const text = `{escaped_content}`;
        navigator.clipboard.writeText(text).then(function() {{
            alert('All content copied to clipboard!');
        }}, function(err) {{
            console.error('Could not copy text: ', err);
        }});
    }}
    </script>
    """
    components.html(copy_button_html, height=70)

def _create_copy_button(section_name, content, button_id):
    """Create a small copy button for individual sections"""
    if not content:
        return
        
    escaped_content = content.replace('`', '\\`').replace('\n', '\\n').replace('\r', '\\r')
    copy_button_html = f"""
    <button onclick="copy{button_id}()" style="
        background-color: transparent;
        border: 1px solid #ccc;
        padding: 5px 8px;
        border-radius: 3px;
        cursor: pointer;
        font-size: 12px;
        color: #666;
    " title="Copy {section_name}">📋</button>
    
    <script>
    function copy{button_id}() {{
        const text = `{escaped_content}`;
        navigator.clipboard.writeText(text).then(function() {{
            alert('{section_name.replace("_", " ").title()} copied to clipboard!');
        }}, function(err) {{
            console.error('Could not copy text: ', err);
        }});
    }}
    </script>
    """
    components.html(copy_button_html, height=40)
    
def format_error_message(error):
    return f"""
    <div style="background-color: #ffebee; border-left: 4px solid #f44336; padding: 10px; margin: 10px 0;">
        <strong style="color: #c62828;">Error:</strong> {error}
    </div>
    """