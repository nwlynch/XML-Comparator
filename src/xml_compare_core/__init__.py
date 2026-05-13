# This file makes the xml_compare_core directory a Python package.
from .models import (
    ComparisonType,  # noqa: F401
    ComparisonEngineConfig,  # noqa: F401
    GlobalReport,  # noqa: F401
    ComparisonResult,  # noqa: F401
    ComparisonStatus,  # noqa: F401
)
from xml_schema_validator.validator import XMLSchemaValidator as _XMLSchemaValidator
from xml_diff_manager.manager import DirectoryManager as _DirectoryManager
from .core import run_xml_comparison as _run_xml_comparison

__all__ = [
    "ComparisonType",
    "ComparisonEngineConfig",
    "GlobalReport",
    "ComparisonResult",
    "ComparisonStatus",
    "XMLSchemaValidator",
    "DirectoryManager",
    "run_xml_comparison",
]

XMLSchemaValidator = _XMLSchemaValidator
DirectoryManager = _DirectoryManager
run_xml_comparison = _run_xml_comparison