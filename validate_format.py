import yaml
import re
import requests

def validate_url(url, expected_status=200):
    try:
        response = requests.head(url, allow_redirects=True)
        if response.status_code != expected_status:
            print(f"URL check failed for {url} with status code {response.status_code}")
            return False
    except requests.RequestException as e:
        print(f"Request failed for {url}: {e}")
        return False
    return True

def find_social_media_urls(text):
    # Regex to find URLs - simplified version
    urls = re.findall(r'https?://(?:www\.)?(linkedin\.com|twitter\.com|x\.com)/[^\s]+', text)
    return urls

def validate_file(file_path):
    with open(file_path, 'r') as file:
        parts = file.read().split('---')
        if len(parts) < 3:
            print("Invalid file structure. Could not find YAML front matter.")
            return False
        yaml_content = parts[1]
        text_content = parts[2]

    try:
        content = yaml.load(yaml_content, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        print(f"Error in YAML parsing: {exc}")
        return False

    # Validate required fields
    required_fields = ['number', 'title', 'topic', 'team_leads', 'github', 'youtube_video']
    for field in required_fields:
        if field not in content:
            print(f"Missing required field: {field}")
            return False

    # Validate team leads and contributors format
    if 'team_leads' in content and not validate_person_format(content['team_leads']):
        return False
    if 'contributors' in content and not validate_person_format(content['contributors']):
        return False

    # Validate GitHub URL
    github_url = f"https://github.com/{content['github']}"
    if not validate_url(github_url):
        return False

    # Validate YouTube URL
    youtube_url = f"https://www.youtube.com/watch?v={content['youtube_video']}"
    if not validate_url(youtube_url):
        return False

    # Validate social media URL
    social_media_urls = find_social_media_urls(text_content)
    if not social_media_urls:
        print("No social media URL found in the text.")
        return False
    for url in social_media_urls:
        if not validate_url(url):
            return False

    print("Validation successful.")
    return True

if __name__ == "__main__":
    import sys
    if not validate_file(sys.argv[1]):
        sys.exit(1)