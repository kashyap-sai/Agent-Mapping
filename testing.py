from Agents.mapping_agent import AutoMappingAgent

# Define SchemaItem class
class SchemaItem:
    def __init__(self, column_name, data_type):
        self.column_name = column_name
        self.data_type = data_type

# Convert dictionary schemas to SchemaItem objects
source_schema = [
    SchemaItem("customer_id", "INTEGER"),
    SchemaItem("customer_name", "TEXT"),
    SchemaItem("customer_email", "TEXT")
]

target_schema = [
    SchemaItem("id", "INTEGER"),
    SchemaItem("name", "TEXT"),
    SchemaItem("email", "TEXT")
]

# Initialize and test AutoMappingAgent
agent = AutoMappingAgent()
mappings = agent.map_schemas(source_schema, target_schema)

print("Final Mappings:\n", mappings)

