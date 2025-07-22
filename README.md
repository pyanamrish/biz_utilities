# Business Utilities

A Streamlit application that provides AI-powered business utilities for e-commerce and marketing teams.

## Features

### 1. Product Details Generator
- Generate compelling product descriptions
- Create SEO-optimized meta titles (< 80 chars)
- Create SEO-optimized meta descriptions (< 160 chars)
- Rich text display with copy-to-clipboard functionality
- Powered by OpenAI GPT-4

### 2. Product Image Enhancer
- Transform product images with AI
- Customizable shot angles and backgrounds
- Multiple aspect ratio support
- Download in multiple formats (PNG, JPG, WebP)
- Powered by Fal.ai Flux models

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd biz_utilities
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
```

Edit `.env` and add your API keys:
- `OPENAI_API_KEY`: Your OpenAI API key
- `FAL_KEY`: Your Fal.ai API key

## Running Locally

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## Deployment on Streamlit Cloud

1. Push your code to GitHub

2. Go to [share.streamlit.io](https://share.streamlit.io)

3. Deploy your app:
   - Select your repository
   - Set the main file path to `app.py`
   - Add your secrets in the Streamlit Cloud dashboard:
     ```toml
     OPENAI_API_KEY = "your-openai-key"
     FAL_KEY = "your-fal-key"
     ```

## Project Structure

```
biz_utilities/
├── app.py                  # Main Streamlit application
├── utilities/             # Core utility modules
│   ├── product_details.py # Product content generator
│   └── image_enhancer.py  # Image enhancement module
├── prompts/              # Prompt templates
├── utils/                # Helper utilities
├── config/               # Configuration and settings
└── requirements.txt      # Python dependencies
```

## Adding New Utilities

To add a new utility:

1. Create a new module in `utilities/`
2. Add prompt templates in `prompts/`
3. Update the utility selection in `app.py`
4. Add any new dependencies to `requirements.txt`

## Requirements

- Python 3.8+
- Streamlit account (for deployment)
- OpenAI API key
- Fal.ai API key

## License

This project is licensed under the MIT License.