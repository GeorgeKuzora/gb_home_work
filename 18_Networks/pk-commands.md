# Команды Packet Tracer

## команды к 1 семинару

- enable -переход в привилегированный режим
- conf t -переход в режим настройки
- int fa 0/0 -переход в режим настройки интерфейса fa 0/0
- description -ввести описание порта (например что к нему подключено, кто выполнял подключение и т. д.)
- shutdown -выключить порт
- duplex ? -настройки дуплекса
- speed ? -настройки скорости
- no -удалить настройку
- do -выполнить команду из привилегированного режима (если находитесь в режиме настройки)

### Команды для просмотра настроек:

- sh run -посмотреть конфигурацию устройства
- sh int fa0/0 -посмотреть информацию о работе порта
- sh int status -посмотреть статус всех портов
- sh int description -посмотреть описание всех портов

## команды к 2 семинару

### Настройка IP-адреса на интерфейсе

- interface FastEthernet0/0
- ip address 192.168.0.1 255.255.255.0

### Настройка статического маршрута

- ip route 10.0.0.0 255.255.255.0 1.1.1.1
    - где 10.0.0.0 255.255.255.0 - IP адрес сети назначения, а 1.1.1.1 - некст-хоп, куда надо слать пакет в сеть 10.0.0.0/255.255.255.0

### Команды для просмотра настроек:

- show ip route -просмотр таблицы маршрутизации
- show arp -просмотр таблицы ARP (на роутерах)
- show mac-address-table -просмотр таблицы коммутации (на свичах)
- arp -a - -просмотр таблицы ARP (на PC)

## команды к 3 семинару

### OSPF На роутере:

- router ospf 123 - включение OSPF процесса на роутре
- router-id 12.12.12.12 - назаначение Router-ID на роутере
- network 1.1.1.0 0.0.0.255 area 0 - включение сети 1.1.1.0/24 в OSPF процесс в area 0 (соответственно и интерфейс из этой сети включается в процесс OSPF)

### Команды для show:

- show ip ospf int (brief) - просмотр интерфейсов, включенных в OSPF процесс
- show ip ospf nei - просмотр соседей по OSPF
- sh ip route ospf - просмотр маршрутов, заинсталлированных в таблицу маршрутизации по протоколу OSPF

### VLAN на коммутаторе:

- vlan 333 - создание влана 333
- name TEST - даем название влану
- interface FastEthernet0/1 - настройка порта в режиме Access с вланом 10
- switchport access vlan 10
- switchport mode access
- interface GigabitEthernet0/1 - настройка порта в режиме Trunk с вланом 10 и 20
- switchport trunk allowed vlan 10,20
    - ( switchport trunk allowed vlan add, remove) - добавить, удалить влан из списка
- switchport mode trunk

### VLAN на роутере:

- interface GigabitEthernet0/0/0.10 - создание подынтерфейса на порту GigabitEthernet0/0/0 с ID 10.
- encapsulation dot1Q 10 - включение подынтерфейса GigabitEthernet0/0/0.10 во влан 10.
- no ip address
- interface GigabitEthernet0/0/0.20 - создание подынтерфейса на порту GigabitEthernet0/0/0 с ID 20.
- encapsulation dot1Q 20 - включение подынтерфейса GigabitEthernet0/0/0.10 во влан 20.
- no ip address - (не забывайте назначить IP адрес)

### Команды для show:

- sh vlan
- sh int gigabitEthernet 0/1 switchport

## Настройка NAT

### Статический NAT на роутере

- enable
- conf t
- interface gb/0/0/0
- ip nat inside
- interface gb/0/0/1
- ip nat outside
- exit - переходим в глобальный конфиг
- ip nat inside source static 10.0.0.100 7.7.7.1

### Динамический (PAT) NAT на роутере

- enable
- conf t
- interface gb/0/0/0
- ip nat inside
- interface gb/0/0/1
- ip nat outside
- exit - переходим в глобальный конфиг
- ip access-list standard NET10
- permit 10.0.0.0 0.0.0.255 - разрешенный диапазон адрессов для листа
- ip nat inside source list NET10 interface gb 0/0/0 overload - или можно создать pool адрессов интерфейсов

### Проброс портов

- enable
- conf t
- interface gb/0/0/0
- ip nat inside
- interface gb/0/0/1
- ip nat outside
- exit - переходим в глобальный конфиг
- ip nat inside source static tcp(udp) 10.0.0.100 80 7.7.7.1 80

### Команды show

- show ip nat translations

## Настройка GRE

- enable
- conf t
- interface tunnel 777
- ip address 172.16.0.1 255.255.255.0 - промежуточная сеть между приватными сетями
- tunnel source ge 0/0/0 - публичный интерфейс с которого будут уходить пакеты
- tunnel destination 4.4.4.2 - публичный адрес на который будут отсылаться пакеты
- exit - в глобальный конфиг
- ip route 192.168.0.0 255.255.255.0 172.16.0.2 - настройка статического маршрута в нашей приватной тунелированной сети