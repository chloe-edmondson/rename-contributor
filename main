import getpass
from github import Github

# Get user credentials
username = input("Enter your GitHub username: ")
password = getpass.getpass("Enter your GitHub password: ")

# Authenticate with GitHub
g = Github(username, password)

# Get the new contributor name
new_name = input("Enter the new contributor name: ")

# Iterate through all repositories
for repo in g.get_user().get_repos():
    # Get the contributors for each repository
    contributors = repo.get_contributors()
    
    # Rename the contributor if the old name is found
    for contributor in contributors:
        if contributor.login == username:
            print(f"Renaming {contributor.login} to {new_name} in repository {repo.full_name}")
            contributor.edit(name=new_name)
            break
