from fastapi._compat import CoreSchema as CoreSchema, GetJsonSchemaHandler as GetJsonSchemaHandler, JsonSchemaValue as JsonSchemaValue, PYDANTIC_V2 as PYDANTIC_V2, with_info_plain_validator_function as with_info_plain_validator_function
from starlette.datastructures import UploadFile as StarletteUploadFile

class UploadFile(StarletteUploadFile): ...
