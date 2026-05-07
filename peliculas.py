peliculas_juan = {"Inception", "Matrix", "Interstellar", "Avengers", "Dune"}
peliculas_maria = {"Matrix", "Avengers", "Titanic", "Dune", "Coco"}
peliculas_pedro = {"Inception", "Titanic", "Coco", "Matrix", "Parasite"}

def peliculas_comunes(peliculas1=peliculas_juan, peliculas2=peliculas_maria, peliculas3=peliculas_pedro):
    return peliculas1 & peliculas2 & peliculas3

def recomendar_a_juan(peliculas1=peliculas_juan, peliculas2=peliculas_maria, peliculas3=peliculas_pedro):

    peliculas_recomendadas = (peliculas2 | peliculas3) - peliculas1
    return peliculas_recomendadas

def exclusivas_de_cada_uno(peliculas1=peliculas_juan, peliculas2=peliculas_maria, peliculas3=peliculas_pedro):
    
    return {
        "María": peliculas2 - (peliculas1 | peliculas3),
        "Pedro": peliculas3 - (peliculas1 | peliculas2),
        "Juan": peliculas1 - (peliculas2 | peliculas3)
    }

if __name__ == "__main__":
    print("1. Películas en común:")
    print(peliculas_comunes(peliculas1=peliculas_juan, peliculas2=peliculas_maria, peliculas3=peliculas_pedro))

    print("\n2. Recomendar a Juan:")
    print(recomendar_a_juan(peliculas1=peliculas_juan, peliculas2=peliculas_maria, peliculas3=peliculas_pedro))

    print("\n3. Exclusivas de cada uno:")
    print(exclusivas_de_cada_uno(peliculas1=peliculas_juan, peliculas2=peliculas_maria, peliculas3=peliculas_pedro))