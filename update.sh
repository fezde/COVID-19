# update data from the original data source
# https://github.com/CSSEGISandData/COVID-19

git pull --no-edit upstream master

python3 basic_numbers.py
python3 rates.py

git add **/*.png
git commit -m "Updated data"
git push