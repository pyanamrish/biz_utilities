IMAGE_ENHANCEMENT_PROMPT_TEMPLATE = """Enhance this product image while preserving the original product and maintaining its authentic appearance. Apply the following enhancements:

Shot Angle: Transform to {shot_angle} perspective while keeping the product recognizable
Background: Change background to {background} style while maintaining professional e-commerce quality
Product Category: This is a {category} product, enhance accordingly

Enhancement requirements:
- Keep the original product exactly as it is with same aspect ratio and shape, only enhance and improve
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

# Category-specific prompt suggestions
CATEGORY_SUGGESTIONS = {
    "Fashion apparel": [
        "Place this dress on a 6 year old kid playing happily in a lawn. The girl should be standing, smiling, and looking at the camera. She should look natural, around 6 years old, with soft lighting. The background should be clean, studio-style or outdoors with a soft blur. The dress must fit naturally with realistic folds, shadows, and proportions. Ensure the pose makes the dress clearly visible",
        "Show this fashion item on a professional model in a studio setting with dramatic lighting. The model should be posing elegantly against a neutral background with perfect styling and makeup",
        "Display this clothing item in a lifestyle setting - someone wearing it casually in an urban environment, natural lighting, authentic everyday moment"
    ],
    "Kitchenware": [
        "Place this kitchen item in a modern, well-lit kitchen setting with marble countertops and natural lighting. Show the product being used in a realistic cooking scenario with complementary ingredients or tools nearby",
        "Create a professional product photography setup with clean white background, perfect lighting, and subtle shadows that highlight the product's features and quality",
        "Show this kitchenware item in an elegant dining setup with beautiful table settings, fine dinnerware, and warm ambient lighting"
    ],
    "Cookware": [
        "Display this cookware on a stovetop with steam or cooking action, showing the product in actual use with delicious food being prepared inside",
        "Create a professional chef's kitchen setting with stainless steel surfaces, proper lighting, and other professional kitchen tools to emphasize quality",
        "Show this cookware in a cozy home kitchen with warm lighting, wooden cutting boards, and fresh ingredients around it"
    ],
    "Electronics": [
        "Show this electronic device in a modern office or home workspace setting with clean lines, contemporary furniture, and professional lighting that highlights the product's sleek design",
        "Create a tech lifestyle shot showing the product being used by someone in a realistic setting, emphasizing its functionality and user experience",
        "Display this device with perfect studio lighting against a gradient background that complements the product's color scheme and design"
    ],
    "Home decor": [
        "Place this home decor item in a beautifully styled interior space with complementary furniture, perfect lighting, and a cohesive design aesthetic that showcases how it fits into a real home",
        "Create an aspirational lifestyle shot showing this item in a luxury home setting with high-end furnishings and architectural details",
        "Show this decor piece in a cozy, lived-in space that feels authentic and relatable while still being visually appealing"
    ],
    "Beauty products": [
        "Display this beauty product in an elegant vanity or bathroom setting with soft, flattering lighting, marble surfaces, and other luxury beauty items for context",
        "Create a spa-like atmosphere with natural elements, soft textures, and serene lighting that emphasizes the product's premium quality and relaxing benefits",
        "Show this beauty item being used by a person with glowing, healthy skin in natural lighting that highlights the product's effectiveness"
    ],
    "Sports equipment": [
        "Show this sports equipment in action - being used by an athlete in the appropriate sports setting with dynamic lighting and movement that demonstrates its performance",
        "Create a professional gym or sports facility setting with proper equipment and lighting that emphasizes the product's quality and intended use",
        "Display this item in an outdoor sports environment with natural lighting and terrain that matches the product's intended activity"
    ],
    "Office supplies": [
        "Place this office item in a clean, modern workspace with professional lighting, organized desk setup, and contemporary office furniture that creates a productive atmosphere",
        "Show this product in use within a realistic office environment with papers, computer, and other office supplies that demonstrate its practical application",
        "Create a minimalist desktop scene with perfect organization and lighting that highlights the product's design and functionality"
    ]
}