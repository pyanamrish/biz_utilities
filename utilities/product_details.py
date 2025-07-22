from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from prompts.product_details_prompts import PRODUCT_DETAILS_PROMPT
from config.settings import OPENAI_API_KEY
import re

class ProductDetailsGenerator:
    def __init__(self):
        self.llm = ChatOpenAI(
            api_key=OPENAI_API_KEY,
            model_name="gpt-4-turbo-preview",
            temperature=0.7
        )
        self.chain = LLMChain(llm=self.llm, prompt=PRODUCT_DETAILS_PROMPT)
    
    def preview_prompt(self, product_name, keywords="", length="", breadth="", height="", weight=""):
        """Generate and return the formatted prompt without calling the LLM"""
        keywords = keywords if keywords else "Not specified"
        length = length if length else "Not specified"
        breadth = breadth if breadth else "Not specified"
        height = height if height else "Not specified"
        weight = weight if weight else "Not specified"
        
        return PRODUCT_DETAILS_PROMPT.format(
            product_name=product_name,
            keywords=keywords,
            length=length,
            breadth=breadth,
            height=height,
            weight=weight
        )
    
    def generate_content(self, product_name, keywords="", length="", breadth="", height="", weight="", custom_prompt=None):
        keywords = keywords if keywords else "Not specified"
        length = length if length else "Not specified"
        breadth = breadth if breadth else "Not specified"
        height = height if height else "Not specified"
        weight = weight if weight else "Not specified"
        
        if custom_prompt:
            # Use custom prompt if provided
            custom_template = PromptTemplate(
                input_variables=["product_name", "keywords", "length", "breadth", "height", "weight"],
                template=custom_prompt
            )
            custom_chain = LLMChain(llm=self.llm, prompt=custom_template)
            result = custom_chain.run(
                product_name=product_name,
                keywords=keywords,
                length=length,
                breadth=breadth,
                height=height,
                weight=weight
            )
        else:
            # Use default template
            result = self.chain.run(
                product_name=product_name,
                keywords=keywords,
                length=length,
                breadth=breadth,
                height=height,
                weight=weight
            )
        
        return self._parse_output(result)
    
    def _parse_output(self, output):
        sections = {
            'description': '',
            'features': '',
            'specifications': '',
            'meta_title': '',
            'meta_description': ''
        }
        
        # Parse Description
        description_match = re.search(r'DESCRIPTION:\s*\n(.*?)(?=FEATURES:|$)', output, re.DOTALL)
        if description_match:
            sections['description'] = description_match.group(1).strip()
        
        # Parse Features
        features_match = re.search(r'FEATURES:\s*\n(.*?)(?=SPECIFICATIONS:|$)', output, re.DOTALL)
        if features_match:
            sections['features'] = features_match.group(1).strip()
        
        # Parse Specifications
        spec_match = re.search(r'SPECIFICATIONS:\s*\n(.*?)(?=META TITLE:|$)', output, re.DOTALL)
        if spec_match:
            sections['specifications'] = spec_match.group(1).strip()
        
        # Parse Meta Title
        title_match = re.search(r'META TITLE:\s*\n(.*?)(?=META DESCRIPTION:|$)', output, re.DOTALL)
        if title_match:
            sections['meta_title'] = title_match.group(1).strip()
        
        # Parse Meta Description
        meta_desc_match = re.search(r'META DESCRIPTION:\s*\n(.*?)$', output, re.DOTALL)
        if meta_desc_match:
            sections['meta_description'] = meta_desc_match.group(1).strip()
        
        return sections