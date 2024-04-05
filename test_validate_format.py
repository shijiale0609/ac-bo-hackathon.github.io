import glob
from validate_format import validate_file


def test_project_files():
    files = sorted(glob.glob("_projects/*.md"))
    errors = []
    for file in files:
        try:
            validate_file(file)
        except Exception as e:
            errors.append(e)
    assert not errors, "\n".join(errors)


if __name__ == "__main__":
    test_project_files()
