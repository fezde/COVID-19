#! /bin/bash
DOWN_BASE_URL=https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/
DATA_DIR=csse_covid_19_data/csse_covid_19_time_series/


# Calc a md5 of the relevant data files 
function md5s()
{
    M1=`md5 -q "${DATA_DIR}time_series_covid19_confirmed_global.csv"`
    M2=`md5 -q "${DATA_DIR}time_series_covid19_deaths_global.csv"`
    M3=`md5 -q "${DATA_DIR}time_series_covid19_recovered_global.csv"`
    echo "$M1 $M2 $M3"
}


# Get checksums before the git pull
MD_BEFORE=$(md5s)

# Update data from the original data source
# https://github.com/CSSEGISandData/COVID-19

DOWN_FILE=time_series_covid19_confirmed_global.csv
curl -s "${DOWN_BASE_URL}${DOWN_FILE}" --output "${DATA_DIR}${DOWN_FILE}"
DOWN_FILE=time_series_covid19_deaths_global.csv
curl -s "${DOWN_BASE_URL}${DOWN_FILE}" --output "${DATA_DIR}${DOWN_FILE}"
DOWN_FILE=time_series_covid19_recovered_global.csv
curl -s "${DOWN_BASE_URL}${DOWN_FILE}" --output "${DATA_DIR}${DOWN_FILE}"

# Get checksums after the git pull
MD_AFTER=$(md5s)
if [ "$MD_BEFORE" == "$MD_AFTER" ]; then
    if [ "$1" != "--force" ]; then
        echo "Files have not chaged. Nothing to do here"
        exit 0
    fi
fi

git add "${DATA_DIR}/*"
git commit -m "Updated data from original data repository"

make all

exit

DATE=`date "+%Y-%m-%d-%H"`
TAG="data-update_$DATE"
git tag "$TAG"
git push --tags

# Bring new charts to git
git add charts/**/*.png
git add charts/**/*.gif
git commit -m "Updated data"
git push
