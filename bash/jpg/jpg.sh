tmpforgrep=$(echo $1 | sed "s/res\/[0-9]*\.html$//")
#echo $tmpforgrep
curl -s $1 | grep -o "image_url=${tmpforgrep}src/[0-9]*/[0-9]*.jpg" | sed "s/image\_url\=//" > t.txt
mkdir download
boardname=$(echo $tmpforgrep | sed "s/https\:\/\/2ch\.hk\///" | sed "s/\/$//")
#echo $boardname
for file in $(cat t.txt)
do
    cd download
    file1=$(echo $file | sed "s/^https\:\/\/2ch\.hk\/${boardname}\/src\/[0-9]*\///")
    curl -s $file -o $file1
    cd ..
done
rm t.txt