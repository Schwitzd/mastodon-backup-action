# Mastodon Backup GitHub Action

This GitHub Action automates the backup of Mastodon posts.

## Inputs

- `mastodon_base_url` (required): The base URL of your Mastodon instance.
- `mastodon_access_token` (required): The access token needed to authenticate and access Mastodon's API.

## Usage

To use this action, create a workflow YAML file (e.g., `.github/workflows/mastodon-backup.yml`) in your dedicated backup repository with the following content:

```yaml
name: Backup Mastodon Posts

on:
  schedule:
    - cron: '0 0 * * 5'  # Runs every Friday at midnight
  workflow_dispatch:

jobs:
  mastodon-backup:
    runs-on: ubuntu-latest

    steps:
      - name: Mastodon Backup
        uses: Schwitzd/mastodon-backup-action@v1
        with:
          mastodon_access_token: ${{ secrets.MASTODON_ACCESS_TOKEN }}
          mastodon_base_url: ${{ vars.MASTODON_BASE_URL }}
```

### Adding Secrets and Variables

To add the necessary secrets and variables:

1. Repository secret & variable:
    - Go to your dedicated backup repository on GitHub.
    - Navigate to **Settings → Secrets and variables → Actions → New repository secret**.
    - In the tab **Secrets**:
        - MASTODON_ACCESS_TOKEN: The access token needed to authenticate and access Mastodon's API.
    - In the tab **Variables**:
        - MASTODON_BASE_URL: The base URL of your Mastodon instance.

1. Workflow Permissions:
    - To allow the Action to write to your backup repository, go to **Settings → Actions -> General → Workflow permissions**.
    - Ensure the permissions are set to **Read and write for the workflow** to have the necessary access.
