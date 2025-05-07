def _create_mapping_prompt(source_schema, target_schema):
    """
    Generate a prompt with few-shot examples to improve mapping accuracy.
    """
    try:
        # Convert lists to strings to avoid KeyError issues
        formatted_source = ", ".join(source_schema) if isinstance(source_schema, list) else str(source_schema)
        formatted_target = ", ".join(target_schema) if isinstance(target_schema, list) else str(target_schema)

        example_mappings = f"""
        Example 1:
        Source Schema: ["customer_name", "customer_id", "email"]
        Target Schema: ["name", "id", "contact_email"]
        Mapping Output: {{"customer_name": "name", "customer_id": "id", "email": "contact_email"}}

        Example 2:
        Source Schema: ["order_date", "order_amount", "product_id"]
        Target Schema: ["date", "amount", "item_id"]
        Mapping Output: {{"order_date": "date", "order_amount": "amount", "product_id": "item_id"}}

        Now, given the following schemas, generate the best possible mapping:
        Source Schema: [{formatted_source}]
        Target Schema: [{formatted_target}]
        Mapping Output:
        """
        
        return example_mappings
    except Exception as e:
        print(f"Error in _create_mapping_prompt: {e}")
        return "Error: Invalid schema format."
