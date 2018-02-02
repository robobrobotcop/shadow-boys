A script that posts a notification to your choice of slack channel using webhook whenever a new excel file for 'små partier' is available on systembolaget.se.

- Create a webhook on your slack integrations page, paste it into the `config-sample.py` file.

- Change name on the `config-sample.py` file to just `config.py`

- Uses GET requests so it needs to be set up with cronjob.
