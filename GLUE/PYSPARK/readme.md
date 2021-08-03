Linux / WSL Environment for local development:

Create a new virtual environment for the project.

python3 -m venv venv

Activating the virtualenv on Linux: From the project root, run: 

source venv/bin/activate


Run pip install -r requirements.txt from the PYSPARK directory.

If you run into the following:
Java not found and JAVA_HOME environment variable is not set.
Install Java and set JAVA_HOME to point to the Java installation directory.

sudo apt update
sudo apt install openjdk-8-jdk openjdk-8-jre

java -version

sudo su
cat >> /etc/environment <<EOL

Incluir o conteúdo
JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
JRE_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
EOL

Execute etl.py:
python etl.py