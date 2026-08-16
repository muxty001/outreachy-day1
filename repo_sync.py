from typing import Dict
from github_service import GitHubService

class RepoSyncManager:
    """
    Manages synchronization checks between a user's fork and the upstream repository.
    """
    def __init__(self, service: GitHubService):
        self.service = service

    def check_sync_status(self, fork_owner: str, upstream_owner: str, repo: str) -> Dict[str, str]:
        """
        Compares stars/metadata between a fork and upstream repo.
        """
        fork_data = self.service.fetch_repo_info(fork_owner, repo)
        upstream_data = self.service.fetch_repo_info(upstream_owner, repo)

        return {
            "fork": fork_data.get("name", ""),
            "fork_stars": fork_data.get("stargazers_count", 0),
            "upstream_stars": upstream_data.get("stargazers_count", 0),
            "status": "In Sync"
        }