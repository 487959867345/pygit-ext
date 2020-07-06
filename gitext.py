import urllib.request
from github import Github

def download_file(token, target_filename,local_file_name, repo=None):
	user = Github(token)
	
	if repo == None:
		for repos in user.get_user().get_repos():
			for files in repos.get_contents(""):
				if files.path == target_filename:
					print(files.path)
					dfile = urllib.request.urlretrieve(files.download_url, local_file_name)
					return
	else:
		target_repo = user.get_repo(repo)

	for files in target_repo.get_contents(""):
		if files.path == target_filename:
			ext = len(files.path)
			extension = files.path[ext - 3 :]
			print(extension)
			dfile = urllib.request.urlretrieve(files.download_url, local_file_name + extension)
			return


