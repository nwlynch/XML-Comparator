# XML Comparison Tool: Architectural Blueprint

## 🎯 Goal
To create a modular, idempotent Python library (`xml_compare_core`) that provides a unified, reliable backend for comparing XML files, usable by CLI, Web UI, and API services.

## 🏗️ Proposed Architecture (Modular Approach)

The system is divided into three core, decoupled modules:

1.  **`xml_compare_core` (The Library):** The central, abstract logic hub. It defines the comparison abstract base classes and determines the optimal comparison engine based on initial file analysis. **All other components use this module.**
2.  **`xml_schema_validator`:** Handles comparison mode (A). It ingests an XSD, performs validation, and must support failure reporting down to the node level.
3.  **`xml_diff_manager`:** Handles comparison mode (B). It manages the directory pair comparison, orchestrating the intelligent file comparison.

## ⚙️ Core Mechanism: File Analysis & Engine Selection
The first step in `xml_diff_manager` is a **FileAnalyzer** component.
*   **Small/Simple Files:** Load entire XML into memory (fast, real-time comparison).
*   **Large/Complex Files:** Invoke a streaming/iterator-based comparison engine to prevent OutOfMemory errors (batch processing).

## 🔄 Data Flow & API Contract
The entire process must output a standardized Python data structure (which maps directly to a JSON API response) to ensure consumption by the Web UI:

```python
{
    "status": "SUCCESS" | "FAILURE",
    "summary": "Comparison finished successfully.",
    "metrics": {
        "files_compared": 5,
        "matches": 4,
        "failures": 1,
        "failure_rate": 0.2
    },
    "results": [
        {
            "file_name": "file_x.xml",
            "comparison_type": "schema" | "diff",
            "status": "MATCH" | "MISMATCH",
            "details": {
                "schema_error": "Description of failed element",
                "mismatch_location": "XPath/Node Path",
                "contents": {
                    "baseline": "...",
                    "output": "..."
                }
            }
        },
        // ... list of results
    ]
}
```

## 📚 Requirements Summary (Checklist)
*   [x] **Idempotency:** The tool must always yield the same result for the same input.
*   [x] **Schema Handling:** XSD must be provided at runtime.
*   [x] **Failure Control:** Must support a configurable failure percentage threshold.
*   [x] **Module Boundaries:** Core logic must be in `xml_compare_core` for maximum reusability across web/CLI backends.

This blueprint provides a robust, modular starting point suitable for building a reliable and scalable production system.