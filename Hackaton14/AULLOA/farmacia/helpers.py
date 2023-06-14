def generar_boleta_venta(nombre_archico, ventas):
    
    archivo = open(nombre_archico, 'w')

    archivo.write("************************************************************************\n")
    archivo.write("                             BOLETA DE VENTA\n")
    archivo.write("************************************************************************\n\n")

    archivo.write("------------------------------------------------------------------------\n")
    archivo.write("Detalle de la Venta:\n")
    archivo.write("------------------------------------------------------------------------\n")
    archivo.write("|  Producto            |  Cantidad                   |   Subtotal      |\n")
    archivo.write("------------------------------------------------------------------------\n")
    
    # for venta in ventas:
    archivo.write(ventas.name + '/t')
    
    archivo.close()

    return archivo
