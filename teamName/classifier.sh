#!/bin/bash

if python ./dummy.py $1
 then exit 0 # Real
 else exit 1 # Fake
fi
