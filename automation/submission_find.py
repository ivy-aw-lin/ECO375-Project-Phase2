#!/usr/bin/env python3
import json, os, re, sys

def obtain_code_file(filename: str) -> dict:

    valid_submission_files = [filename + ext for ext in ['.ipynb', '.py', '.r', '.do']]
    valid_code_files = [filename + ext for ext in ['.py', '.r', '.do']]

    # Check there is exactly one file matching the specified filename (not case sensitive)
    submitted_file_original = count_file_presence(
        valid_files = valid_submission_files,
        required = 1
    )[0]

    # Rename submitted file to lowercase
    submitted_file = submitted_file_original.lower()
    if submitted_file_original != submitted_file:
        os.rename(submitted_file_original, submitted_file)

    # If the submitted file is a Jupyter notebook, convert it to a script.
    if submitted_file == filename + '.ipynb':
        os.system('jupyter nbconvert --to script ' + submitted_file)

    # Check there is exactly one code file (not case sensitive)
    code_file = count_file_presence(
        valid_files = valid_code_files,
        required = 1
    )[0]

    # Check the file type of the code file
    submission = {
        'file': code_file,
        'original': submitted_file_original
    }

    if code_file.endswith('.py'):
        submission['lang'] = 'python'
        submission['python'] = True
        submission['r'] = False
        submission['stata'] = False
    elif code_file.endswith('.r'):
        submission['lang'] = 'r'
        submission['python'] = False
        submission['r'] = True
        submission['stata'] = False
    elif code_file.endswith('.do'):
        submission['lang'] = 'stata'
        submission['python'] = False
        submission['r'] = False
        submission['stata'] = True
    else:
        raise ValueError(f'ERROR: {code_file} must be .py, .r, or .do')
    
    # Check if other languages are needed
    with open(code_file, 'r') as file:
        content = file.read()
        
        match = re.search(r'{"project_languages":\[.*?\]}', content)
        if match:
            languages_json_str = match.group(0)
            languages_json = json.loads(languages_json_str)
            project_languages = languages_json.get('project_languages', [])
            
            if "stata" in project_languages:
                submission['stata'] = True
            if "R" in project_languages or "r" in project_languages:
                submission['r'] = True
            if "python" in project_languages:
                submission['python'] = True

    return submission

def count_file_presence(valid_files: list[str], required: int = None) -> list[str]:
    ''' Check whether files in valid_files are present in cwd
        (not case sensitive)
    '''

    valid_files_lowercase = set(file.lower() for file in valid_files)
    found_files = set()
    found_files_lowercase = set()

    for file in os.listdir('.'):
        if os.path.isfile(file) and file.lower() in valid_files_lowercase:
            found_files.add(file)
            found_files_lowercase.add(file.lower())

    if required is not None:
        if len(found_files) != required:
            error_message = f"<h1>❌ Submission Error</h1> There must be exactly {required} of the following files, found {len(found_files)}: <ul>"
            for file in valid_files_lowercase:
                if file in found_files_lowercase:
                    error_message += f'<li>🔴 {file}</li>'
                else:
                    error_message += f'<li>{file}</li>'
            error_message += "</ul>"

            print(error_message)
            sys.exit(1)

    return list(found_files)

def main() -> int:
    submission = obtain_code_file('submission')
    print(json.dumps(submission))
    return 0

if __name__ == '__main__':
    sys.exit(main())
