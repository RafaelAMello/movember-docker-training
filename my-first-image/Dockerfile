# From defines our "Base Image" this can be prebuilt to whatever extent we want it to
# You can search in https://hub.docker.com/ to see many publicly available images
# Note this should be like considering installing new software - only install from trusted sources
# the python image library is a Docker "Offical Image" installed over 1 Billion times so we can trust this
FROM python:3.7.9-alpine

# Alpine is a light wight version of python with lower overhead
# its considered good practice to use it for lighter apps
# But some libraries with strong C bindings (eg pandas) does not work on it
# you can use FROM python:3.7.9

RUN echo "Run Allows us to run arbirary commands that determine how to install libraries"
RUN pip install --upgrade pip

# RUN echo "Docker also Caches commands so whenever you make changes you don't have to re-install libraries"

ENTRYPOINT [ "python"]
CMD ["--version"]