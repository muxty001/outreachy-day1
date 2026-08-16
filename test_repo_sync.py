import pytest
from unittest.mock import MagicMock
from repo_sync import RepoSyncManager

@pytest.fixture
def mock_github_service():
    """
    Creates a reusable mock GitHubService fixture for tests.
    """
    service = MagicMock()
    # Define default return value for fetch_repo_info calls
    service.fetch_repo_info.side_effect = [
        {"name": "my-fork", "stargazers_count": 10},      # First call (fork)
        {"name": "awesome-python", "stargazers_count": 1500} # Second call (upstream)
    ]
    return service

def test_check_sync_status(mock_github_service):
    sync_manager = RepoSyncManager(service=mock_github_service)
    status = sync_manager.check_sync_status("dev_user", "vinta", "awesome-python")

    assert status["fork"] == "my-fork"
    assert status["upstream_stars"] == 1500
    assert status["status"] == "In Sync"
    
    # Assert fetch_repo_info was called exactly twice (once for fork, once for upstream)
    assert mock_github_service.fetch_repo_info.call_count == 2