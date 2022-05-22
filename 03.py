delta = lambda x:[x[0]]+[v-x[i-1] for i,v in enumerate(x) if i!=0]
assert delta([1000, 800, 802, 1000, 1003]) == [1000, -200, 2, 198, 3]
assert delta([42]) == [42]