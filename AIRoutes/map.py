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

    portoUniao.add_adjacent_city(Adjacent(pauloFrontin))
    portoUniao.add_adjacent_city(Adjacent(canoinhas))
    portoUniao.add_adjacent_city(Adjacent(saoMateus))

    pauloFrontin.add_adjacent_city(Adjacent(irati))
    pauloFrontin.add_adjacent_city(Adjacent(portoUniao))

    canoinhas.add_adjacent_city(Adjacent(portoUniao))
    canoinhas.add_adjacent_city(Adjacent(tresBarras))
    canoinhas.add_adjacent_city(Adjacent(mafra))

    irati.add_adjacent_city(Adjacent(pauloFrontin))
    irati.add_adjacent_city(Adjacent(palmeira))
    irati.add_adjacent_city(Adjacent(saoMateus))

    palmeira.add_adjacent_city(Adjacent(irati))
    palmeira.add_adjacent_city(Adjacent(campoLargo))
    palmeira.add_adjacent_city(Adjacent(saoMateus))

    campoLargo.add_adjacent_city(Adjacent(palmeira))
    campoLargo.add_adjacent_city(Adjacent(balsaNova))
    campoLargo.add_adjacent_city(Adjacent(curitiba))

    curitiba.add_adjacent_city(Adjacent(campoLargo))
    curitiba.add_adjacent_city(Adjacent(balsaNova))
    curitiba.add_adjacent_city(Adjacent(araucaria))
    curitiba.add_adjacent_city(Adjacent(saoJose))

    balsaNova.add_adjacent_city(Adjacent(contenda))
    balsaNova.add_adjacent_city(Adjacent(campoLargo))
    balsaNova.add_adjacent_city(Adjacent(curitiba))

    araucaria.add_adjacent_city(Adjacent(curitiba))
    araucaria.add_adjacent_city(Adjacent(contenda))

    saoJose.add_adjacent_city(Adjacent(curitiba))
    saoJose.add_adjacent_city(Adjacent(tijucas))

    contenda.add_adjacent_city(Adjacent(balsaNova))
    contenda.add_adjacent_city(Adjacent(araucaria))
    contenda.add_adjacent_city(Adjacent(lapa))

    mafra.add_adjacent_city(Adjacent(canoinhas))
    mafra.add_adjacent_city(Adjacent(tijucas))
    mafra.add_adjacent_city(Adjacent(lapa))

    tijucas.add_adjacent_city(Adjacent(mafra))
    tijucas.add_adjacent_city(Adjacent(saoJose))

    lapa.add_adjacent_city(Adjacent(contenda))
    lapa.add_adjacent_city(Adjacent(saoMateus))
    lapa.add_adjacent_city(Adjacent(mafra))

    saoMateus.add_adjacent_city(Adjacent(palmeira))
    saoMateus.add_adjacent_city(Adjacent(lapa))
    saoMateus.add_adjacent_city(Adjacent(irati))
    saoMateus.add_adjacent_city(Adjacent(tresBarras))
    saoMateus.add_adjacent_city(Adjacent(portoUniao))

    tresBarras.add_adjacent_city(Adjacent(saoMateus))
    tresBarras.add_adjacent_city(Adjacent(canoinhas))
