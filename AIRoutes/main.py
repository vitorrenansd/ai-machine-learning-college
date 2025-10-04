from map import Map
from depth_search import DepthSearch

map = Map()
ds = DepthSearch(map.portoUniao, map.curitiba)
ds.search()
