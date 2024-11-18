EBIRD_API_KEY="${EBIRD_API_KEY:-EBIRD_API_KEY}"

curl -s --location 'https://api.ebird.org/v2/product/spplist/TW' \
  --header "x-ebirdapitoken: ${EBIRD_API_KEY}" -o ./tw.json

curl -s --location 'https://siansiansu.github.io/ebird-data/json/species_joined.json' \
  -o ./species_joined.json

python ./main.py