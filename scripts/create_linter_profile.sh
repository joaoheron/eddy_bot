#!/bin/bash
mkdir -p ~/.config
rm -f ~/.config/flake8
printf "[flake8]\ncount = True\nignore = E121,E122,E126,E128,E201,E202,E203,E211,E261,E302,E305,E501,W1,W4,W5,W6\nstatistics = True" >> ~/.config/flake8
