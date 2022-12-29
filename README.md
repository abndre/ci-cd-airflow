# CI-CD airflow

In this repository have a git-hub actions ci-cd to check if airflow is read to prod.
Only check if airflow up without problem. Not check dags contends.

## Steps

- First is installed a airflow 
- Second is copy all files in ./dag folder to ./dag folder of airflow
- Third check if have any problem

The otivation for this project is because in my work some the team up new dags, and the server broken.
