### Python MySQL Tutorial Files

This folder contains all the files I created while following the [Python MySQL tutorial found here.](https://www.mysqltutorial.org/python-mysql/).

[https://www.mysqltutorial.org/](https://www.mysqltutorial.org/) in general is a great source for learning MySQL.

### Dependencies

These programs depend a few files and installations to be run correctly, all of which are explained in the tutorial. 

I had to make a small deviation from the tutorial for my programs to work. The tutorial has you connect to the database as the `root` user. This gave me a "permission denied" error, because on my Ubuntu MySQL installation, the `root` user uses the `auth_socket` plugin. I had to create a new user and connect to the database with that user, which also required me to specify a port. If you have a similar issue, this may be the fix.

### Example Config.ini

An example configuration file is shown below. In theory, this contains sensitive information and shouldn't be uploaded to a repository (leave out by adding it to .gitignore). In practice, if the database is local to your computer, then accidently uploading it to a repository isn't a big deal.

```
[mysql]  
host = [hostname]  
port = [portnumber]  
database = [database being used] 
user = [username]  
password = [password]
```

