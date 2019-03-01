#!/bin/bash
aws s3 sync ./public s3://findmyfood.webhost/
echo Your deployed content is here: https://findmyfood.webhost.s3-website-us-east-1.amazonaws.com