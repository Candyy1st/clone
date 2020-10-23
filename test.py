import requests

print('Hello World')

try:
    r = requests.get('https://google.com')
    print(r.status_code)
    if r.status_code == 200:
        print("Berhasil")
except Exception as e:
    print('Ada Error', e)

JA = 4
for i in range(1, JA):
    print(f'Hallo {i}')

anak = ['a', 'b', 'c']
print(anak)
anak.append('d')
print(anak)
print(f'Halo {anak[1]}')
#version 1
for a in anak:
    print(f'hai {a}')
#version 2
for a in range(0, len(anak)):
    print(f'{a+1}. hai {anak[a]}')
