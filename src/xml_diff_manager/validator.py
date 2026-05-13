from typing import Tuple, Optional
from lxml import etree

__all__ = ["XMLSchemaValidator"]

class XMLSchemaValidator:
    """
    Handles validation of XML files against a provided XSD schema.
    This is the base validator class used across multiple modules.
    """
    def __init__(self, xsd_path: str):
        """
        Initializes the validator by loading and compiling the XSD schema.
        """
        try:
            xmlschema_doc = etree.parse(xsd_path)
            self.schema = etree.XMLSchema(xmlschema_doc)
            print("Schema Validator initialized successfully.")
        except etree.XMLSchemaParseError as e:
            raise ValueError(f"Failed to parse XSD schema: {e}")

    def validate(self, xml_path: str) -> Tuple[bool, Optional[str]]:
        """
        Validates an XML file against the loaded schema.
        Returns (True, None) on success, or (False, error_message) on failure.
        """
        try:
            xml_doc = etree.parse(xml_path)
            if self.schema.validate(xml_doc):
                return (True, None)
            else:
                # Returns the most relevant error message from the schema validation
                error_list = self.schema.error_log
                # Get error message from lxml 5.x+ error_log or older error_log.error
                error = error_list.last_error if hasattr(error_list, 'last_error') else getattr(error_list, 'error', None)
                return (False, str(error) if error else "Schema validation failed")
        except etree.XMLSyntaxError as e:
            return (False, f"XML Syntax Error: {e}")
        except FileNotFoundError:
            return (False, "XML file not found.")
