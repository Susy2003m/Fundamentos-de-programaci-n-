#Crear una matriz 3D paraa almacenar datos de temperaturas
#Priemra dimensión: ciudades (3 ciudades)
#Segunda dimensión: días de la semana (7 días)
#Tercera dimensión: semanas ( 4 semanas)
temperaturas = [
    [ #Ciudad 1 Guayaquil
        [  #semana 1
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 33},
            {"day": "Martes", "temp": 34},
            {"day": "Miercoles", "temp": 35},
            {"day": "Viernes", "temp": 29},
            {"day": "Sabado", "temp":33},
            {"day": "Domingo", "temp": 34},
        ],
        [   #Semana 2
            {"day" : "Lunes", "temp" : 33},
            {"day" : "Martes", "temp" : 30},
            {"day": "Miercoles", "temp": 36},
            {"day": "Jueves", "temp": 34},
            {"day": "Viernes", "temp": 34},
            {"day": "Sabado", "temp": 34},
            {"day": "Domingo", "temp": 34},
       ],
      [   #Semana 3
          {"day" : "Lunes", "temp" : 29},
          {"day" : "Martes", "temp" : 33},
          {"day": "Miercoles", "temp": 34},
          {"day": "Jueves", "temp": 31},
          {"day": "Lunes", "temp": 30},
          {"day": "Sabado", "temp": 32},
          {"day": "Domingo", "temp": 34},
      ],
      [   #Semana 4
          {"day" : "Lunes", "temp" : 30},
          {"day" : "Martes", "temp" : 35},
          {"day": "Miercoles", "temp": 34},
          {"day": "Jueves", "temp": 29},
          {"day": "Viernes", "temp": 36},
          {"day": "Sabado", "temp": 32},
          {"day": "Domingo", "temp": 33},
      ]
    ],
    [  # Ciudad 2 Quito
       [ # Semana 1
         {"day" : "Lunes", "temp" : 29},
         {"day" : "Martes", "temp" : 26 },
         {"day": "Miercoles", "temp": 28},
         {"day": "Jueves", "temp": 29},
         {"day": "Viernes", "temp": 25},
         {"day": "Sabado", "temp": 28},
         {"day": "Domingo", "temp": 27},
      ],
       [ # Semana 2
         { "day" : "lunes", "temp" : 29},
         { " day" : "Martes","temp" : 28 },
         {"day" : "Miercoles", "temp" : 25},
         {"day" : "Jueves", "temp" : 24},
         {"day" : "Viernes", "temp" : 25},
         {"day" : "Sabado", "temp" : 26},
         {"day" : "Domingo", "temp" : 24},
       ],
        [ # Semana 3
          { "day" : "lunes", "temp" : 26},
          { " day" : "Martes", "temp" : 28 },
          {"day" : "Miercoles", "temp" : 25},
          {"day" : "Jueves", "temp" : 24},
          {"day" : "Viernes", "temp" : 29},
          {"day" : "Sabado", "temp" : 27},
          {"day" : "Domingo", "temp" : 23},
        ],
        [ # Semana 4
            { "day" : "lunes", "temp" : 26},
            { " day" : "Martes", "temp" : 28 },
            {"day" : "Miercoles", "temp" : 25},
            {"day" : "Jueves", "temp" : 24},
            {"day" : "Viernes", "temp" : 29},
            {"day" : "Sabado", "temp" : 27},
            {"day" : "Domingo", "temp" : 24},
        ]
    ],
    [   # Ciudad 3 Cuenca
        [ # Semana 1
            { "day" : "lunes", "temp" : 30},
            {"day" : "Martes", "temp" : 28},
            {"day" : "Miercoles", "temp" : 27},
            {"day" : "Jueves", "temp" : 24},
            {"day" : "Viernes", "temp" : 25},
            {"day" : "Sabado", "temp" : 26},
            {"day" : "Domingo", "temp" : 27},
        ],
        [ # Semana 2 
            { "day" : "lunes", "temp" : 30},
            {"day" : "Martes", "temp" : 25},
            {"day" : "Miercoles", "temp" : 27},
            {"day" : "Jueves", "temp" : 24},
            {"day" : "Viernes", "temp" : 24},
            {"day" : "Sabado", "temp" : 26},
            {"day": "Domingo", "temp": 23},
        ],
        [ # Semana 3 
            { "day" : "lunes", "temp" : 30},
            {"day" : "Martes", "temp" : 25},
            {"day" : "Miercoles", "temp" : 27},
            {"day" : "Jueves", "temp" : 24},
            {"day" : "Viernes", "temp" : 24},
            {"day" : "Sabado", "temp" : 26},
            {"day" : "Domingo", "temp" : 25},
        ]    
    ]
    ]
#Calcular el promedio de temperaturas para cada ciudad y semana 
ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f'Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx}: {promedio}')
        