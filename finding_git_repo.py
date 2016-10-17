import os
import unittest
import shutil
import tempfile
def is_git_repo(path):
	return '.git' in os.listdir(path) 

def find_git_repo(path):
	result = []
	for dirpath, dirnames, filenames in os.walk(path):
		for dirname in dirnames:
			full_dir_path = os.path.join(dirpath,dirname)
			if is_git_repo(full_dir_path):
				result.append(full_dir_path)
	return result

def create_git_repo(path):
	gitdir = os.path.join(path, '.git')
	os.makedirs(gitdir)


class TestFindGitRepos(unittest.TestCase):
	def setUp(self):
		#Create a temp dir and make a git repo
		self.root = tempfile.mkdtemp()
	def tearDown(self):
		shutil.rmtree(self.root)

	def test_is_git_repo_should_detect_git_repo(self):
		#Given
		gitdir = os.path.join(self.root, 'junk')
		create_git_repo(gitdir)

		#When
		result = is_git_repo(gitdir)

		#Then

		self.assertTrue(result)
	def test_is_git_repo_should_not_detect_non_git_repo(self):
		#Given
		gitdir = os.path.join(self.root, 'junk')
		os.mkdir(gitdir)

		#When
		result = is_git_repo(gitdir)

		#Then

		self.assertFalse(result)

	def test_is_git_repo_should_all_repos(self):
		#Given
		gitdir = os.path.join(self.root, 'junk')
		os.mkdir(gitdir)

		#When
		result = is_git_repo(gitdir)

		#Then

		self.assertFalse(result)

if __name__ == '__main__':
	unittest.main()