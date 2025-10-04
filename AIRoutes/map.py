from city import City
from adjacent import Adjacent

class Map:
    portoUniao = City("Porto União")
    pauloFrontin = City("Paulo Frontin")
    canoinhas = City("Canoinhas")
    irati = City("Irati")
    saoMateus = City("São Mateus")
    mafra = City("Mafra")
    tijucas = City("Tijucas do Sul")
    curitiba = City("Curitiba")
    araucaria = City("Araucária")
    balsaNova = City("Balsa Nova")
    campoLargo = City("Campo Largo")
    lapa = City("Lapa")
    palmeira = City("Palmeira")
    contenda = City("Contenda")
    saoJose = City("São José dos Pinhais")
    tresBarras = City("Três Barras")

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
