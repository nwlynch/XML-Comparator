#!/usr/bin/env python
"""
CLI tool for XML file comparison.
Supports both schema validation and directory diff modes.
"""

import argparse
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

from xml_compare_core import run_xml_comparison, ComparisonType, ComparisonEngineConfig


def format_report(report):
    """Format the comparison report for display."""
    print(f"Status: {report.status}")
    print(f"Summary: {report.summary}")
    print(f"\nMetrics:")
    print(f"  Files compared: {report.metrics['files_compared']}")
    print(f"  Matches: {report.metrics['matches']}")
    print(f"  Failures: {report.metrics['failures']}")
    print(f"  Failure rate: {report.metrics['failure_rate']:.2%}")
    
    if report.results:
        print(f"\nDetailed Results:")
        for i, result in enumerate(report.results, 1):
            status_icon = "✓" if result.status == "MATCH" else "✗" if result.status == "ERROR" else "⚠"
            print(f"\n{status_icon} File {i}: {result.file_name}")
            print(f"  Type: {result.comparison_type.value}")
            print(f"  Status: {result.status}")
            print(f"  Details: {result.details}")


def main():
    parser = argparse.ArgumentParser(
        description="XML Comparison Tool - Compare XML files using schema validation or directory diff",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s schema --xsd schema.xsd --xml-path input.xml
  %(prog)s diff --input-dir ./baseline --output-dir ./generated --failure-threshold 0.1
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Comparison mode")
    
    # Schema validation command
    schema_parser = subparsers.add_parser("schema", help="Validate XML against XSD schema")
    schema_parser.add_argument(
        "--xsd", 
        required=True,
        help="Path to the XSD schema file"
    )
    schema_parser.add_argument(
        "--xml-path",
        required=True,
        help="Path to the XML file to validate"
    )
    
    # Directory diff command
    diff_parser = subparsers.add_parser("diff", help="Compare XML files in two directories")
    diff_parser.add_argument(
        "--input-dir",
        required=True,
        help="Directory containing baseline XML files"
    )
    diff_parser.add_argument(
        "--output-dir",
        required=True,
        help="Directory containing XML files to compare against baseline"
    )
    diff_parser.add_argument(
        "--failure-threshold",
        type=float,
        default=0.1,
        help="Maximum failure rate allowed (default: 0.1)"
    )
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Create config with appropriate options
    config = ComparisonEngineConfig(
        schema_path=args.xsd if args.command == "schema" else None,
        failure_threshold=getattr(args, 'failure_threshold', 0.1)
    )
    
    # Build kwargs for run_xml_comparison
    kwargs = {
        "input_dir": getattr(args, 'input_dir', None),
        "output_dir": getattr(args, 'output_dir', None),
    }
    
    if args.command == "schema":
        kwargs["xml_path"] = args.xml_path
    
    # Run comparison
    print(f"\n🔍 Starting XML comparison ({args.command} mode)...")
    print("=" * 50)
    
    try:
        report = run_xml_comparison(
            comparison_type=ComparisonType.SCHEMA if args.command == "schema" else ComparisonType.DIFF,
            config=config,
            **kwargs
        )
        format_report(report)
        
    except ValueError as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
