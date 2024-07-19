# Wilbert Würfel
A simple discord bot written in python using the pycord library for the role-playing game DSA (The dark Eye).
Can easily be hosted using docker.

## Setup
Simply run the command to build the docker image:
```
docker build github.com/dominik1106/wilbert#main -t repository/name:version
```
Then start it using:
```
docker run -e BOT_TOKEN=$VALUE$ -d repository/name:version
```
Or create a `docker-compose.yml`.
You need to set the `BOT_TOKEN` enviroment variable to your discord bot token, either in the `docker-compose.yml` file or by passing the `-e` flag.

## Functions
Provides the following slash commands:
All results are ***not*** sorted.

`/r xdy` or `/r xwy` rolls `x` dice with `y` sides.

`/eigenschaft` rolls 1d20.

`/talent` rolls 3d20s.

`/attacke` rolls 2d20s, the first one is the attack roll, the second decides where the attack hits (if using the advanced zone system)
