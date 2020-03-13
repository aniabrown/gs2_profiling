#!/bin/bash

FIELD_TIME=$(cat $1 | grep "(field" | awk '{print $3 }')
ADVANCE_TIME=$(cat $1 | grep "Advance steps" | awk '{print $3 }')

echo ${FIELD_TIME}, ${ADVANCE_TIME}
