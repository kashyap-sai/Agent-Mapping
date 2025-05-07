class MemoryManager:
    def __init__(self):
        self.short_term_memory = []
        self.long_term_memory = []

    def store_mappings(self, mappings):
        """
        Store mappings in memory.
        
        Args:
            mappings (list): List of mapping results.
        """
        self.short_term_memory.extend(mappings)
        self.long_term_memory.extend(mappings)

    def retrieve_mappings(self):
        """
        Retrieve mappings from memory.
        
        Returns:
            list: List of mapping results.
        """
        return self.short_term_memory + self.long_term_memory