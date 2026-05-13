from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
from enum import Enum

class ComparisonStatus(str, Enum):
    MATCH = "MATCH"
    MISMATCH = "MISMATCH"
    ERROR = "ERROR"

class ComparisonType(str, Enum):
    SCHEMA = "schema"
    DIFF = "diff"
    
@dataclass
class ComparisonResult:
    """Represents the result of a single file comparison."""
    file_name: str
    comparison_type: ComparisonType
    status: ComparisonStatus
    details: Dict[str, Any] = field(default_factory=dict)

@dataclass
class GlobalReport:
    """The standardized packet/stream return structure for the entire comparison run."""
    status: str  # "SUCCESS" or "FAILURE"
    summary: str
    metrics: Dict[str, Any] = field(default_factory=lambda: {
        "files_compared": 0,
        "matches": 0,
        "failures": 0,
        "failure_rate": 0.0
    })
    results: List[ComparisonResult] = field(default_factory=list)

__all__ = [
    "ComparisonStatus",
    "ComparisonType",
    "ComparisonResult",
    "GlobalReport",
    "ComparisonEngineConfig",
]

@dataclass
class ComparisonEngineConfig:
    """Configuration parameters used by the comparison engine."""
    failure_threshold: float = 0.1
    schema_path: Optional[str] = None
    # Add other runtime parameters as needed (e.g., required fields, etc.)
