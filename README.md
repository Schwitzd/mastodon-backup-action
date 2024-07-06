# Mastodon Posts Backup

This repository contains a Python script to backup posts (toots) from a Mastodon instance and automate the process using GitHub Actions.

## Usage

To use this backup script and GitHub Action:

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

1. Ensure you have the following secrets set in your GitHub repository settings:
    * MASTODON_ACCESS_TOKEN: Access token for Mastodon API.
    * MASTODON_BASE_URL: Base URL of your Mastodon instance.

1. Run the backup manually or automatically:
    * **Manual Trigger**: You can trigger the backup manually using GitHub Actions by selecting the workflow and running it.
    * **Automatic Trigger**: By default, the workflow is set to run every Friday at midnight UTC. You can adjust this schedule in the .github/workflows/mastodon-backup.yml file.

1. Remove backup files (if cloning this repository):
    * Before making any commits or modifications, ensure to remove any existing `mastodon_posts_<year>.json` files to prevent unnecessary conflicts.