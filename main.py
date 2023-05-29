import getpass
import requests

# Get user credentials
username = input("Enter your GitHub username: ")
token = getpass.getpass("Enter your GitHub personal access token: ")

# Get the new contributor name
new_name = input("Enter the new contributor name: ")

# API endpoint for fetching repositories
repo_api_url = "https://api.github.com/user/repos"

try:
    # Authenticate with GitHub API using the personal access token
    headers = {"Authorization": f"Token {token}"}
    response = requests.get(repo_api_url, headers=headers)
    response.raise_for_status()
    repos = response.json()

    # Iterate through all repositories
    for repo in repos:
        try:
            # Get contributors for each repository
            contributors_api_url = f"https://api.github.com/repos/{repo['full_name']}/contributors"
            response = requests.get(contributors_api_url, headers=headers)
            response.raise_for_status()
            contributors = response.json()

            # Check if the old name is found among contributors
            contributor_found = False
            for contributor in contributors:
                if contributor['login'] == username:
                    contributor_found = True
                    contributor_url = f"https://api.github.com/repos/{repo['full_name']}/collaborators/{username}"
                    data = {"name": new_name}
                    response = requests.patch(contributor_url, headers=headers, json=data)
                    response.raise_for_status()
                    if response.status_code == 200:
                        print(f"Renamed contributor {username} to {new_name} in repository {repo['full_name']}")
                    else:
                        print(f"Failed to rename contributor {username} in repository {repo['full_name']}")

            if not contributor_found:
                print(f"Contributor {username} not found in repository {repo['full_name']}")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred while processing repository {repo['full_name']}: {str(e)}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred during authentication: {str(e)}")
