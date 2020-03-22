
#!/bin/bash

> oldFiles.txt

FILES=$(grep "jane " ../data/list.txt | cut -d' ' -f3)

for i in $FILES
do
        if [ -e .."$i" ];then
                echo .."$i" >> oldFiles.txt
        fi
done
