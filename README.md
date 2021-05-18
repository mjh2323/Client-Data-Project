## Client Data App (Python)

## Installation 

Fork this repository, clone or download it to your desktop, then navigate here via the command-line.

```sh
cd ~/Desktop/Client_Data_Project
```

Next, activate the new environment. 

```sh
conda create -n project.env
conda activate project.env
```

Then, within the enviornment, install the package requirements. 
```sh
pip install -r requirements.txt
```

Follow the SendGrid setup instructions to sign up for a SendGrid account, configure your account's email address (i.e. SENDER_EMAIL_ADDRESS), and obtain an API key (i.e. SENDGRID_API_KEY).

Create a new file called ".env" in the root directory of this repo, and paste the following contents inside, using your own values as appropriate:

```sh
# these are example contents for the ".env" file:

# required vars:
SENDGRID_API_KEY="_______________"
SENDER_EMAIL_ADDRESS="_______________"

# optional vars:
#APP_ENV="development"
#COUNTRY_CODE="US"
#ZIP_CODE="10017"
#USER_NAME="Jon Snow"
```