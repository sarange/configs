#!/bin/bash

if [[ $(uptime -p) == *"hour"* ]]
then
	echo $(uptime -p | cut -d ' ' -f 2)h $(uptime -p | cut -d ' ' -f 4)m
else
	echo $(uptime -p | cut -d ' ' -f 2)m
fi