#!/bin/bash

## Parse input ##
NAME=$1
BASE=$2
DOCKERFILE=$3

# Determine if we are using private images
# if [ ${USE_PRIVATE_IMAGES} -eq 1 ]; then
#   BASE=${BASE}-private
# fi

## Build/Push image to cache endpoint by pipeline ID ##
  # --build-arg BASE_TAG="${BASE_TAG}" \
docker build \
  -t kasmcustom/${NAME}:dev \
  --build-arg BASE_IMAGE="${BASE}" \
  -f ${DOCKERFILE} .
