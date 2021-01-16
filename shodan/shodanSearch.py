import cadena as cadena

import shodan


class ShodanSearch:
    # Clase para buscar en Shodan
    def __init__(self, API_KEY):
        self.api = shodan.Shodan(API_KEY)

    def search(self, chain):
        # Búsquedas basadas en la cadena pasada por parámetro
        try:
            # Buscamos la cadena anterior pasada por parámetro
            result = self.api.search(str(cadena))
            return result
        except Exception as e:
            print("An error has ocurred: %s" % e)
            result = []
            return result

    def obtain_info_host(self, IP):
        # Obtiene la información que Shodan puede tener sobre una IP.
        try:
            results = self.api.host(IP)
            return results
        except Exception as e:
            print("Ups! An error has ocurred : %s" % e)
            results = []
            return results
