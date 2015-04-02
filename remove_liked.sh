access_token="30266858.767ac43.bdc6ed67d7e441c184fedc3bc5f1a808"
last_liked_mediaid="953763074500958794_538540229"

curl https://api.instagram.com/v1/users/self/media/liked?access_token=$access_token > read.txt

python get_liked.py $last_liked_mediaid

while read line
do
    echo -e "\nRemove liked media, MEDIA ID: $line\n"
    curl -X DELETE https://api.instagram.com/v1/media/$line/likes?access_token=$access_token
    echo 
    
done < "./write.txt"

echo -e "\n---------- done ----------\n"
