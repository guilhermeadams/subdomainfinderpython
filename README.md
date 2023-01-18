Subdomain Takeover Scanner 🔍
==========================

A Python script that can be used to find subdomains, list the subdomains of a given domain, and check for subdomain takeover vulnerabilities. 🕵️‍♂️

Prerequisites 🛍
-------------

*   Python 3 🐍
*   requests 🌐
*   bs4 📜
*   json 📦
*   termcolor 🌈

Installation 🛠
------------

1.  Clone the repository

```bash
git clone https://github.com/guilhermeadams/subdomainfinderpython.git
```

2.  Install the required libraries
```bash
pip install -r requirements.txt
```
Usage 🚀
-----
```bash
python3 script.py domain.com
```
Example 💻
-------
```bash
python3 script.py example.com`
```
Output 📊
------

The script will list the subdomains of the provided domain and check if they are vulnerable to subdomain takeover. The output will be colored in the terminal.

Please be aware that using such tools might be against terms and conditions of some websites and could be illegal in some countries.

Note 📝
----

This script uses crt.sh website to get the subdomains, there are many other ways to find subdomains and check for subdomain takeovers, you can use different libraries and APIs. This script is a basic script, and it only checks for HTTP and HTTPS. Different services like AWS/Azure/Heroku etc have different ways to check, you can use different libraries and APIs to check for those services.
