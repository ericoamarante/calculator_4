from typing import Dict, List
from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4:
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        media = self.__calculate_media(input_data)
        response = self.__format_response(media)
        return response
    
    def __validate_body(self, body:Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Body mal formatado!")
        
        input_data = body["numbers"]
        return input_data
    
    def __calculate_media(self, input_data: List[float]) -> float:
        media = sum(input_data) / len(input_data)
        return media
    
    def __format_response(self, media: float) -> Dict:
        return {"data": {"Calculator": 4, "result": media, "Success": True}}
