<h1> Preparação, Orquestração e Fluxos de Dados (PUC-MG-2022) </h1>

<p style='text-align: justify;'> Trabalho final propsoto para a disciplina, utilizando conceitos adquiridos ao longo das aulas, submentendo stack de Engenheiro de Dados na AWS.</p>

<h2 > Estruturação do Projeto: </h2>

            PRE_AWS_Airflow
            .
            ├───.archives
            |    ├──── campeonato-brasileiro-cartoes.csv
            |    ├──── campeonato-brasileiro-estatisticas-full.csv
            |    ├──── campeonato-brasileiro-full.csv
            |    ├──── campeonato-brasileiro-gols.csv
            |    └──── Legenda.txt
            |
            ├───.dags
            |    └──── campeonato_dag.py
            |
            ├───.data_pipiline
            |    ├──── data_pipiline_s3.py
            |    └──── job_spark_campeonato.py
            |  
            ├───.kurbenetes
            |    └──── custom_values.yaml
            |
            ├─── README.md
            └─── requirements.txt


<h4> Tecnologias: </h4>

* [Kubectl](https://kubernetes.io/docs/tasks/tools/)
* [Docker](https://docs.docker.com/engine/install/ubuntu/)
* [AWS CLI](https://docs.aws.amazon.com/pt_br/cli/latest/userguide/cli-chap-getting-started.html) ou [Terraform](https://www.terraform.io/)
* [AWS-Vault](https://github.com/99designs/aws-vault)
* [AWS](https://github.com/99designs/aws-vault)
* [Python](https://www.python.org/)
* [Airflow](https://airflow.apache.org/)
* [Spark](https://spark.apache.org/)
* [Helm](https://helm.sh/docs/intro/install/)
<br>

<h4>Criação do cluster pela CLI:</h4>

~~~
eksctl create clurster --name=pre-aws-airflow --managed --instance-type=m5.xlarge 
--alb-ingress-access --node-private-networking --region=us-east-1 --nodes-min=1 nodes-max=3 --full-ecr-access --asg-access --nodegroup-name=ng-kubpre
~~~