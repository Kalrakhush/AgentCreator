import yaml
from custom_logging import setup_logger

logger = setup_logger(__name__)

class APIDocParser:
    """
    A class responsible for parsing and validating API documentation.
    This class automatically handles discrepancies like missing fields or malformed data.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.api_doc = None

    def load_and_parse(self) -> dict:
        try:
            with open(self.file_path, 'r') as file:
                self.api_doc = yaml.safe_load(file)
            logger.info("API documentation loaded successfully.")
        except yaml.YAMLError as e:
            logger.error("YAML parsing error: %s", e)
            raise
        except Exception as e:
            logger.error("Error loading API documentation: %s", e)
            raise
        
        return self.api_doc

    def validate(self):
        """
        Validates and automatically corrects common issues in the API documentation.
        """
        if not isinstance(self.api_doc, dict):
            logger.error("Invalid API documentation format. Expected a dictionary.")
            raise ValueError("API documentation must be a dictionary.")
        
        if "endpoints" not in self.api_doc:
            logger.warning("Missing 'endpoints' section in API documentation. Adding default structure.")
            self.api_doc["endpoints"] = []

        for endpoint in self.api_doc["endpoints"]:
            if "method" not in endpoint:
                logger.warning("Missing 'method' in endpoint. Setting to 'GET' as default.")
                endpoint["method"] = "GET"
            if "url" not in endpoint:
                logger.error("Missing 'url' in endpoint.")
                raise ValueError("Each endpoint must have a 'url'.")

    def get_parsed_doc(self) -> dict:
        if not self.api_doc:
            self.load_and_parse()
        self.validate()
        return self.api_doc
