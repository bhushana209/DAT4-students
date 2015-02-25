## DAT4 Student Repository

Student work for [General Assembly's Data Science course](https://generalassemb.ly/education/data-science/washington-dc/) in Washington, DC (12/15/14 - 3/16/15).

View course materials in the [main course repository](https://github.com/justmarkham/DAT4).

#### Guidelines for contributing

 * Use valid Markdown in your Markdown files
 * When naming files, never use spaces and generally avoid capital letters
 * Don't add large files unless absolutely necessary (e.g., resize your images to a reasonable size)

#### Initial setup

 1. Fork the [primary DAT4-students repo](https://github.com/justmarkham/DAT4-students) on GitHub
 2. `git clone URL_of_your_fork`: copy your fork to your local computer (automatically defines your fork as the remote origin)
 3. `cd DAT4-students`: change into the DAT4-students subdirectory that was just created
 4. `git remote add upstream URL_of_primary_repo`: define the primary DAT4-students repo as the remote upstream

#### Recipe for submitting homework

 1. `git pull upstream master`: fetch changes from the master branch of upstream, and merge those changes into your master branch
 2. Copy your homework file(s) to your folder
 3. `git add .` or `git add name_of_file`: stage file modifications, additions, and deletions
 4. `git status`: check that you staged what you intended to stage
 5. `git commit -m "message about commit"`: commit any changes that have been staged
 6. `git push origin master`: push your changes to the origin
 7. On GitHub, create a [pull request](https://help.github.com/articles/using-pull-requests): ask the upstream to merge your changes into its master branch

#### Other useful commands

 * `git status`: view the status of files in your repo (untracked, modified, staged)
 * `git log`: view the detailed commit history (type `q` to quit)
   * `git log -1`: only show the last commit (you can use any number)
   * `git log --oneline`: show each commit on a single line
 * `git remote -v`: view your remotes
 * [Detailed reference guide](http://gitref.org/)
 * [Quick reference guide](http://www.dataschool.io/git-quick-reference-for-beginners/)
