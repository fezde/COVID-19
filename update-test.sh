#! /bin/bash

# Calc a md5 of the relevant data files 
function md5s()
{
    M1=`$MD5_CMD -q csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv`
    M2=`$MD5_CMD -q csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv`
    M3=`$MD5_CMD -q csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv`
    echo "$M1 $M2 $M3"
}

MD5_CMD="thisshouldfail"
if ! [ -x "$(command -v md5)" ]; then
    if ! [ -x "$(command -v md5sum)" ]; then
        echo 'Error: could not detect md5 or md5sum on the system' >&2
        exit 1
    else
        MD5_CMD="md5sum"
    fi
else
    MD5_CMD="md5"
fi

# Get checksums before the git pull
MD_BEFORE=$(md5s)

# Update data from the original data source
# https://github.com/CSSEGISandData/COVID-19
git pull --no-edit upstream master
git merge --strategy-option ours -F README.md
git add README.md

# Get checksums after the git pull
MD_AFTER=$(md5s)
if [ "$MD_BEFORE" == "$MD_AFTER" ]; then
    if [ "$1" != "--force" ]; then
        echo "Files have not chaged. Nothing to do here"
        exit 0
    fi
fi

make all

# DATE=`date "+%Y-%m-%d-%H"`
# TAG="data-update_$DATE"
# git tag "$TAG"
# git push --tags

# # Bring new charts to git
# git add charts/**/*.png
# git add charts/**/*.gif
# git commit -m "Updated data"
# git push
