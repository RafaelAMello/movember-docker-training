# My First Dockerfile

To build a docker image & run it you should run:
```bash
$ docker build . -t my-first-docker-images/python-hello-world:latest
$ docker run my-first-docker-images/python-hello-world:latest
```
Wait what just happened??
This builds your first Docker Image and ran it based on the Dockerfile - this is how the Dockerfile works:

## Dockerfile instructions:
Dockerfile syntax:
```Dockerfile
INSTRUCTION arguments
RUN echo "For example"
```
These are the components of a Dockerfile
## FROM
Every Dockerfile you **needs** a FROM, it is structured as so:
```Dockerfile
FROM remote/path/image:reference
```
### Remote
Remote can be dockerhub.io (think github for docker containers) or Amazon Elastic Container Registry, a private AWS solution, in the absence of a remote docker will assume 

### Path (usually creator)
This is the subdirectory of the Docker Image, on dockerhub this is the creator but can be whatever the repository determines what repo to use
Examples:
docker.io/rafaelamello/image:reference
mcr.microsoft.com/windows/nanoserver

### Image
Image what you want to build from
For us 90 % will be **python** but can be others, for example:
1. [microsoft/nanoserver](https://hub.docker.com/_/microsoft-windows-nanoserver)
2. [postgres](https://hub.docker.com/_/postgres?tab=reviews)
3. etc

### Reference
Reference is what tag you want to use - think of these as releases
every time the python image is updated (eg they release a new version of python) they will release a new tag, usually docker providers provide a `latest` tag to show latest and greatest version

***BEST PRACTICE ALERT***
> `latest` is good for testing but YOU SHOULD NEVER USE IT IN PRODUCTION as it is often overwritten to ensure are consistent with your deployments always use a tag

## RUN
RUN runs arbitrary code inside the container, this code is ***SANDBOXED*** it can only access resources available to it inside the container and its effects do not impact your computer

Here we can install libraries to run our code
EG:
```Dockerfile
RUN pip install requests==2.24.0
RUN pip install -r usr/docker/app/requirements.txt
```

## CMD & ENTRYPOINT
CMD & ENTRYPOINT do similar things but are designed for different purposes

ENTRYPOINT exists to abstract away setup, by default you should expect that ENTRYPOINT will always be run when you use this container

CMD exists to give a default execution pattern but can easily overwritten, so for example CMD can be "run the app" but can easily be overwritten to be "run the tests"

This difference is highlighted more in the next example

```bash
docker run my-first-docker-images/python-hello-world:latest  -c 'print("lets overwrite cmd with this print")'
```

***BEST PRACTICE ALERT***
> while you can overwrite --entrypoint its not considered kosher and should be used really only for debugging not prod