from git import Repo
from git import Submodule
import git 

repo = Repo('fullstack-interview-test/')
assert not repo.bare
#assert not repo.is_dirty()
""" print(repo.untracked_files)
print(repo.head.ref)
print(repo.head.commit) """


""" for el in repo.refs:
  print(el.log()) """

#print(repo.heads.master.log())
""" el = repo.heads.master.log()
print(el[0])
print(el[-1]) """

""" print(repo.head.commit.tree.blobs[1].data_stream.read())

print(repo.commit('HEAD'))
commits = list(repo.iter_commits('master'))
print(commits) """

""" for commit in commits:
  print(commit.committed_date)
  print(commit.message) """
#print(repo.active_branch)


""" print(repo.heads)
repo.heads['master'].checkout()
print(repo.head.reference) """

""" print(repo.submodule)
#For creating a submodule
Submodule.add(repo, 'test', './fullstack-interview-test/sm', url='https://github.com/Danble/fullstack-interview-test') """
#print(repo.submodules)

alfonso = repo.branches['alfonsolzrg-add-instructions'].checkout()
generator = repo.iter_commits()
print(next(generator))
print(next(generator))

master = repo.branches['master'].checkout()
generator = repo.iter_commits()
print(next(generator))
print(next(generator))
print(next(generator))
#print(next(generator))

print(git.objects.util.parse_actor_and_date(next(generator).__str__()))

""" print(next(generator).athor)
print(next(generator).committed_date)
print(next(generator).committed_datetime)
print(next(generator).count()) """

""" 
master = repo.branches['master']
alfonso = ...
base = repo.merge_base(alfonso, master)
repo.index.merge_tree(master, base=base)
print(repo.index.commit('my test merge', parent_commits=(master.commit, alfonso.commit))) """
