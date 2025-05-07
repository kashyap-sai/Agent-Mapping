from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from Agents.mapping_agent import AutoMappingAgent

app = FastAPI()

class SchemaItem(BaseModel):
    column_name: str
    data_type: str

class MappingRequest(BaseModel):
    source_schema: list[SchemaItem]
    target_schema: list[SchemaItem]

class MappingResponse(BaseModel):
    source_column: str
    source_data_type: str
    target_column: str
    target_data_type: str
    confidence_score: float

class MappingResult(BaseModel):
    mappings: list[MappingResponse]

@app.post("/map-schema", response_model=MappingResult)
async def map_schema(request: MappingRequest):
    try:
        # Debug: Print input schemas
        print("Source Schema Received:", [item.model_dump() for item in request.source_schema])
        print("Target Schema Received:", [item.model_dump() for item in request.target_schema])

        agent = AutoMappingAgent()
        mappings = agent.map_schemas(request.source_schema, request.target_schema)
        return {"mappings": mappings}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
