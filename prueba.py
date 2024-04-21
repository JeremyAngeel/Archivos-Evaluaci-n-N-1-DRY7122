def tiene_ruta_por_defecto(archivo_config):
    with open(archivo_config, 'r') as f:
        lineas = [linea.strip() for linea in f.readlines() if not linea.strip().startswith('!')]

    for linea in lineas:
        if 'ip route 0.0.0.0 0.0.0.0' in linea:
            return True

    return False

if __name__ == "__main__":
    archivo_config = "RT01.cfg"
    if tiene_ruta_por_defecto(archivo_config):
        print("El archivo de configuracion si cuenta con una entrada de ruta por defecto en la tabla de enrutamiento del router.")
    else:
        print("El archivo de configuración no tiene una entrada de ruta por defecto.")
