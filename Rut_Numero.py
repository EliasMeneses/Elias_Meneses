vlansw = {
    "sw1": {"VLAN nativa": 99, "VLANs": [10, 20, 30]},
    "sw2": {"VLAN nativa": 200, "VLANs": [40, 50, 60]}
}

nombre_switch = input("Ingrese el nombre del Switch (SW1 o SW2): ")

if nombre_switch in vlansw:
    vlan_n = vlansw[nombre_switch]["VLAN nativa"]
    vlan_l = vlansw[nombre_switch]["VLANs"]
    
    print("El switch", nombre_switch, "tiene la VLAN nativa", vlan_n, "y las VLANs", vlan_l)
    
    if nombre_switch == "sw1":
        vlan_d = [10, 100, 30]
        if vlan_l == vlan_d:
            print("Las VLAN son iguales y cumplen con el requerimiento.")
        else:
            print("Las VLAN son diferentes y no cumplen con el requerimiento.")
    
    elif nombre_switch == "sw2":
        vlan_d = [40, 50, 60]
        if vlan_l == vlan_d:
            print("Las VLAN son iguales y cumplen con el requerimiento.")
        else:
            print("Las VLAN son diferentes y no cumplen con el requerimiento.")
else:
    print("Switch no encontrado.")
