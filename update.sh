# update data from the original data source
https://github.com/CSSEGISandData/COVID-19

git pull --no-edit upstream master

python3 basic_numbers.py
python3 rates.py
python3 offsets.py
python3 daily_changes.py

cd gatsby
gatsby clean
npm run deploy
cd ..

git add charts/**/*.png
git commit -m "Updated data"
git push
