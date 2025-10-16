from map import Map
from depth_search import DepthSearch
from greedy_search import GreedySearch
from astar_search import AStar

map = Map()
## ds = DepthSearch(map.portoUniao, map.curitiba)
## ds.search()

## gs = GreedySearch(map.curitiba)
## gs.search(map.portoUniao)

a_star = AStar(map.curitiba)
a_star.search(map.portoUniao)
