from os.path import join
from pathlib import Path

# Directories
PROJECT_DIRECTORY = Path(__file__).parents[1]
SRC_DIRECTORY = join(PROJECT_DIRECTORY, "src")
INPUT_DIRECTORY = join(PROJECT_DIRECTORY, "input")
RESULT_DIRECTORY = join(PROJECT_DIRECTORY, "results")
CLASS_DIRECTORY = join(SRC_DIRECTORY, "classes")
INTERMEDIATE_DIRECTORY = join(SRC_DIRECTORY, "intermediate_results")
WORD_LIST_DIRECTORY = join(INPUT_DIRECTORY, "defined_word_lists")
GDPR_REALIZATION_INPUT_DIRECTORY = join(INPUT_DIRECTORY, "gdpr_realization_documents")
GDPR_REGULATION_INPUT_DIRECTORY = join(INPUT_DIRECTORY, "gdpr_regulatory_documents")
ISO_REALIZATION_INPUT_DIRECTORY = join(INPUT_DIRECTORY, "iso_realization_documents")
ISO_REGULATION_INPUT_DIRECTORY = join(INPUT_DIRECTORY, "iso_regulatory_documents")