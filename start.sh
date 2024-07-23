if [ -z $SOURCE_CODE ]
then
  echo "Cloning main Repository"
  git clone https://github.com/kevinnadar22/URL-Shortener-V2.git /URL-Shortener-V2
else
  echo "Cloning Custom Repo from $SOURCE_CODE "
  git clone $SOURCE_CODE /AlphaShortBot
fi
cd /AlphaShortBot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
