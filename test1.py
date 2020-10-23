serv_a = {
    'tanggal': '2020-10-23',
    'driver_list' : [
        {'nama':'alpha', 'jarak':10},
        {'nama':'bravo', 'jarak':20},
        {'nama':'charlie', 'jarak':40},
        {'nama':'delta', 'jarak':80},
    ],
    'motor':[
        {'a':'bebek'},
        {'b':'matic'},
        {'c':'moge'}
    ]
}

print(f"jarak {serv_a['driver_list'][0]['jarak']}m,"
      f" motor {serv_a['motor'][1]['b']}")