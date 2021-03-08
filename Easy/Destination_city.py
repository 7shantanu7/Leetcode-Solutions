class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing_count = {}
        for path in paths:
            city_1, city_2 = path
            outgoing_count[city_1] = outgoing_count.get(city_1, 0)+1
            outgoing_count[city_2] = outgoing_count.get(city_2, 0)            
        for city in outgoing_count:
            if outgoing_count[city] == 0:
                return city
        