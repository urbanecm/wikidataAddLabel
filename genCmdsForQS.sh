#!/bin/bash

sql wikidatawiki < sql | sed 1d | sed "s/^/echo -e \'/g" | sed "s/$/\'/g" | bash > cmds.txt
