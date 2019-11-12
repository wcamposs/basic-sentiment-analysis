# Installation:

To prepare your environment, I recommend install [Python3](https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/) and [Virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b) using your **Terminal**

PS: I recommend set Python3 as default:
```
alias python=python3
```

After install and set your alias, create your environment using:
```
virtualenv -p python3 environment-name
```

# Activating Environment:

To activate your environment, run:
```
source environment-name/bin/activate
```

# Installing necessary libs:

Once in the environment, run:
```
pip3 install nltk
pip3 install pandas
```

# Runing Application:

To run your application (via terminal), go to application folder and run:
```
python src.py
```
