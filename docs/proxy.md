# Proxy Instructions (Optional)

Before proceeding, please note:

- that the process is somewhat involved, it should take around 30 minutes to get everything set-up

If you would still like to proceed, here are the steps:

1. This program needs access to the `proxy_host` and `proxy_port`, and for authenticaded proxy it needs also `proxy_username` and `proxy_password`.
    - Re-run setup.py to update the config file:

    ```py
    python setup.py --proxy_host <your_proxy_host> --proxy_port <your_proxy_port> [--proxy_username <your_proxy_username> --proxy_password <your_proxy_password>]
    ```

    **Please note**: Your proxy credentials will be stored in plain text

2. To summarize, the end result of the above is the following:
    - `config/config.json` was updated via `setup.py` and now contains the following:
        - proxy_host
        - proxy_port
        - proxy_username (optional)
        - proxy_password (optional)
