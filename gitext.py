import urllib.request
from github import Github
class Download():
	def download_file(token, target_filename,local_file_name, repo=None):
		user = Github(token)
	
		if repo == None:
			for repos in user.get_user().get_repos():
				for files in repos.get_contents(""):
					if files.path == target_filename:
						print(files.path)
						urllib.request.urlretrieve(files.download_url, local_file_name)
						return
		else:
			target_repo = user.get_repo(repo)

		for files in target_repo.get_contents(""):
			if files.path == target_filename:
				ext = len(files.path)
				extension = files.path[ext - 3 :]
				urllib.request.urlretrieve(files.download_url, local_file_name + extension)
				return
	def download_repo(token,target_repo,dir_path, ignore_extensions=[]):
		user = Github(token)

		for repo in user.get_user().get_repos():
			if repo.full_name == target_repo:
				for contents in repo.get_contents(""):
					for bexts in ignore_extensions:
						if contents.path.endswith(bexts):
							pass
						else:
							print(f"downloading {contents.path}")
							urllib.request.urlretrieve(contents.download_url,f'{dir_path}/{contents.path}')

