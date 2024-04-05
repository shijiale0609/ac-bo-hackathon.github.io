import glob
from validate_format import validate_file


def test_project_files():
    files = sorted(glob.glob("_projects/*.md"))
    errors = []
    for file in files:
        try:
            result = validate_file(file)
            if not result:
                errors.append(f"Validation failed for {file}")
        except Exception as e:
            errors.append(f"Exception occurred while validating {file}: {e}")
    assert not errors, "\n".join(errors)


if __name__ == "__main__":
    test_project_files()
