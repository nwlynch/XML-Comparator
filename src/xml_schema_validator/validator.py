from typing import Tuple, Optional
from lxml import etree

class XMLSchemaValidator:
    """
    Handles validation of XML files against a provided XSD schema.
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
                error_log = self.schema.error_log
                return (False, str(error_log.error[0] if error_log.error else "Unknown validation error"))
        except etree.XMLSyntaxError as e:
            return (False, f"XML Syntax Error: {e}")
        except FileNotFoundError:
            return (False, "XML file not found.")

# Placeholder for future functionality:
# class XMLContentComparer:
#     ...
