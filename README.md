# ytb2moodle
Converter dari youtube playlist menjadi course moodle.
Ini adalah aplikasi flask, untuk di webserver, tapi bisa di ikuti alurnya, kalau ingin menjadi skrip biasa gunakan makecourse.py

## file api.yaml
isinya adalah api key dari google Youtube API Data v3
hanya perlu key api. tidak perlu oAuth.

isinya seperti ini
api_key: 'blabla3blablablabla'

# Install local

git clone https://github.com/irzaip/ytb2moodle 

buat file api.yaml dengan isi api_key: 'blablablabla'

flask run


# Deploy to heroku

Pertama harus sudah install heroku-cli dan buat account di heroku.

git clone https://github.com/irzaip/ytb2moodle

buat file api.yaml dengan isi api_key: 'blablablabla'  

pipenv install -r requirements
pipenv shell
git init
git add
git commit -m "First commit"
heroku login
heroku create ytb2moodle
git push heroku master




