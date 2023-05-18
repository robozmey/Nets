import random

ip_list = []

def generate_ip_str():
    return '.'.join([str(random.randrange(10, 250)) for _ in range(4)])


def generate_ip():
    global ip_list
    ip = generate_ip_str()
    while ip in ip_list:
        ip = generate_ip_str()
    
    ip_list.append(ip)

    return ip


def generate_net(router_count = 6, connection_prob = 0.5):
    routers = [generate_ip() for _ in range(router_count)]

    gateways = {}
    for router in routers:
        gateways[router] = []

    for router1 in routers:
        for router2 in routers:
            if router1 < router2:
                if random.random() < connection_prob:
                    gateways[router1].append(router2)
                    gateways[router2].append(router1)

    tables = {}
    for router in routers:
        tables[router] = {}
        for dst_router in gateways[router]:
            tables[router][dst_router] = (router, dst_router, 1)

    return routers, gateways, tables
    

routers, gateways, tables = generate_net()

print(tables)

from dsplot.graph import Graph

graph = Graph(
    gateways, directed=False
)
graph.plot()

def print_table(table, router, name_state='Final'):
    print(name_state, 'state of router', router, 'table:')

    frmt = '{:<20} {:<20} {:<20} {:<10}'

    print(frmt.format('[Source IP]', '[Destination IP]', '[Next Hop]', '[Metric]'))

    for dst_router in table:
        src_router, next_hop, metric = table[dst_router]
        print(frmt.format(router, dst_router, next_hop, metric))


def print_tables(tables, name_state='Final'):
    for router in tables:
        print_table(tables[router], router, name_state=name_state)

queue = {}
for router in routers:
    queue[router] = []

step_count = ()

for step_no in range(1, 4):

    print_tables(tables, name_state='Simulation step ' + str(step_no))

    print()
    print()
    print()
    
    for router in routers:
        for router2 in gateways[router]:
            queue[router2].append(tables[router].copy())

    for router in routers:
        my_table = tables[router]

        for table in queue[router]:
            for dst_router in table:
                src_router, next_hop, metric = table[dst_router]

                if dst_router not in my_table.keys() or my_table[src_router][2] + table[dst_router][2] < my_table[dst_router][2]:
                    new_metric = my_table[src_router][2] + table[dst_router][2] 
                    if new_metric > 16:
                        new_metric = 16

                    my_table[dst_router] = (router, src_router, new_metric)




print_tables(tables)