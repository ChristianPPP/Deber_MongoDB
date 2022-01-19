#!/usr/bin/env python
# coding: utf-8

#In[0]
#  Copyright (c) 2022.
#  Realizado por: Christian Palacios 
#  All rights reserved.
import pymongo
import random


#In[1]
#  Copyright (c) 2022.
#  Realizado por: Christian Palacios 
#  All rights reserved.
# Ejercicio con MongoDB de forma local
mongo = pymongo.MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')
db = mongo['ciudadanosbd']
docs = db['Datos']

#In[2]
#  Copyright (c) 2022.
#  Realizado por: Christian Palacios 
#  All rights reserved.
nombres = ["Adriana" ,"Byron" ,"Carlos", "Daniel", "Elias", "Fausto", "Gabriel", "Hugo", "Igancio", "Javier"] 
apellidos = ["Smith", "Johnson", "Williams", "Brown", "Jones", "García", "Miller", "Davis", "Rodrígez", "Martínez"]   
n = input("Ingrese el numero de ciudadanos: ") 
for i in range (int(n)):
    doc = {
            "Nombres":nombres[random.randint(0, 9)]+" "+nombres[random.randint(0, 9)],
            "Apellidos":apellidos[random.randint(0, 9)]+" "+apellidos[random.randint(0, 9)],
            "Edad":random.randint(18, 80),
            "Cedula":str(random.randint(1000000000, 1999999999))
        }
    docs.insert_one(doc)
    

#In[3]
#  Copyright (c) 2022.
#  Realizado por: Christian Palacios 
#  All rights reserved.
def consultar_mongodb():
    for datos in docs.find():
        print(datos)
consultar_mongodb()

#In[4]
#  Copyright (c) 2022.
#  Realizado por: Christian Palacios 
#  All rights reserved.
# Ejercicio con MongoDB en la nube
mongo = pymongo.MongoClient('mongodb+srv://admin:agujeronegro@cluster0.21fzo.mongodb.net/test')
db = mongo['ciudadanosbd']
docs = db['Datos']


#In[5]
#  Copyright (c) 2022.
#  Realizado por: Christian Palacios 
#  All rights reserved.
# Ejercicio con MongoDB en la nube
nombres = ["Adriana" ,"Byron" ,"Carlos", "Daniel", "Elias", "Fausto", "Gabriel", "Hugo", "Igancio", "Javier"] 
apellidos = ["Smith", "Johnson", "Williams", "Brown", "Jones", "García", "Miller", "Davis", "Rodrígez", "Martínez"]   
n = input("Ingrese el numero de ciudadanos: ") 
for i in range (int(n)):
    doc = {
            "Nombres":nombres[random.randint(0, 9)]+" "+nombres[random.randint(0, 9)],
            "Apellidos":apellidos[random.randint(0, 9)]+" "+apellidos[random.randint(0, 9)],
            "Edad":random.randint(18, 80),
            "Cedula":str(random.randint(1000000000, 1999999999))
        }
    docs.insert_one(doc)
    
    
#In[6]
#  Copyright (c) 2022.
#  Realizado por: Christian Palacios 
#  All rights reserved.
def consultar_mongodb():
    for datos in docs.find():
        print(datos)
consultar_mongodb()


