FunctionForSubject = [
    {
        "name": "getSubjectInformation",
        "description": "Get the all subject from the input .the input may be contain an arrays . you need to split it .",
        "parameters": {
            "type": "object",
            "properties": {
                "Subjects": {
                    "type": "array",
                    "description": "List of subjects to be returned.",
                    "items": {
                        "type": "string"
                    }
                }
            },
            "required": ["Subjects"]
        }
    }
]
