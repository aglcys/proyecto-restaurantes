from appfoodie.models import Restaurante

Restaurante(nombre="De Luca", direccion="Rio Parana 745", telefono= 11123123, rango_precios= "800-2000", horario= "11hs a 23.30hs", tipo_comida="Pasta").save()
Restaurante(nombre="Tu Pasta", direccion="Obispo trejo 987", telefono= 11128304, rango_precios= "780-1800" , horario= "11hs a 00:30hs", tipo_comida="Pasta").save()
Restaurante(nombre="Pasta Pesto", direccion="Independecia 1233", telefono= 11628934, rango_precios= "500-2200", horario= "11hs a 00:30hs", tipo_comida="Pasta").save()
Restaurante(nombre="Italy", direccion="Estrada 90", telefono= 11825063, rango_precios= "950-2000", horario= "20hs a 00:30hs", tipo_comida="Pasta").save()
Restaurante(nombre="La Pasta Burrosa", direccion="Parana 234", telefono= 11732975, rango_precios= "890- 3000", horario= "11hs a 00:00hs", tipo_comida="Pasta").save()
Restaurante(nombre="Sabor de Roma", direccion="Balcarce 563", telefono= 11239024, rango_precios= "1000-2000", horario= "11hs a 15hs", tipo_comida="Pasta").save()
Restaurante(nombre="Hamburgueseria", direccion="Ituizango 879", telefono= 11934721, rango_precios= "740-2150" , horario= "11hs a 00.30hs", tipo_comida="Hamburguesas").save()
Restaurante(nombre="Blent", direccion="Peru 98", telefono= 11182945, rango_precios= "860-3000" , horario= "11hs a 14:30hs", tipo_comida="Hamburguesas").save()
Restaurante(nombre="Punto 33", direccion="9 de Julio 9874", telefono= 11153363, rango_precios= "930-3000", horario= "11hs a 00:30hs", tipo_comida="Hamburguesas").save()
Restaurante(nombre="Mc Donalds", direccion="Italia 9923", telefono= 11573274, rango_precios= "900-3200", horario= "11hs a 00:30hs", tipo_comida="Hamburguesas").save()
Restaurante(nombre="Hommie", direccion="Domingo Buzzi 1895", telefono= 11096489, rango_precios= "790-2290", horario= "11hs a 23:30hs", tipo_comida="Hamburguesas").save()
Restaurante(nombre="Burgerbeer", direccion="Ayacucho 909", telefono= 11892356, rango_precios= "820-2278", horario= "11hs a 00.30hs", tipo_comida="Hamburguesas").save()

print("Se cargaron con exito los restaurantes")