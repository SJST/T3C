import git

repo = git.Repo('D:\SJT\TestingAuto\docs')
remote = repo.remote()
remote.pull()




