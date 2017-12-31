#!/bin/bash

###INSTRUCTIONS###
# downtime-end.sh is used for ending downtime for nodes in datadog
# it takes 2 arguments: tag and tag-value
#EXAMPLE:
# if you wanted to end downtime for all nodes tagged with the puppet_role rct
# downtime-end.sh -t puppet_role -v rct

#parameters
verbose='false'
tag=''
value=''

while getopts 't:v:z' flag; do
  case "${flag}" in
    t) tag="${OPTARG}" ;;
    v) value="${OPTARG}" ;;
    z) verbose='true' ;;
    *) error "Unexpected option ${flag}" ;;
  esac
done

#parameter error handling
if [[ -z $tag ]] || [[ -z $value ]]
then
        echo -e "\n !!! ERROR: At least one parameter not specified !!!
 Usage: downtime-end.sh -t tag -v value \n"
        exit 1
fi

#datadog keys
api_key="71ab1488cdc9e808c2f8bcca940ca154"
app_key="4777281b7ce988e619c66691b651d3e3b26b4b06"

#end downtime
curl -X POST -H "Content-type: application/json" -H "Accept: application/json" \
-d "{
      \"scope\": \"$tag:$value\"
   }" \
   "https://app.datadoghq.com/api/v1/downtime/cancel/by_scope?api_key=${api_key}&application_key=${app_key}"

if [ $? -ne 0 ]; then
    echo "ERROR: Downtime did not end successfully for nodes in DataDog with the tag:value of $tag:$value"
else
    echo "SUCCESS: Downtime has ended for nodes in DataDog with the tag:value of $tag:$value"
fi
