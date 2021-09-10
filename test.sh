#!/bin/bash

GIT_TAG=$(echo $(git describe --tags --abbrev=0))
# git checkout -b $GIT_TAG
TAG_SOURCE_BRANCH=$(echo $(git branch --contains tags/$GIT_TAG))
echo $TAG_SOURCE_BRANCH
if [[ "$TAG_SOURCE_BRANCH" == *"$master"* ]]; then
  echo "It's there."
else
  echo "Not there"
fi
# git checkout master