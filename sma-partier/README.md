A script that posts a notification to your choice of slack channel using webhook whenever a new excel file for 'små partier' is available on systembolaget.se.

- Copy the `config-sample.py` file and name it `config.py`

- Create a webhook on your slack integrations page, paste it into the `config.py` file.

- Uses GET requests so it needs to be set up with cronjob (fyi, on the first run all previous dates will be posted to slack).
