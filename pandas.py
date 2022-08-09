import pandas as pd
import requests
import mysql.connector
import numpy as np
from sqlalchemy import create_engine

##############################################################################

engine = create_engine("mysql://{user}:{pw}@{host}:3306/{db}"
            .format(host="34.163.182.248", db='academy', user='root', pw='Ciocanul12%40'))

########################################################
#Connect to db

mydb = mysql.connector.connect(
  host="34.163.182.248",
  port=3306,
  user="root",
  password="Ciocanul12@",
  database="academy"
)
mycursor = mydb.cursor()
########################################################

url = "https://www.balldontlie.io/api/v1/players"
r = requests.get(url,params = {"per_page": 100})
json = r.json()
# print(json.keys())
# print(json["data"])

players = pd.DataFrame(json["data"])
list = players["team"].tolist()
# print(list)
teams = pd.DataFrame(list)
teams["player_id"] = players["id"]
print(teams.to_string())
del players["team"]
print(players.to_string())

########################################################

tabela1 = pd.read_sql_query("Select * from nba_players",mydb)
tabela2 = pd.read_sql_query("Select * from nba_salary",mydb)

new1 = tabela1.merge(tabela2, on ="id")
print(new1.to_string())

##############################################################################
#Media de salariu pe oras si numarul de playeri din oras
toinsert1 =new1.groupby("team.city").agg({"Salary":"mean","id":"count"})
print(toinsert1)
# CREEAREA TABELULUI
# comanda = '''CREATE TABLE city_average_edi(
#                 team_city varchar,
#                 salary int,
#                 id int
#             )'''
# mycursor.execute(comanda)
toinsert1.to_sql("city_average_edi", con=engine, if_exists='replace', index=False)
##############################################################################






##############################################################################
#Full name and if is above or under average salary
new1["name"] = new1['first_name'] +" "+ new1['last_name']
avgSal = new1["Salary"].mean()
# print(avgSal)
new1['Above_average_salary'] = np.where(new1['Salary'] > avgSal, 1, 0)

toinsert2 = new1[['name','Above_average_salary']].reset_index()
# print(toinsert2.to_string())

# CREEAREA TABELULUI
# comanda = '''CREATE TABLE players_average_edi(
#                 name varchar,
#                 Above_average_salary int
#             )'''
# mycursor.execute(comanda)
toinsert2.to_sql("players_average_edi", con=engine, if_exists='replace', index=False)
##############################################################################






##############################################################################
# Name and salary
toinsert3 = new1[['name','Salary','team.city']].where(new1["team.city"] == "LA").sort_values(by=['team.city','Salary']).reset_index()
print(toinsert3)
# CREEAREA TABELULUI
# comanda = '''CREATE TABLE LA_salary(
#                 name varchar,
#                 salary int
#             )'''
toinsert3.to_sql()

##############################################################################
