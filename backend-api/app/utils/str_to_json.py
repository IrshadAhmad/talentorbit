import re
import json
from fastapi import HTTPException

def extract_json_from_string(response_str: str) -> dict:
    try:
        if response_str.strip().startswith(("{", "[")):
            return json.loads(response_str)
        
        json_match = re.search(r"({.*}|\[.*\])", response_str, re.DOTALL)
        if json_match:
            json_data = json_match.group(0)
            return json.loads(json_data)

        raise HTTPException(status_code=400, detail="Please provide the correct job description.")

    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Failed to parse JSON from the response string")