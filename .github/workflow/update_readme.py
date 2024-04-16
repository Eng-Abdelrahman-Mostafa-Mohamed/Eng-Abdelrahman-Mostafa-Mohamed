import requests
import json

def get_wakatime_stats(username, api_key):
  """Fetches Wakatime stats for a given username using the Wakatime API.

  Args:
      username (str): The Wakatime username for which to retrieve stats.
      api_key (str): The Wakatime API key for authentication.

  Returns:
      dict or None: A dictionary containing Wakatime statistics for the user,
                    or None if an error occurs.
  """

  url = f"https://api.wakatime.com/v1/users/{username}/stats/last_week"
  headers = {"Authorization": f"Bearer {api_key}"}

  try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    return json.loads(response.text)
  except requests.exceptions.RequestException as e:
    print(f"Error fetching Wakatime stats: {e}")
    return None

def generate_stats_chart_markdown(stats):
  """Generates Markdown content representing Wakatime statistics in a chart format.

  Args:
      stats (dict): A dictionary containing Wakatime statistics.

  Returns:
      str: Markdown-formatted text with the statistics in a chart-like format using Unicode characters.
  """

  if not stats:
    return "Unable to retrieve Wakatime stats."

  markdown = f"## Wakatime Stats (Last Week)\n\n"

  total_seconds = stats.get("total_seconds")
  if total_seconds:
    total_hours = int(total_seconds // 3600)
    markdown += f"**Total Coding Time:** {total_hours} hours\n"
    # Example chart-like formatting using text bars (replace with actual chart library if desired)
    markdown += f"[```]\n"
    markdown += f"{'=' * total_hours[:20]}\n"  # Simulate a progress bar
    markdown += f"[```]\n"

  languages = stats.get("languages")
  if languages:
    markdown += "**Languages Used:**\n"
    total_language_seconds = sum(data.get("total_seconds", 0) for _, data in languages.items())
    for language, data in languages.items():
      language_seconds = data.get("total_seconds", 0)
      percentage = (language_seconds / total_language_seconds) * 100
      markdown += f"  * {language}: {int(percentage)}% ({language_seconds} seconds)\n"
      markdown += f"      {'█' * int(percentage // 5)}{' ' * (20 - int(percentage // 5))}\n"  # Simulate a language usage bar

  # ... (add logic for other stats like operating systems, editors, etc.)

  return markdown

# Example usage (replace with your actual Wakatime username)
username = "ENG_Abdelrahman"
api_key = os.environ.get("waka_d7d1d3fe-5bb8-47e3-b1d1-95dbb81722b2")  # Access API key from environment variable

stats = get_wakatime_stats(username, api_key)
stats_markdown = generate_stats_chart_markdown(stats)

# Update your README file dynamically (use a suitable method based on your version control system)
# (This part will be handled by GitHub Actions)
