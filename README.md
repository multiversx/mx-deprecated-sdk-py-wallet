# elrond-sdk-erdpy-eggs

Experimental: highly modularized erdpy (to be first used on PyChain tutorials).

## Create virtual environment

```
python3 -m venv ./sandbox
source ./sandbox/bin/activate
pip install pip -U
```

## Installing modules

```
python -m pip install -e "git+ssh://git@github.com/ElrondNetwork/elrond-sdk-erdpy-eggs.git@init#egg=erdpy_accounts&subdirectory=erdpy_accounts" --upgrade
```

References:
 - https://pip.pypa.io/en/stable/cli/pip_install/#vcs-support
