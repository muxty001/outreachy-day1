from unittest.mock import patch, MagicMock  # Fix 1: Correct spelling
from github_service import GitHubService     # Fix 1: Matching class name

@patch("urllib.request.urlopen")
def test_fetch_repo_info_mocked(mock_urlopen):
    """
    Tests fetching repo info without sending a real network request.
    """
    # 1. Create mock response
    mock_response = MagicMock()
    mock_response.status = 200  # Fix 2: Set .status attribute, don't overwrite object
    mock_response.read.return_value = b'{"name": "awesome-python", "stargazers_count": 1500}'

    # 2. Attach mock response to context manager return value
    mock_urlopen.return_value.__enter__.return_value = mock_response

    # 3. Call service method
    service = GitHubService()
    repo_data = service.fetch_repo_info("vinta", "awesome-python")

    # 4. Assertions
    assert repo_data["name"] == "awesome-python"
    assert repo_data["stargazers_count"] == 1500

    mock_urlopen.assert_called_once()