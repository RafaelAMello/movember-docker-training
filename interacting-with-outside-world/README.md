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

# Copy Command Coppies a Local File INTO the dockercontainer
# COPY
# USER
# EXPOSE
# ENV
# WORKDIR