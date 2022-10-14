# elrond-sdk-erdpy-eggs

Experimental: highly modularized erdpy (to be first used on PyChain tutorials).

## Create virtual environment

```
python3 -m venv ./sandbox
source ./sandbox/bin/activate
```

## Installing modules

```
python -m pip install -e "git+ssh://git@github.com/ElrondNetwork/elrond-sdk-erdpy-eggs.git@init#egg=subdir&subdirectory=accounts"
```

References:
 - https://pip.pypa.io/en/stable/cli/pip_install/#vcs-support
