#!/usr/bin/env python3
import argparse
import json
import os
import sys
import textwrap
import yaml


def parse_args() -> argparse.Namespace:
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="Validate submitted results")
    parser.add_argument(
        "--config", help="Specify YAML file containing results config", required=True
    )
    parser.add_argument(
        "--correct", help="JSON string containing correct results", required=True
    )
    parser.add_argument(
        "--output",
        help="Write validation results in HTML to specified file",
        required=True,
    )
    parser.add_argument(
        "--output-yaml", help="Write validation results in YAML to specified file"
    )
    return parser.parse_args()


def load_config(filename: str) -> dict:
    with open(filename, "r") as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)
    return config


def check_submitted_results_are_valid(filename: str, output_file: str) -> bool:
    if not os.path.isfile(filename):
        validation_output = f"<h1>❌ Results Validation</h1> ❌ Your code did not produce a <code>{filename}</code> file, which is required for grading. Please review the README and update your code."
    else:
        with open(filename, "r") as f:
            try:
                yaml.load(f, Loader=yaml.SafeLoader)
                validation_output = ""
            except yaml.constructor.ConstructorError as e:
                if (
                    "tag:yaml.org,2002:python/object/apply:numpy.core.multiarray.scalar"
                    in str(e)
                ):
                    validation_output = textwrap.dedent(f"""
                        <h1>🚩 Results Validation</h1> Your code produced a <code>{filename}</code> file that contains Python objects.
                        You probably intended them to be human-readable strings or numbers.
                        See the guide for troubleshooting <a href='https://github.com/UofT-Econ-DataAnalytics/files/wiki/%E2%98%81%EF%B8%8F-Online:-Python#the-code-to-automatically-validate-your-results-failed-with-an-error'>Online Python</a>
                        or <a href='https://github.com/UofT-Econ-DataAnalytics/files/wiki/%F0%9F%92%BB-Local:-Python'>Local Python</a> for more details.<br><br>
                        """)
                else:
                    raise e

    if validation_output:
        with open(output_file, "w") as f:
            f.write(validation_output)
        return False
    return True


def load_submitted_results(filename: str) -> dict:
    with open(filename, "r") as f:
        submitted = yaml.load(f, Loader=yaml.SafeLoader)

    # Convert numeric strings to floats
    for key, value in submitted.items():
        if isinstance(value, str):
            try:
                submitted[key] = float(value)
            except ValueError:
                pass

    return submitted


def load_correct_results(json_string: str) -> dict:
    if json_string:
        correct = json.loads(json_string)
    else:
        raise ValueError("No correct results provided, --correct cannot be empty.")
    return correct


def compare_results(
    submitted: dict, correct: dict, input_file: str, output_html: str, output_yaml: str
) -> bool:
    validation_output = []
    errors = False

    def reldif(a, b):
        return abs(a - b) / a

    validated = {"VALIDATED_COUNT": 0}

    for key, value in correct.items():
        if key not in submitted:
            errors = True
            validation_output.append(f"⭕️ no value submitted for <code>{key}</code>")
            validated["VALIDATED_" + key] = "⭕️"
        elif reldif(value, submitted[key]) > 0.01:
            errors = True
            validation_output.append(
                f"❌ {submitted[key]} is not the correct result for <code>{key}</code>"
            )
            validated["VALIDATED_" + key] = "❌"
        else:
            validation_output.append(f"✅ <code>{key}</code>")
            validated["VALIDATED_" + key] = "✅"
            validated["VALIDATED_COUNT"] += 1

    with open(output_html, "w") as f:
        if errors:
            f.write(
                f"<h1>❌ Results Numbers Validation</h1> There are mistakes or omissions in <code>{input_file}</code>: <ul>"
            )
        else:
            f.write(
                f"<h1>✅ Results Numbers Validation</h1> All results in <code>{input_file}</code> are correct: <ul>"
            )
        for line in validation_output:
            f.write(f"<li>{line}</li>")
        f.write("</ul>\n\n")
        f.write("<b>Generated output:</b>\n\n")
        f.write("```yaml\n")
        with open(input_file, "r") as f_input:
            f.write(f_input.read())
        f.write("```\n\n")

    if output_yaml:
        with open(output_yaml, "w") as f:
            yaml.dump(validated, f, allow_unicode=True)

    return not errors


def check_files_exist(files: list, output_file: str) -> bool:
    validation_output = []
    errors = False
    for file in files:
        if not os.path.isfile(file):
            errors = True
            validation_output.append(f"⭕️ did not find <code>{file}</code>")
        else:
            validation_output.append(f"🟢 <code>{file}</code>")

    # Append validation output to existing file
    with open(output_file, "a") as f:
        if errors:
            f.write(
                "<h1>⭕️ Results Files Validation</h1> Some expected results files were not created: <ul>"
            )
        else:
            f.write(
                "<h1>🟢 Results Files Validation</h1> All expected results files were created: <ul>"
            )
        for line in validation_output:
            f.write(f"<li>{line}</li>")
        f.write("</ul>")
        f.write(
            "<i>This check only verifies the files exist, not whether they are correct. The files will be graded manually.</i>"
        )

    return not errors


def main() -> int:
    args = parse_args()
    config = load_config(args.config)

    valid_yaml = check_submitted_results_are_valid(
        filename=config["results_submitted_path"], output_file=args.output
    )

    if valid_yaml:
        results_match = compare_results(
            submitted=load_submitted_results(config["results_submitted_path"]),
            correct=load_correct_results(args.correct),
            input_file=config["results_submitted_path"],
            output_html=args.output,
            output_yaml=args.output_yaml,
        )
    else:
        results_match = False

    if config.get("results_created_files"):
        files_exist = check_files_exist(
            files=config["results_created_files"], output_file=args.output
        )
    else:
        files_exist = True

    if valid_yaml and results_match and files_exist:
        return 0
    else:
        return 2


if __name__ == "__main__":
    sys.exit(main())
