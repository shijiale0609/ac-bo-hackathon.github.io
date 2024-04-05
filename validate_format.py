import yaml
import re
import requests


class ValidationError(Exception):
    """Exception raised for errors in the validation process."""

    def __init__(self, file_path, errors):
        message = f"Multiple validation errors occurred in {file_path}:\n" + "\n".join(
            errors
        )
        super().__init__(message)


def validate_person_format(person_list, errors):
    # This pattern allows for nested parentheses and simple HTML anchor tags.
    # It's not foolproof and assumes relatively well-formed HTML.
    for person in person_list:
        # Check if the entry matches the allowed format with HTML links and nested parentheses.
        if not re.match(
            r"^.+ \((?:[^()]|\([^()]*\))*\) @(?:[^\s]|<a\s+[^>]*>[^<]*<\/a>)+$", person
        ):
            errors.append(f"Invalid format for person entry: {person}")


# def validate_person_format(person_list, errors):
#     for person in person_list:
#         if not re.match(r"^.+ \(.+\) @.+$", person):
#             errors.append(f"Invalid format for person entry: {person}")


def validate_url(url, expected_status=200, errors=None):
    if errors is None:
        errors = []
    try:
        response = requests.head(url, allow_redirects=True)
        if response.status_code != expected_status:
            errors.append(
                f"URL check failed for {url} with status code {response.status_code}"
            )
    except requests.RequestException as e:
        errors.append(f"Request failed for {url}: {e}")


def find_social_media_urls(text):
    urls = re.findall(
        r"https?://(?:www\.)?(linkedin\.com|twitter\.com|x\.com)/[^\s]+", text
    )
    return urls


def validate_file(file_path):
    errors = []
    with open(file_path, "r") as file:
        parts = file.read().split("---")
        if len(parts) < 3:
            print("Invalid file structure. Could not find YAML front matter.")
            errors.append("Invalid file structure. Could not find YAML front matter.")
        yaml_content, text_content = parts[1], parts[2]

    try:
        content = yaml.load(yaml_content, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        print(f"Error in YAML parsing: {exc}")
        errors.append(f"Error in YAML parsing: {exc}")

    required_fields = [
        "number",
        "title",
        "topic",
        "team_leads",
        "github",
        "youtube_video",
    ]
    for field in required_fields:
        if field not in content:
            print(f"Missing required field: {field}")
            errors.append(f"Missing required field: {field}")

    if "team_leads" in content:
        validate_person_format(content["team_leads"], errors)
    if "contributors" in content:
        validate_person_format(content["contributors"], errors)

    if "github" in content:
        github_url = f"https://github.com/{content['github']}"
        validate_url(github_url, errors=errors)

    if "youtube_video" in content:
        youtube_url = f"https://www.youtube.com/watch?v={content['youtube_video']}"
        validate_url(youtube_url, errors=errors)

    social_media_urls = find_social_media_urls(text_content)
    if not social_media_urls:
        errors.append("No social media URL found in the text.")
    for url in social_media_urls:
        validate_url(url, errors=errors)

    if errors:
        raise ValidationError(file_path, errors)


if __name__ == "__main__":
    import sys

    validate_file(sys.argv[1])
