# Web-GPU-Monitor

Simple server monitoring for your GPU cluster.
Periodically calls `nvidia-smi` through SSH and parses it into a website.

## Setup

You need to satisfy some Python dependencies.

```
conda env create -f environment.yml
```

## Getting Started

First step is to create a `config.ini` where your credentials and hostnames are specified.

An example could look like this:

```
[common]
user = yourusername
hosts = host1.domain.tld,host2.domain.tld
```

Save this as `config.ini`.

Now you can run `python fetch_data -c config.ini` to fetch data from
your specified hosts. The result is then saved in `load_data.csv`.
Call `python render_website.py` to create a HTML site out of it.
The result is stored in `output/index.html`.

## Automation

Of course, you want to host this on a webserver and it should automatically
update the website. A simple cronjob does this job very nicely.
