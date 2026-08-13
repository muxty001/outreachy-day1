import urllib.request
import json
from typing import Dict, Any  # Fix 1: Correct import syntax

class GitHubService:
    """
    Fetches open-source repository details from a remote server API.
    """
    def __init__(self, base_url: str = "https://api.github.com"):  # Fix 2: Exactly two underscores
        self.base_url = base_url

    def fetch_repo_info(self, owner: str, repo: str) -> Dict[str, Any]:
        """
        Sends an HTTP GET request to retrieve repository metadata.
        """
        # Fix 3: Include both owner and repo in the URL path
        url = f"{self.base_url}/repos/{owner}/{repo}"
        
        request = urllib.request.Request(url, headers={"User-Agent": "PythonApp"})

        # Fix 4: Use urlopen to execute the network request
        with urllib.request.urlopen(request) as response:
            if response.status != 200:
                raise RuntimeError(f"API Request Failed with status {response.status}")

            raw_data = response.read().decode("utf-8")
            return json.loads(raw_data)