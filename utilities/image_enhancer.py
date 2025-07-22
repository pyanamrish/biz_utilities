import fal_client
from config.settings import FAL_KEY
from prompts.image_enhancer_prompts import IMAGE_ENHANCEMENT_PROMPT_TEMPLATE
import base64
from PIL import Image
import io

class ImageEnhancer:
    def __init__(self):
        fal_client.api_key = FAL_KEY
        self.model = "fal-ai/flux-pro/kontext"  # Using Flux Pro Kontext for image-to-image enhancement
    
    def preview_prompt(self, shot_angle, background, category, additional_instructions=""):
        """Generate and return the formatted prompt without calling the API"""
        return IMAGE_ENHANCEMENT_PROMPT_TEMPLATE.format(
            shot_angle=shot_angle,
            background=background,
            category=category,
            additional_instructions=additional_instructions
        )
        
    def enhance_image(self, image_bytes, shot_angle, background, category, aspect_ratio, output_format, additional_instructions="", custom_prompt=None):
        if custom_prompt:
            prompt = custom_prompt
        else:
            prompt = IMAGE_ENHANCEMENT_PROMPT_TEMPLATE.format(
                shot_angle=shot_angle,
                background=background,
                category=category,
                additional_instructions=additional_instructions
            )
        
        # Convert image to base64
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
        
        try:
            result = fal_client.run(
                self.model,
                arguments={
                    "prompt": prompt,
                    "image_url": f"data:image/png;base64,{image_base64}",
                    "guidance_scale": 3.5,
                    "num_inference_steps": 28,
                    "num_images": 1,
                    "output_format": output_format,
                    "aspect_ratio": aspect_ratio,
                    "safety_tolerance": "2"
                }
            )
            
            if result and 'images' in result and len(result['images']) > 0:
                return result['images'][0]
            else:
                raise Exception("No image generated")
                
        except Exception as e:
            raise Exception(f"Image enhancement failed: {str(e)}")
    
