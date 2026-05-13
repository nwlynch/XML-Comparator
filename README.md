# XML Comparator

A Python library for comparing XML files using schema validation or directory diff operations.

## Features

- **Schema Validation**: Validate XML files against XSD schemas with detailed error reporting
- **Directory Diff**: Compare XML files across two directories (baseline vs output)
- **Modular Architecture**: Clean separation of concerns with reusable components
- **Production-Ready**: Modern Python 3.12+ patterns, comprehensive error handling
- **CLI Tool**: Ready-to-use command-line interface for common use cases

## Installation

```bash
# Clone and install
cd /path/to/xml-comparator
pip install -e .
```

## Quick Start

### Schema Validation Mode

Validate a single XML file against an XSD schema:

```bash
python compare_xml_cli.py schema \
    --xsd schema.xsd \
    --xml-path input.xml
```

### Directory Diff Mode

Compare XML files between two directories:

```bash
python compare_xml_cli.py diff \
    --input-dir ./baseline \
    --output-dir ./generated
```

## Usage Examples

### Validate XML against schema

```bash
python compare_xml_cli.py schema --xsd items.xsd --xml-path document.xml
```

### Compare entire directories

```bash
python compare_xml_cli.py diff --input-dir ./input --output-dir ./output --failure-threshold 0.1
```

### Using the API directly

```python
from xml_compare_core import run_xml_comparison, ComparisonType, ComparisonEngineConfig

# Schema validation
config = ComparisonEngineConfig(schema_path="schema.xsd")
report = run_xml_comparison(
    comparison_type=ComparisonType.SCHEMA,
    config=config,
    xml_path="document.xml"
)

# Directory diff
config = ComparisonEngineConfig()
report = run_xml_comparison(
    comparison_type=ComparisonType.DIFF,
    config=config,
    input_dir="./baseline",
    output_dir="./output"
)
```

## Project Structure

```
xml-comparator/
├── compare_xml_cli.py      # CLI entry point
├── items.xsd               # Sample XSD schema
├── input/                  # Input XML files (for testing)
│   ├── valid.xml
│   └── invalid_element.xml
├── output/                 # Output XML files (for testing)
├── src/
│   ├── xml_compare_core/
│   │   ├── __init__.py
│   │   ├── core.py
│   │   └── models.py
│   ├── xml_diff_manager/
│   │   ├── __init__.py
│   │   ├── manager.py
│   │   └── validator.py
│   └── xml_schema_validator/
│       ├── __init__.py
│       └── validator.py
├── tests/                  # Test fixtures
├── setup.py
├── requirements.txt
└── README.md
```

## Supported Operations

| Operation | Description | Command |
|-----------|-------------|---------|
| Schema Validation | Verify XML conforms to XSD schema | `compare_xml_cli.py schema --xsd schema.xsd --xml-path file.xml` |
| Directory Diff | Compare two directories of XML files | `compare_xml_cli.py diff --input-dir ./input --output-dir ./output` |
| Custom Threshold | Set maximum allowed failure rate | Add `--failure-threshold 0.1` |

## Error Handling

The tool provides detailed error messages including:
- Schema validation errors with line numbers
- Missing files and directories
- Custom failure rate thresholds

## Dependencies

- `lxml>=4.9.0` - XML parsing and schema validation
- `pytest>=7.0.0` - Testing framework
- `setuptools>=60.0.0` - Package management

## License

MIT License - See LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

