IMAGE_ENHANCEMENT_PROMPT_TEMPLATE = """Enhance this product image while preserving the original product and maintaining its authentic appearance. Apply the following enhancements:

Shot Angle: Transform to {shot_angle} perspective while keeping the product recognizable
Background: Change background to {background} style while maintaining professional e-commerce quality
Product Category: This is a {category} product, enhance accordingly

Enhancement requirements:
- Keep the original product exactly as it is, only enhance and improve
- Apply professional lighting and composition improvements
- Ensure the background change complements the product
- Maintain high resolution and sharpness
- Optimize for e-commerce and marketing use
- Preserve all product details, colors, and textures

Additional specific instructions:
{additional_instructions}

Important: This is an image-to-image enhancement, not generation - preserve the original product while applying the specified improvements."""

SHOT_ANGLES = [
    "Front view",
    "Side view", 
    "Top-down view",
    "45-degree angle",
    "Close-up detail",
    "Lifestyle shot"
]

BACKGROUNDS = [
    "Pure white background",
    "Gradient background",
    "Natural environment",
    "Kitchen setting",
    "Office setting",
    "Outdoor setting",
    "Studio lighting setup",
    "Minimal aesthetic"
]

CATEGORIES = [
    "Kitchenware",
    "Cookware",
    "Fashion apparel",
    "Electronics",
    "Home decor",
    "Beauty products",
    "Sports equipment",
    "Office supplies"
]

ASPECT_RATIOS = [
    "1:1",
    "4:3", 
    "3:2",
    "16:9",
    "21:9",
    "2:3",
    "3:4",
    "9:16",
    "9:21"
]

OUTPUT_FORMATS = [
    "jpeg",
    "png"
]