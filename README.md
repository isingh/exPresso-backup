Express Yourself
==================

Git configurations
------------------
* Fork the main repo located at `https://github.com/isingh/exPresso` by clicking Fork.
* On your local machine clone your forked repo:
```
git clone git@github.com:<your_github_username>/exPresso.git
```
* Add the main repo as a remote repo:
```
git remote add exPresso git@github.com:isingh/exPresso.git
```

Creating a Pull Request
------------------
* Navigate to your master by `git checkout master`
* Get the latest merged code by running `git pull exPresso master`
* Create a new branch: git checkout -b my_working_branch (-b specified create a new branch)
* Make changes and commit them (`git commit -a`)
* Once the change is ready push it to _your_ repo by doing `git push origin my_working_branch`
* Now goto your fork `https://github.com/<your_github_username>/exPresso`
  * Click on Branches and select your branch (the one you pushed, my_working_branch)
  * Click on Pull Request button next to the fork button.
  * Make sure all the commits and changes are accounted. Tag people if needed.
  * Issue the actual requests.
