from typing import Dict, Any
from src.xml_compare_core.models import ComparisonType, ComparisonEngineConfig, GlobalReport
from src.xml_schema_validator.validator import XMLSchemaValidator
from src.xml_diff_manager.manager import DirectoryManager
from .models import ComparisonEngineConfig, ComparisonType, GlobalReport

def run_xml_comparison(
    comparison_type: ComparisonType, 
    config: ComparisonEngineConfig, 
    **kwargs: Any
) -> GlobalReport:
    """
    Primary entry point for all XML comparison tasks.
    Orchestrates the appropriate comparison method based on the required type.
    """
    print(f"Starting comparison run for type: {comparison_type.value}")
    
    if comparison_type == ComparisonType.SCHEMA:
        # 1. Schema Validation Path
        if not config.schema_path:
             raise ValueError("Schema comparison requires a valid XSD path.")
             
        validator = XMLSchemaValidator(config.schema_path)
        xml_path = kwargs.get('xml_path')
        if not xml_path:
             raise ValueError("Schema comparison requires a path to the XML file.")
             
        return process_schema_comparison(validator, xml_path)
    
    elif comparison_type == ComparisonType.DIFF:
        # 2. Directory Diff Path
        output_dir = kwargs.get('output_dir')
        input_dir = kwargs.get('input_dir')
        
        if not output_dir or not input_dir:
            raise ValueError("Directory comparison requires both 'output_dir' and 'input_dir'.")
            
        manager = DirectoryManager(
            output_dir=output_dir, 
            input_dir=input_dir, 
            failure_threshold=config.failure_threshold
        )
        return manager.compare()
        
    else:
        raise ValueError(f"Unknown comparison type specified: {comparison_type}")

def process_schema_comparison(validator: XMLSchemaValidator, xml_path: str) -> GlobalReport:
    """Handles the flow and result transformation for schema validation."""
    is_valid, error_message = validator.validate(xml_path)
    
    status = "SUCCESS" if is_valid else "FAILURE"
    
    result = ComparisonResult(
        file_name=xml_path,
        comparison_type=ComparisonType.SCHEMA,
        status=ComparisonStatus.MATCH if is_valid else ComparisonStatus.ERROR,
        details={"error_message": error_message} if not is_valid else {"message": "XML passed schema validation."}
    )
    
    return GlobalReport(
        status=status,
        summary=f"Schema comparison for {os.path.basename(xml_path)} completed. Status: {status}",
        metrics={"files_compared": 1, "matches": 1 if is_valid else 0, "failures": 1 - (1 if is_valid else 0), "failure_rate": 0.0},
        results=[result]
    )
