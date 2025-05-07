import ollama
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain.tools import Tool
from Memory.memory_manager import MemoryManager
from Tools.schema_tools import SchemaTools
from LLM.LLM_handler import LLMHandler
from Prompt_Template.prompts import _create_mapping_prompt

class AutoMappingAgent:
    def __init__(self):
        # Initialize LLM with Ollama's Mistral model
        self.llm_model_name = "mistral:latest"

        # Initialize tools
        self.memory = MemoryManager()
        self.schema_tools = SchemaTools()

        # Initialize LLM Handler
        self.llm_handler = LLMHandler(self.llm_model_name)

        # Initialize LangChain memory
        self.langchain_memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        # Define tools
        self.tools = [
            Tool(name="Schema_Validator", func=self.schema_tools.validate_schema_mapping, description="Validates schema mappings."),
        ]

        # Initialize the agent with tools
        self.mapping_agent = initialize_agent(
            tools=self.tools,
            llm=self.llm_handler,
            agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,  # Enable Few-Shot Learning
            verbose=True,
            memory=self.langchain_memory,
            handle_parsing_errors=True,
            max_iterations=3,  # Increased iterations for better accuracy
            early_stopping_method="generate"
        )
    
    def map_schemas(self, source_schema, target_schema):
        """
        Map columns from source schema to target schema using one LLM.
        
        Args:
            source_schema (list): List of source schema items.
            target_schema (list): List of target schema items.
        
        Returns:
            list: List of mapping results.
        """
        # Check for empty schemas early
        if not source_schema or not target_schema:
            print("Error: Empty schema provided!")
            return []
            
        # Prepare the prompt for schema mapping
        prompt = _create_mapping_prompt(source_schema, target_schema)
        print("Generated Prompt:\n", prompt)  # Debug: Print the prompt

        # Generate response from LLM
        llm_response = self.llm_handler._generate_response(prompt)
        print("LLM Response:\n", llm_response)  # Debug: Print LLM response
        
        if not llm_response:
            print("Error: No response from LLM")
            return []

        # Parse the final response into structured mappings
        mappings = self.schema_tools.parse_mappings(llm_response)
        print("Parsed Mappings:\n", mappings)  # Debug: Print the parsed mappings

        # Store mappings in memory
        self.memory.store_mappings(mappings)

        return mappings