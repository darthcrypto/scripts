#find files in current running directory older than 365 days and delete them

find . -type f -name *.wsp -mtime +365 -exec rm {} \;
