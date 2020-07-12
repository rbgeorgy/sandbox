curl -s $1 | grep -o "image_url=https://2ch.hk/b/src/[0-9]*/[0-9]*.\(webm\|mp4\)" | sed "s/image_url=//" > videos_from_dvach.txt
mkdir downloads
for temp in $(cat videos_from_dvach.txt)
do 
    cd downloads
    temp2=$(echo $temp | sed "s/https\:\/\/2ch\.hk\/b\/src\/[0-9]*\///")
    curl $temp -o $temp2
    cd ..
done
rm videos_from_dvach.txt
vlc downloads
