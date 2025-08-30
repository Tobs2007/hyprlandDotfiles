curl -s 'https://api.nasa.gov/planetary/apod?api_key='$nasaApiKey |jq -r '.url' |xargs -n1 curl -so image.jpg
