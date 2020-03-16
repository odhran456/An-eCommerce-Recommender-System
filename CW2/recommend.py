import pandas as pd
from normalise_user_item_matrix import linebreak
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors


matrix = pd.read_csv('user_item_matrix_normalised.csv')

drop_columns_all_except_name = [i for i in range(linebreak[0],linebreak[5]+1)]
drop_list = matrix.columns[drop_columns_all_except_name].tolist()
name_matrix = matrix.drop(drop_list,axis=1)
name_dict = dict(name_matrix.values)
# print(name_dict)

drop_columns = [i for i in range(1,linebreak[1]+1)]
drop_list = matrix.columns[drop_columns].tolist()
taxonomy_matrix = matrix.drop(drop_list,axis=1)

X = taxonomy_matrix.drop('ID',axis=1)
y = pd.DataFrame(taxonomy_matrix['ID'])

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=1,shuffle=False)

knn = NearestNeighbors(n_neighbors=8,algorithm='brute',metric='cosine')
knn.fit(X_train)

neighbours = knn.kneighbors(X_test,return_distance=False)

neighbour_1_posn = neighbours[0][0]
neighbour_1_ID = y_train.iloc[neighbours[0][0]].values[0]
neighbour_1_name = name_dict[neighbour_1_ID]
neighbour_2_posn = neighbours[0][1]
neighbour_2_ID = y_train.iloc[neighbours[0][1]].values[0]
neighbour_2_name = name_dict[neighbour_2_ID]
neighbour_3_posn = neighbours[0][2]
neighbour_3_ID = y_train.iloc[neighbours[0][2]].values[0]
neighbour_3_name = name_dict[neighbour_3_ID]

print(neighbour_1_name,neighbour_2_name,neighbour_3_name)

target = X.iloc[8].to_numpy().reshape(1,12)

top_sim = round(cosine_similarity(target,X.iloc[neighbour_1_posn].to_numpy().reshape(1,12))[0][0],3)
second_sim = round(cosine_similarity(target,X.iloc[neighbour_2_posn].to_numpy().reshape(1,12))[0][0],3)
third_sim = round(cosine_similarity(target,X.iloc[neighbour_3_posn].to_numpy().reshape(1,12))[0][0],3)

neighbours_similarity_dict = {
    neighbour_1_name:top_sim,
    neighbour_2_name:second_sim,
    neighbour_3_name:third_sim
}

print(neighbours_similarity_dict)
