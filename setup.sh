#!/bin/bash

mkdir "advent"

for i in $(seq -w 01 25); do
  mkdir "advent/$i"
  touch "advent/$i/$i.py"
  touch "advent/$i/$i.md"
done