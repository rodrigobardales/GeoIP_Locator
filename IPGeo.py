import geoip2.database

def get_country_from_ip(ip_addresses, db_path):
    # Cargar la base de datos GeoLite2
    with geoip2.database.Reader(db_path) as reader:
        results = {}
        for ip in ip_addresses:
            try:
                response = reader.country(ip)
                results[ip] = response.country.name
            except geoip2.errors.AddressNotFoundError:
                results[ip] = "No encontrado"
            except Exception as e:
                results[ip] = f"Error: {str(e)}"
        return results

def read_ips_from_file(file_path):
    # Leer las IPs desde el archivo, una por línea
    with open(file_path, 'r') as file:
        ip_addresses = [line.strip() for line in file if line.strip()]
    return ip_addresses

def save_results_to_file(results, output_file):
    # Guardar los resultados en un archivo de texto
    with open(output_file, 'w') as file:
        for ip, country in results.items():
            file.write(f"{ip}: {country}\n")

# Ruta del archivo con las direcciones IP
file_path = "file.txt"

# Ruta a la base de datos GeoLite2 descargada
db_path = "GeoLite2-Country.mmdb"

# Archivo donde se guardarán los resultados
output_file = "ip_results.txt"

# Leer las IPs del archivo
ip_addresses = read_ips_from_file(file_path)

# Obtener los países de las IPs
ip_countries = get_country_from_ip(ip_addresses, db_path)

# Guardar los resultados en un archivo
save_results_to_file(ip_countries, output_file)
