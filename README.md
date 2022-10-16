# elrond-sdk-erdpy-eggs

Experimental: highly modularized erdpy (to be first used on PyChain tutorials).

## Create virtual environment

```
rm -rf ~/erdpy-sandbox
python3 -m venv ~/erdpy-sandbox
source ~/erdpy-sandbox/bin/activate
export PYTHONPATH=""
pip install pip -U
```

## Installing modules

```
python -m pip install "git+ssh://git@github.com/ElrondNetwork/elrond-sdk-erdpy-eggs.git@init#egg=erdpy_accounts&subdirectory=accounts" --upgrade

python -m pip install "git+ssh://git@github.com/ElrondNetwork/elrond-sdk-erdpy-eggs.git@init#egg=erdpy_network&subdirectory=network" --upgrade
```

References:
 - https://pip.pypa.io/en/stable/cli/pip_install/#vcs-support
