# XML Comparator

A robust, modular Python application for comparing XML files across multiple validation types: Schema Validation and Content Difference Detection.

## ✨ Features
*   **Schema Validation:** Compares an XML document against a predefined XSD schema, providing detailed feedback on structural or type mismatches.
*   **Directory Comparison (Diffing):** Compares files between a baseline (`input`) and a target (`output`) directory pair.
*   **Intelligent Engine:** Automatically selects the best comparison engine (in-memory vs. streaming) based on file size and complexity to ensure performance and prevent memory exhaustion.
*   **Standardized Output:** All comparisons return a single, consistent JSON/Python data structure (`GlobalReport`) suitable for immediate consumption by Web UIs or API endpoints.
## 📐 Architecture
The tool is built on a highly modular Python library (`xml_compare_core`) to ensure maximum reusability and maintainability, decoupling the core comparison logic from the user interface (CLI, API, Web).

**Core Modules:**
1.  **`xml_schema_validator`**: Handles the parsing and validation logic against XSDs.
2.  **`xml_diff_manager`**: Contains the orchestration logic for directory comparison and the file size/complexity analysis.
3.  **`xml_compare_core`**: The main dispatcher that routes the request to the correct, specialized module.

## 🚀 Getting Started

### Prerequisites
You must have Python 3.8+ installed. The following dependencies are required:
*   `lxml`: For robust XML parsing and XSD validation.
*   `pytest`: For running the included test suite.

Install dependencies using:
```bash
pip install -r requirements.txt
```

### Usage
The application is intended to be run via a wrapper script or directly imported into a larger service.

**1. Schema Validation Example:**
To validate a file `my_schema.xsd` against a target file `test_file.xml`:
```bash
python -m xml_compare_core.core run_comparison --type schema \
    --xsd_path /path/to/my_schema.xsd \
    --xml_path /path/to/test_file.xml
```

**2. Directory Diff Example:**
To compare files in the `output` directory against the baseline in the `input` directory:
```bash
python -m xml_compare_core.core run_comparison --type diff \
    --output_dir ./test_fixtures/test_out \
    --input_dir ./test_fixtures/test_in \
    --failure_threshold 0.2 
```

## 🧪 Running Tests
To run the integrated test suite, ensure you are in the project root and execute:
```bash
pytest tests/test_comparison.py
```

## 🏗️ Development & Contribution
This project is managed by the QMS team. All contributions must follow the architectural standards defined in `BLUEPRINT.md`. Please ensure all new features are first scoped via the `brainstorming` skill.

