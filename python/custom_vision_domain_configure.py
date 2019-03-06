import json

domain_json = {
  "type": "object",
  "properties": {
    "id": {
      "format": "uuid",
      "type": "string",
      "readOnly": True,
      "x-nullable": False
    },
    "name": {
      "type": "string",
      "readOnly": True,
      "x-nullable": True
    },
    "type": {
      "enum": [
        "Classification",
        "ObjectDetection"
      ],
      "type": "string",
      "readOnly": True,
      "x-nullable": False,
      "x-ms-enum": {
        "name": "DomainType",
        "modelAsString": True
      }
    },
    "exportable": {
      "type": "boolean",
      "readOnly": True,
      "x-nullable": False
    },
    "enabled": {
      "type": "boolean",
      "readOnly": True,
      "x-nullable": False
    }
  },
  "x-nullable": True
}

domain_configure = json.dumps(domain_json)