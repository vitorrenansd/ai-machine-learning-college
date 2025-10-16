from city import City
from adjacent import Adjacent

class Map:
    portoUniao = City("Porto União", 203) ## name, distanceFromGoal
    pauloFrontin = City("Paulo Frontin", 172)
    canoinhas = City("Canoinhas", 141)
    irati = City("Irati", 139)
    saoMateus = City("São Mateus", 123)
    mafra = City("Mafra", 95)
    tijucas = City("Tijucas do Sul", 57)
    curitiba = City("Curitiba", 0) ## Goal
    araucaria = City("Araucária", 23)
    balsaNova = City("Balsa Nova", 41)
    campoLargo = City("Campo Largo", 27)
    lapa = City("Lapa", 60)
    palmeira = City("Palmeira", 59)
    contenda = City("Contenda", 40)
    saoJose = City("São José dos Pinhais", 14)
    tresBarras = City("Três Barras", 130)


    portoUniao.add_adjacent_city(Adjacent(pauloFrontin, 46))
    portoUniao.add_adjacent_city(Adjacent(canoinhas, 78))
    portoUniao.add_adjacent_city(Adjacent(saoMateus, 87))

    pauloFrontin.add_adjacent_city(Adjacent(irati, 75))
    pauloFrontin.add_adjacent_city(Adjacent(portoUniao, 46))

    canoinhas.add_adjacent_city(Adjacent(portoUniao, 78))
    canoinhas.add_adjacent_city(Adjacent(tresBarras, 12))
    canoinhas.add_adjacent_city(Adjacent(mafra, 66))

    irati.add_adjacent_city(Adjacent(pauloFrontin, 75))
    irati.add_adjacent_city(Adjacent(palmeira, 75))
    irati.add_adjacent_city(Adjacent(saoMateus, 57))

    palmeira.add_adjacent_city(Adjacent(irati, 75))
    palmeira.add_adjacent_city(Adjacent(saoMateus, 77))
    palmeira.add_adjacent_city(Adjacent(campoLargo, 55))

    campoLargo.add_adjacent_city(Adjacent(palmeira, 55))
    campoLargo.add_adjacent_city(Adjacent(balsaNova, 22))
    campoLargo.add_adjacent_city(Adjacent(curitiba, 29))

    curitiba.add_adjacent_city(Adjacent(campoLargo, 29))
    curitiba.add_adjacent_city(Adjacent(balsaNova, 51))
    curitiba.add_adjacent_city(Adjacent(araucaria, 37))
    curitiba.add_adjacent_city(Adjacent(saoJose, 15))

    balsaNova.add_adjacent_city(Adjacent(curitiba, 51))
    balsaNova.add_adjacent_city(Adjacent(campoLargo, 22))
    balsaNova.add_adjacent_city(Adjacent(contenda, 19))

    araucaria.add_adjacent_city(Adjacent(curitiba, 37))
    araucaria.add_adjacent_city(Adjacent(contenda, 18))

    saoJose.add_adjacent_city(Adjacent(curitiba, 15))
    saoJose.add_adjacent_city(Adjacent(tijucas, 49))

    contenda.add_adjacent_city(Adjacent(balsaNova, 19))
    contenda.add_adjacent_city(Adjacent(araucaria, 18))
    contenda.add_adjacent_city(Adjacent(lapa, 26))

    mafra.add_adjacent_city(Adjacent(tijucas, 99))
    mafra.add_adjacent_city(Adjacent(lapa, 57))
    mafra.add_adjacent_city(Adjacent(canoinhas, 66))

    tijucas.add_adjacent_city(Adjacent(mafra, 99))
    tijucas.add_adjacent_city(Adjacent(saoJose, 49))

    lapa.add_adjacent_city(Adjacent(contenda, 26))
    lapa.add_adjacent_city(Adjacent(saoMateus, 60))
    lapa.add_adjacent_city(Adjacent(mafra, 57))

    saoMateus.add_adjacent_city(Adjacent(palmeira, 77))
    saoMateus.add_adjacent_city(Adjacent(irati, 57))
    saoMateus.add_adjacent_city(Adjacent(lapa, 60))
    saoMateus.add_adjacent_city(Adjacent(tresBarras, 43))
    saoMateus.add_adjacent_city(Adjacent(portoUniao, 87))

    tresBarras.add_adjacent_city(Adjacent(saoMateus, 43))
    tresBarras.add_adjacent_city(Adjacent(canoinhas, 12))
