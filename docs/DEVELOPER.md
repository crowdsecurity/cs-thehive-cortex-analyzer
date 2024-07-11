![CrowdSec Logo](images/logo_crowdsec.png)
# TheHive/Cortex CrowdSec analyzer

## Developer guide

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Local installation](#local-installation)
  - [Prepare local environment](#prepare-local-environment)
  - [Start Docker environment](#start-docker-environment)
  - [Stop Docker environment](#stop-docker-environment)
- [Manual test in UI](#manual-test-in-ui)
  - [Cortex Api key](#cortex-api-key)
  - [Enable the analyzer](#enable-the-analyzer)
  - [Set the report template](#set-the-report-template)
  - [Test and analyze an observable](#test-and-analyze-an-observable)
- [Manual test with Python](#manual-test-with-python)
  - [Set a virtual environment](#set-a-virtual-environment)
  - [Create a test input](#create-a-test-input)
  - [Run and debug the analyzer](#run-and-debug-the-analyzer)
- [Update documentation table of contents](#update-documentation-table-of-contents)
- [TheHive/Cortex Pull Request](#thehivecortex-pull-request)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Local installation



### Prepare local environment

The final structure of the project will look like below.

```markdown
crowdsec-thehive-cortex (choose the name you want for this folder)
│       
│
└───Cortex-Analyzers (do not change this folder name; Only needed for TheHive/Cortex Pull Request process)
│   │
│   │ (Fork of https://github.com/TheHive-Project/Cortex-Analyzers)
│
└───cs-thehive-cortex-analyzer (do not change this folder name)
    │   
    │ (Clone of this repo)

```

- Create an empty folder that will contain all necessary sources:
```bash
mkdir crowdsec-thehive-cortex && cd crowdsec-thehive-cortex
```

- Clone the fork of Cortex-Analyzers repository:

```bash
git clone git@github.com:some-fork/Cortex-Analyzers.git
```

- Clone this repository:

``` bash
git clone git@github.com:crowdsecurity/cs-thehive-cortex-analyzer.git
```

### Start Docker environment

#### Prepare `docker/.env`

Create a `.env` file in the `docker` folder, copy the content of the `.env.example` file 
and update the `ChangeMe` values. 
For the first run, you don't need to fill the `CORTEX_KEY` value (see below for more information).

```
cd docker && docker-compose up -d --build
```

Once all the containers have been started, you need to wait a few minutes for TheHive platform to be fully operational.
You can check that all operation are done with the following command:

```bash
docker logs -f -n50 docker-thehive-1
```

(The name of container may vary, and you can find it by running the `docker ps` command)


### Stop Docker environment

To stop all containers: 

```bash
docker-compose down
```

To stop all containers and remove all data (if you want to come back to a fresh TheHive/Cortex installation): 

```
docker-compose down -v
```

## Manual test in UI

To be able to manually test the CrowdSec analyzer, you need to create users and organisation with sufficient permissions.
This can be done with following steps:

### Cortex Api key

- Browse to Cortex: http://localhost:9001.
- Update database and create an admin login.
- Log in with the admin account.
- Create an organisation.
- Create a user for this organisation with read, analyse and orgadmin rights. Don't forget to edit/save password for this user.
- Create API key for this user and copy the key in `CORTEX_KEY` value of the `docker/.env` file

- Restart the docker environment:

```bash
docker compose down && docker compose up -d
```

### Enable the analyzer

- Browse to TheHive: http://localhost:9000.
- Log in with the default admin account (username: `admin@thehive.local`, password: `secret`).
- Create a CrowdSec organisation.
- Create a user for this organisation with orgadmin profile. Don't forget to edit/save password for this user.
- Logout and login with the new user account.
- Browse to http://localhost:9001/index.html#!/admin/organizations/CrowdSec
- Open the Analyzers tab
- You should see CrowdSec_Analyzer_X_Y: Enable it and copy your CTI key

### Set the report template

- Log out and log in with the default admin account
- Browse to http://localhost:9000/administration/entities/analyzer-templates
- You should be able to edit the CrowdSec_Analyzer_X_Y template: Copy /paste the content of `thehyve-template/Crowdsec_X_Y/long.html`

### Test and analyze an observable

- Log out and log in to The Hive with the user account you created for the CrowdSec organisation
- On the top right menu, you should see a `CREATE CASE +` button
- Create a case with an observable (e.g. an IP address like `1.2.3.4`)
- Click `...` then `Run Analyzers` and select the CrowdSec analyzer
- Wait until job run: then preview and click on the Last analysis date: you should see thr report with the good template


## Manual test with Python

### Set a virtual environment

```bash
cd src/analyzer/Crowdsec
virtualenv env
source ./env/bin/activate
pip install -r requirements.txt
```

### Create a test input

See https://thehive-project.github.io/Cortex-Analyzers/dev_guides/how-to-test-an-analyzer/

Create a file `input/input.json` with the following content:

```json
{
    "data": "1.2.3.4",
    "tlp": 0,
    "parameters": {},
    "dataType": "ip",
    "config": {
        "jobTimeout": 30,
        "service": "",
        "url": "",
        "api_key": "YOUR_CROWDSEC_CTI_KEY",
        "proxy_http": "",
        "proxy": {
            "http": "",
            "https": ""
        },
        "max_tlp": 2,
        "max_pap": 2,
        "check_tlp": true,
        "check_pap": true,
        "proxy_https": "",
        "cacerts": "",
        "auto_extract_artifacts": false,
        "jobCache": 10
    },
    "pap": 2,
    "message": "1"
    }
```

### Run and debug the analyzer

Run the analyzer:

```bash
python3 crowdsec_analyzer.py .
```

You should see the result in the `output` folder.

Depending on your IDE, it should be straightforward to set breakpoints and debug the analyzer. 


## Update documentation table of contents

To update the table of contents in the documentation, you can use [the `doctoc` tool](https://github.com/thlorenz/doctoc).

First, install it:

```bash
npm install -g doctoc
```

Then, run it in the documentation folder:

```bash
doctoc docs/*
```



## TheHive/Cortex Pull Request

@TODO




 
