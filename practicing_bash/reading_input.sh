echo -e "What's your name?"
read name
echo -e "Hello $name"
echo "what's your fav colors?"
read -a colors
echo "Great choice about : " ${colors[0]} ${colors[1]} 

