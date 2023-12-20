FROM selenium/standalone-chrome

USER root

RUN sudo apt-get update
RUN sudo apt-get install -y python3
RUN sudo apt-get install -y python3-pip

WORKDIR /var/jenkins_home/workspace/pythongirlpower/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8866

CMD ["pytest", "-v", "-s", "--alluredir=allure-results", "--capture=no", "--log-cli-level=INFO", "./tests/."]

