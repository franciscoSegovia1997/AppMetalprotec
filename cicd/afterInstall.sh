sudo apt install -y python3-pip
sudo apt install -y virtualenv
sudo mkdir -pv /var/{log,run}/gunicorn/
sudo chown -cR ubuntu:ubuntu /var/{log,run}/gunicorn/
pip install -r /home/ubuntu/AppMetalprotec/requirements.txt
cd /home/ubuntu/AppMetalprotec/
gunicorn -c config/gunicorn/dev.py