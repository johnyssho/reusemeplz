#!/bin/bash

rsync -ravuP --delete reusemeplz/* prod/reusemeplz/

cat secret/key > prod/reusemeplz/reusemeplz/secret_key.txt

rm prod/reusemeplz/reusemeplz/settings.py

cp settings.py prod/reusemeplz/reusemeplz/settings.py

