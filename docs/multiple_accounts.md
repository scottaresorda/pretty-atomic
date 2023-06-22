Multiple accounts are now supported. There are a variety of ways to update your config with new accounts:

1. setup.py - simple
1. setup.py - command line
1. Manual

First a brief note on porting your old config.

### Porting old config
If you were using the old config, i.e `config.json`, you will need to first run `python setup.py` one time to port over your account details to the new JSON format.

The new file will be called `config_multiple_accounts.json`.

**Please note**: Credentials will no longer be base64 encoded, as base64 provides a false sense of security.

## Adding accounts
### 1) Setup.py - simple way
After you have ported over your account, do the following:
1. run `python setup.py`
2. Enter your account(s) per the onscreen prompt
3. If you want to configure a proxy, enter the proxy host you want to user for this specific MS account, if you leave the field blank the shell skips next parameters otherwise it asks also port, proxy username and proxy password (if your proxy need authentication)

### 2) Setup.py - command line arguments
Please note that this method will save your passwords to your `bash history`.

However, it can be useful if you need to set-up/run the entire process programmatically, i.e via Docker.

To add Microsoft accounts:
`python setup.py -e account1 account2 -p 'pw1' 'pw2'`

To add Microsoft accounts and proxy:
`python setup.py -e account1 account2 -p 'pw1' 'pw2' --proxy_host '1.2.3.4' '5.6.7.8' --proxy_post '1234' '5678' --proxy_username 'pxuser1' 'pxuser2' --proxy_password 'pxpwd1' 'pxpwd2'`

To add/update reporting:
`python setup.py -d <discord_webhook_url>`

### 3) Manual way
Assuming you have the new config file created already, i.e `config/config_multiple_accounts.json`, you can manually add new accounts to the config file.

This is a good option for those comfortable with JSON syntax.

### Deleting accounts
You must do this manually, `setup.py` is append-only.

## Disclaimer
Your accounts are more likely to be **banned** if you do this. Especially if you redeem multiple accounts with the **same phone number**.

You have been warned.


