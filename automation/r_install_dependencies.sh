#!/bin/bash

function usage {
    echo "Usage: $(basename $0) -r REQUIREMENTS_FILE [-o LOG_FILE]" 2>&1
    echo '   -r     Path to file listing R packages to install'
    echo '   -o     Path to log file, default: packages-r.log'
    exit 1
}

# Parse arguments
log="packages-r.log"
while getopts :r:o: option; do
    case "${option}" in
        r) requirements="${OPTARG}";;
        o) log="${OPTARG}";;
        ?)
            echo "Invalid option: -${OPTARG}."
            echo
            usage
            exit 1
            ;;
    esac
done

# Check if requirements file is provided
if [ -z "${requirements}" ]; then
    echo "You must provide a requirements file using the -r option."
    usage
    exit 1
fi

# Install R packages
Rscript -e "install.packages('requiRements', repos='https://cloud.r-project.org/')"
Rscript -e "requiRements::install(path_to_requirements = '${requirements}')" 2>&1 | tee ${log}
if grep --quiet 'non-zero exit status' ${log}; then
  exit 1
fi
