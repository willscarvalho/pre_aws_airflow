from pyspark.sql import SparkSession
from pyspark.sql import functions as f



if __name__ == "__main__":

    print("Starting Spark Session")

    spark = SparkSession.builder.getOrCreate()

    df = spark.read.csv("s3://bucket-campeonato-brasileiro-216320350078/raw-data/campeonato-brasileiro.csv", header=True, sep=",", inferSchema=True)

    df.createOrReplaceTempView("campeonato_brasileiro")

    # Media Gols por partida:
    avg_gols_partida = spark.sql("""
    SELECT
        ROUND((SUM(visitante_placar)\
             + SUM(mandante_placar))\
                 / COUNT(id), 0) as media_gols_partida
    From
        campeonato_brasileiro
    """)

    # Proporção gols visitante
    propotion_visiting_gols =spark.sql("""
    SELECT
        ROUND(SUM(visitante_placar)/(SUM(visitante_placar) + SUM(mandante_placar))*100, 2) AS  proporcao_gols_visitante
    From
        campeonato_brasileiro
    """)

    # Proporção gols mandante
    propotion_home_gols = spark.sql("""
    SELECT
        ROUND(SUM(mandante_placar)/(SUM(visitante_placar) + SUM(mandante_placar))*100, 2) AS  proporcao_gols_visitante
    From
        campeonato_brasileiro
    """)

    (
        avg_gols_partida.write.format("parquet")
        .save("s3://bucket-campeonato-brasileiro-216320350078/processed-data/campeonato-brasileiro/avg_gols")
    )

    (
        propotion_visiting_gols.write.format("parquet")
        .save("s3://bucket-campeonato-brasileiro-216320350078/processed-data/campeonato-brasileiro/propotion_visiting_gols")
    )

    (
        propotion_home_gols.write.format("parquet")
        .save("s3://bucket-campeonato-brasileiro-216320350078/processed-data/campeonato-brasileiro/propotion_home_gols")
    )