There are 2 ideas -
1. Communicate with AD and check the entitlement and user authorization - it requires code change, "stealth" deployment and involves risk
2. Replace the existing hard coded use config.py with valid users (once an hour or week is okay with business)

This needs to be done in about 4 business days with lack of important resources and thus option#2 is chosen

Once correct config.py exists, find out the docker container id that is running the flask application and use "docker cp config.py container_id:/CORRECTPATH/config.py" command to copy config file, no restart is required.
