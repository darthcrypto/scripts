#!/bin/bash

#list all repos or i can build a list of repo links
REPOS="ssh://git@stash.dev.lotame.com:7999/per/panda-ui-deprecated.git ssh://git@stash.dev.lotame.com:7999/per/panda-ui.git"

#make directories for all repos, clone all repos and tags locally, remove old origin, create new origin, push repos and tags to new origin
for i in $REPOS; do
    mkdir -p /tmp/migrate-test/$i
    cd /tmp/migrate-test/$i
    git clone $i
    repodir=$(ls /tmp/migrate-test/$i)
    cd /tmp/migrate-test/$i/$repodir
    for BRANCH in $(git branch -a | grep remotes | grep -v HEAD | grep -v master); do 
 	       #git branch --track "${BRANCH#remotes/origin/}" "${BRANCH}"; 
               git checkout "${BRANCH#remotes/origin/}";   
    done
    git fetch --tags
    git remote rm origin
    ORIGIN_OLD=${i##ssh://git@stash}
    ORIGIN_NEW=ssh://git@stash-staging2$ORIGIN_OLD
    git remote add origin $ORIGIN_NEW
    git push origin --all
    git push --tags
done

################################## ADD ERROR HANDLING!!!  ########################
