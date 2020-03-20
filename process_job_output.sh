#!/bin/bash

FIELD_TIME=$(cat $1 | grep "(field" | awk '{print $3 }')
ADVANCE_TIME=$(cat $1 | grep "Advance steps" | awk '{print $3 }')
INIT_TIME=$(cat $1 | grep "Initialization" | awk '{print $2 }')

echo ${FIELD_TIME}, ${ADVANCE_TIME}, ${INIT_TIME}
