# Airflow2_Docker
Simple steps to setup airflow2 using docker .

Step 1 :  Install Docker 
 
Step 2 :  check docker compose is installed using docker-compose -v in windows power shell.(if not install docker compose seperately)
 
Step 3 :  Download the yaml file for airflow :https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml
 
Step 4 :  create a new folder in windows machine ( eg named airflow)
 
Step 5 :  inside the folder place the docker-compose.yaml file .
 
Step 6 :  open microsoft power shell , naviagate to airflow folder and run 'docker config' command to check docker compose file is proper
 
Step 7 :  Once confirming run docker-compose up and enter (command to bring up docker image )
 
Step 8 :  Once image is created succesfully ,in chrome check the localhost:8080/ where the airflow server will be up and running .
![image](https://user-images.githubusercontent.com/83544534/119598447-97251780-be00-11eb-80ce-16a8b140cd87.png)

 
Step 9 :  In the airflow diectory you can see three more subdriectories will be created with the name dags, plugins , logs.
 
Step 10 :  Attached is the sample dag (first_dag.py) place this code inside dags directory ,Once placed this will create a new dag (dag_id : my_dag) in airflow webserver .

![image](https://user-images.githubusercontent.com/83544534/119598628-ebc89280-be00-11eb-8e00-f4e526b1e56f.png)

 
Step 11 :  You can turn on the dag icon for the dag to run .

![image](https://user-images.githubusercontent.com/83544534/119598759-292d2000-be01-11eb-821b-9a64f341225d.png)

![image](https://user-images.githubusercontent.com/83544534/119598768-2d593d80-be01-11eb-8184-2291b4ccbcad.png)


Happy Learning !!!
