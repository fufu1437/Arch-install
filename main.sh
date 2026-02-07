#!/bin/base

test_num=0

ping -c 2 baidu.com
if [ $? -ne 0 ]; then
    test_num=$((test_num + 1))
    ping -c 2 baidu.com

    if [ $? -ne 0 ]; then
        echo "No internet"
    fi
fi


