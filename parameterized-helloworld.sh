#!/bin/bash


verbose='false'
puppetrole=''
release=''

while getopts 'p:r:v' flag; do
  case "${flag}" in
    p) puppetrole="${OPTARG}" ;;
    r) release="${OPTARG}" ;;
    v) verbose='true' ;;
    *) error "Unexpected option ${flag}" ;;
  esac
done

if [[ -z $puppetrole ]] || [[ -z $release ]]
then
        echo -e "\n !!! ERROR: At least one parameter not specified !!!
 Usage: updateReleaseTags.sh -p puppetrole -r release \n"
        exit 1
fi

echo "one parameter is ${puppetrole} and the other is ${release}"
