# Calc a md5 of the relevant data files 
function md5s()
{
    M1=`md5 -q csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv`
    M2=`md5 -q csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv`
    M3=`md5 -q csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv`
    echo "$M1 $M2 $M3"
}


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


# Calculate charts
export DEBUG_LEVEL="INFO"
python3 basic_numbers.py
python3 rates.py
python3 offsets.py
python3 daily_changes.py
python3 ill.py
python3 opengraph_image.py

# Create page
cd gatsby
gatsby clean
npm run deploy
cd ..

DATE=`date "+%Y-%m-%d-%H"`
TAG="data-update_$DATE"
git tag "$TAG"
git push --tags

# Bring new charts to git
git add charts/**/*.png
git commit -m "Updated data"
git push
