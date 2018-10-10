A script that fetches information from Lauris Graphql API about your MTG card selling progress and posts it to Slack. 

- Copy and rename the `mtg_card_sale_config_sample.json` file to `mtg_card_sale_config.json`
- Input info in the file, `usr`, `pwd` and `url` you'll get from Lauri if you use him to sell your MTG cards. Create a Slack webhook to the channel you want to receive the info. 
- Run daily with cronjob.
