# Gigger-Webserver
Gigger's Django based web server has now been open sourced, enabling anyone to contribute to the music industry's search engine.

Gigger's ultimate goal is to revolutionise live music such that it provides musicians a primary career with good pay.

We believe:
* In empowering the underdog first
* Musicians deserve to make a career from their art.
* Musicians need local venues to grow their careers
* Live music is vital to a society’s social cohesion

This means that if anyone wants to contribute features that could help Gigger empower independent musicians then code it up and submit a pull request. Anything that makes it to master will go live at https://www.gigger.rocks/.

## Gigger's database
Being a search engine, Gigger has access to a database of over 250,000 bands and venues whose data has been crawled from publicly available sources such as Facebook, Soundcloud and Bandcamp. This data is available both via `main.models` and api calls to https://api.gigger.rocks. The next step will be to open source this API, and/or rewrite it Django REST Framework. Currently the crawler itself is private.

Database is currently MySQL although I have been considering migrating to Postgres for more control over fulltext search vectors.

## Tech Stack
The server runs on AWS Lambda and API Gateway thanks to [Zappa](https://github.com/Miserlou/Zappa). This means that the server is entirely stateless, all state is maintained in the database. Additionally, this means that the web server itself does not support file uploads directly. However, uploading to s3 and triggering some processing via AWS Lambda or similar is a better design pattern anyway.

**Due to use of Zappa, up to date requirements are located in `requirements-zappa.txt` and `.ebextensions` is unused.**

## Costs
All costs are currently absorbed by Gigger itself, which is a Proprietary Limited company registered in Australia, however it is donationware and funded entirely by the project maintainer.

## Contribution
Please feel free to submit pull requests - there are so many things Gigger could do, all it needs is love and attention.
