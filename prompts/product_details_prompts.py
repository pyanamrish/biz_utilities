from langchain.prompts import PromptTemplate

PRODUCT_DETAILS_PROMPT = PromptTemplate(
    input_variables=["product_name", "keywords", "length", "breadth", "height", "weight"],
    template="""You are an expert product copywriter and SEO specialist. Create compelling product content for the following:

Product Name: {product_name}
Keywords/Features: {keywords}
Dimensions: Length: {length} cm, Breadth: {breadth} cm, Height: {height} cm
Weight: {weight}

Please generate:

1. **Product Description**: Write an engaging, informative product overview that:
   - Provides a compelling introduction to the product
   - Highlights the main value proposition
   - Uses persuasive language that appeals to potential buyers
   - Is between 100-150 words

2. **Product Features**: List key features as bullet points that:
   - Highlight specific benefits and capabilities
   - Include relevant keywords naturally
   - Focus on what makes the product unique
   - Provide 4-6 key features

3. **Product Specifications**: Include technical details such as:
   - Exact dimensions (Length x Breadth x Height)
   - Weight
   - Materials used
   - Any relevant technical specifications
   - Other measurable attributes

4. **SEO Meta Title**: Create a compelling meta title that:
   - Must be under 80 characters
   - Includes the product name
   - Is optimized for search engines
   - Captures attention

5. **SEO Meta Description**: Write a meta description that:
   - Must be under 160 characters
   - Summarizes the product's main benefits
   - Includes a call to action
   - Is optimized for click-through rates

Format your response exactly as follows:

DESCRIPTION:
[Your product description here]

FEATURES:
• [Feature 1]
• [Feature 2]
• [Feature 3]
• [Feature 4]
• [Feature 5]
• [Feature 6]

SPECIFICATIONS:
• Dimensions: {length} cm × {breadth} cm × {height} cm
• Weight: {weight}
• [Additional specifications]

META TITLE:
[Your meta title here]

META DESCRIPTION:
[Your meta description here]
"""
)