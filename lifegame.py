import numpy

frame = numpy.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]])

s = len(frame)

def compute_number_neighbors(padded_frame, index_line, index_column):

    number_neighbors = 0

    for i in range(index_line -1, index_line + 2):
        for j in range(index_column -1, index_column + 2):

# On parcout les voisins de la cellule pour trouver les 1
            if  padded_frame[(i,j)] != 0:
# Si il y a des voisins on incrémente number_neighbors
                number_neighbors += padded_frame[(i,j)]
    
    #print(number_neighbors)
    return number_neighbors
    
def compute_next_frame(frame):

#Etape 1 : On calcule la matrice avec bordure
    padded_frame = numpy.pad(frame, 1, mode='constant')
    #new_frame = numpy.zeros((s,s))

#Etape 2 : 2 boucle for pour parcourir la matrice avec bordure
    for index_line in range(1, padded_frame.shape[0] -1):
        for index_column in range(1, padded_frame.shape[1] -1):

#Etape 3: On récupère le nombres de cellule voisines
            number_neighbors = compute_number_neighbors(padded_frame, index_line, index_column)

#Etape 4 : test et remplacement des cellules
# Si la cellule est vivante et que le nombre de cellule voisine est inférieur à 2 ou supérieur à 3 la cellule devient morte
            if  padded_frame[index_line][index_column] == 1:
                if (number_neighbors - 1) < 2 or (number_neighbors - 1) > 3 :
                    frame[index_line - 1][index_column - 1] = 0
                elif (number_neighbors - 1) == 2 :
                    frame[index_line - 1][index_column - 1] = 1
                
# Si la cellule est morte et qu'elle a 3 cellules voisines elle devient vivante
            elif padded_frame[index_line][index_column] == 0 :
                if number_neighbors == 3 :
                    frame[index_line -1][index_column -1] = 1
   
    return frame

k=0

while k<5:

    #boucle infini qui affiche toutes les frames successives (ctrl + c pour arreter le script) (ici boucle fini pour test rapide)
    print(frame)
    frame = compute_next_frame(frame)
    k += 1