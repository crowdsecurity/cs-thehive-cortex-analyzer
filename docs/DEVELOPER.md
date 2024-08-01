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
- [Unit tests](#unit-tests)
- [Update documentation table of contents](#update-documentation-table-of-contents)
- [TheHive/Cortex Pull Request](#thehivecortex-pull-request)
  - [Sync fork with upstream](#sync-fork-with-upstream)
  - [Update fork sources](#update-fork-sources)
  - [During the pull request review](#during-the-pull-request-review)
  - [Once pull request is merged](#once-pull-request-is-merged)

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
│   │ (Clone of https://github.com/crowdsecurity/Cortex-Analyzers)
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
git clone git@github.com:crowdsecurity/Cortex-Analyzers.git
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
cd docker && docker compose up -d --build
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
docker compose down
```

To stop all containers and remove all data (if you want to come back to a fresh TheHive/Cortex installation): 

```
docker compose down -v
```

## Manual test in UI

To be able to manually test the CrowdSec analyzer, you need to create users and organization with sufficient permissions.
This can be done with following steps:

### Cortex Api key

- Browse to Cortex: http://localhost:9001.
- Update database and create an admin login.
- Log in with the admin account.
- Create an organization.
- Create a user for this organization with read, analyse and orgadmin rights. Don't forget to edit/save password for this user.
- Create API key for this user and copy the key in `CORTEX_KEY` value of the `docker/.env` file

- Restart the docker environment:

```bash
docker compose down && docker compose up -d
```

### Enable the analyzer

- Browse to TheHive: http://localhost:9000.
- Log in with the default admin account (username: `admin@thehive.local`, password: `secret`).
- Create a CrowdSec organization.
- Create a user for this organization with orgadmin profile. Don't forget to edit/save password for this user.
- Logout and login with the new user account.
- Browse to http://localhost:9001/index.html#!/admin/organizations/CrowdSec
- Open the Analyzers tab
- You should see CrowdSec_Analyzer_X_Y: Enable it and copy your CTI key

### Set the report template

- Log out and log in with the default admin account
- Browse to http://localhost:9000/administration/entities/analyzer-templates
- You should be able to edit the CrowdSec_Analyzer_X_Y template: Copy /paste the content of `thehyve-template/Crowdsec_X_Y/long.html`

### Test and analyze an observable

- Log out and log in to The Hive with the user account you created for the CrowdSec organization
- On the top right menu, you should see a `CREATE CASE +` button
- Create a case with an observable (e.g. an IP address like `1.2.3.4`)
- Click `...` then `Run Analyzers` and select the CrowdSec analyzer
- Wait until job run: then preview and click on the Last analysis date: you should see thr report with the good template


## Manual test with Python

### Set a virtual environment

```bash
cd crowdsec-thehive-cortex/cs-thehive-cortex-analyzer
virtualenv env
source ./env/bin/activate
pip install -r tests/requirements.txt
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
cd src/analyzer/Crowdsec
python3 crowdsec_analyzer.py .
```

You should see the result in the `output` folder.

Depending on your IDE, it should be straightforward to set breakpoints and debug the analyzer. 


## Unit tests

First, prepare your virtual environment:

```bash
source src/env/bin/activate
python -m pip install --upgrade pip
python -m pip install -r tests/requirements.txt
```

Then, run tests: 

```bash
python -m pytest -v
```

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

To make an update publicly available, we need to submit a pull request to the [Cortex Analyzers repository](https://github.com/TheHive-Project/Cortex-Analyzers), 
and to submit a pull request, we use the [CrowdSec fork](https://github.com/crowdsecurity/Cortex-Analyzers).

### Sync fork with upstream

Before modifying the code of our fork, we need to sync it from the upstream repo. There are many way to do it. Below is what you can do locally.

Using your local connectors folder defined [above](#prepare-local-environment), you should define two Git remote: origin (the fork) and upstream (the Cortex Analyzer repo).
You can check that with the following command: 

```shell
cd Cortex-Analyzers
git remote -v
```

You should see the following result:

```
origin	git@github.com:crowdsecurity/Cortex-Analyzers.git (fetch)
origin	git@github.com:crowdsecurity/Cortex-Analyzers.git (push)
upstream	git@github.com:TheHive-Project/Cortex-Analyzers.git (fetch)
upstream	git@github.com:TheHive-Project/Cortex-Analyzers.git (push)
```



Once you have this, you can force update the fork develop branch :

```shell
git checkout develop
git fetch upstream
git reset --hard upstream/develop
git push origin develop --force 
```

### Update fork sources

#### Create a release

Before creating a release, ensure to format correctly the `CHANGELOG.md` file and to update all necessary code related to the version number:
`src/analyzer/Crowdsec/crowdsec_api.py`, `src/analyzer/Crowdsec/Crowdsec_analyzer.json`, `src/thehive-template/Crowdsec_X_Y`

Then, you can use the [Create Release action](https://github.com/crowdsecurity/cs-thehive-cortex-analyzer/actions/workflows/release.yml).

#### Retrieve zip for release

At the end of the Create Release action run, you can download a zip containing the relevant files.  

#### Create a branch for the Pull Request

If your release is `vX.Y.Z`, you can create a `feat/release-X-Y-Z` branch:

```shell
cd Cortex-Analyzers
git checkout develop
git checkout -b feat/release-X-Y-Z
```

#### Update sources

Before all, remove all files related to CrowdSec:

```shell
cd Cortex-Analyzers
rm -rf analyzers/Crowdsec/* thehive-templates/Crowdsec_*
```

Then, unzip the `crowdsec-thehive-cortex-analyzer-X.Y.Z.zip` archive and copy files in the right folders:
- `src/analyzer/Crowdsec` -> `analyzers/Crowdsec`
- `src/thehive-template/Crowdsec_X_Y` -> `thehive-templates/Crowdsec_X_Y`


Now, you can verify the diff.

Once all seems fine, add and commit your modifications:

```shell
git add .
git commit -m "[crowdsec] Update analyzer (vX.Y.Z)"
```

#### Test locally before pull request 

You can test with the docker local stack by modifying the `docker/docker-compose.yml` file:
Change

```
  cortex:
    ...
    volumes:
      ...
      - ../src/analyzer:/opt/cortex/analyzers
```

to 

```
  cortex:
    ...
    volumes:
      ...
      - ../../Cortex-Analyzers/analyzers:/opt/cortex/analyzers
```


#### Open a Pull request

Push your modification 

```shell
git push origin feat/release-X.Y.Z
```

Now you can use the `feat/release-X.Y.Z` branch to open a pull request in the Cortex Analyzer repository.
For the pull request description, you could use the release version description that you wrote in the `CHANGELOG.md` file.



### During the pull request review

As long as the pull request is in review state, we should not create a new release. 
If there are modifications to do, we can do it directly on the `feat/release-X.Y.Z`. 
All changes made to pass the pull request review must be back ported to a `feat/pr-review-X-Y-Z` branch created in this repository:

```shell
cd cs-thehive-cortex-analyzer
git checkout main
git checkout -b feat/pr-review-X.Y.Z
```

### Once pull request is merged

If pull request has been merged without any modification, there is nothing more to do.

If there were modifications, we need to update the sources anc create a patch release.

#### Sync fork with upstream

First, sync the connector fork like we did [here](#sync-fork-with-upstream). 

#### Retrieve last version

After this, you should have the last version of the CrowdSec analyzer in `analyzers/Crowdsec` and `thehive-templates/Crowdsec_X_Y` folders.

You need to retrieve it and commit the differences.

```shell
cd cs-thehive-cortex-analyzer
git checkout feat/pr-review-X.Y.Z
```

Delete `src/analyzer/Crowdsec` and `src/thehive-template/Crowdsec_X_Y` folder content.

Copy all files from the analyzers fork: 

```
cp -r ../Cortex-Analyzers/analyzers/Crowdsec/. ./src/analyzer/Crowdsec
cp -r ../Cortex-Analyzers/thehive-templates/Crowdsec_X_Y/. ./src/thehive-template/Crowdsec_X_Y
```

Add and commit the result. Push the `feat/pr-review-X-Y-Z` and merge it into `main` with a pull request.


#### Create a new minor release

Once the `main` branch is updated, you can create a new minor `X.Y.Z+1` release with the following CHANGELOG content:

```
## Changed

- Synchronize content with Cortex Analyzer release [A.B.C](https://github.com/TheHive-Project/Cortex-Analyzers/releases/tag/A.B.C)

```






 
