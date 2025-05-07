import json
import re

class SchemaTools:
    def parse_mappings(self, llm_response):
        try:
            # Extract JSON from response using regex
            json_str = re.search(r'\{.*\}', llm_response, re.DOTALL).group()
            print("Extracted JSON:", json_str)  # Debug
            mappings = json.loads(json_str)["mappings"]
            return mappings
        except Exception as e:
            print(f"Error parsing mappings: {str(e)}")
            return []

    def validate_schema_mapping(self, mapping):
        if not mapping:
            return "Invalid mapping: Empty input."
        return "Schema mapping is valid."
