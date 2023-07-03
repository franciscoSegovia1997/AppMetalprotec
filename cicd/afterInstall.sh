sudo apt install -y python3-pip
sudo apt install -y virtualenv
sudo mkdir -pv /var/{log,run}/gunicorn/
sudo chown -cR ubuntu:ubuntu /var/{log,run}/gunicorn/
virtualenv /home/ubuntu/env
source /home/ubuntu/env/bin/activate
pip install -r /home/ubuntu/AppMetalprotec/requirements.txt
cd /home/ubuntu/AppMetalprotec/
gunicorn -c config/gunicorn/dev.py
python3 manage.py migrate
python3 manage.py collectstatic --no-input
sudo systemctl restart nginx