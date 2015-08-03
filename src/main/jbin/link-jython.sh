#!/bin/bash


for x in `cd ../jython/bin ; ls` ; do
    ln -s ../jython/bin/$x $x
done ;

