# Interacting with outside world

## COPY
Copy copies files & data from our non sandbox environment to our sandbox environment, without running copy then our data is not available to the sandbox

example:
```dockerfile
# you can copy files
COPY my_app.py my_app.py
# or directories
COPY app /usr/docker/app
```

# USER
User specifies which user to use - good for installing packages that require root access

# EXPOSE
this determin's what ports to "expose" to the outside world, be default no ports are accessible 

# ENV
Sets environment variables for the web app

# WORKDIR
Specifies which directory is considered "Home"