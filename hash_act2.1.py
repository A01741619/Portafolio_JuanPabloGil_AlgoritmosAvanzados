from pathlib import Path
import sys
import numpy as np       
import binascii 

def leerArchivo(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    return data

def crearTabla(datos: bytes, n: int) -> np.ndarray:
    if n < 16 or n > 64 or (n % 4) != 0:
        raise ValueError("n debe ser múltiplo de 4 y estar entre 16 y 64.")
    faltan = (-len(datos)) % n
    if faltan:
        pad_pat = str(n).encode("ascii")               
        datos += (pad_pat * ((faltan + len(pad_pat)-1)//len(pad_pat)))[:faltan]
    tabla = np.frombuffer(datos, dtype=np.uint8).reshape(-1, n)
    return tabla

def sumarColumnas(tabla: np.ndarray) -> np.ndarray:
    return np.sum(tabla, axis=0) % 256

def sumasToBytes(sumas: np.ndarray) -> bytes:
    return bytes(sumas.tolist())


def reducirSalida(datos: str, n: int) -> str:
    bytesReducidos = (n // 4) * 2  
    return datos[:bytesReducidos]

def main(path: Path, n: int, reducir: bool):
    datos = leerArchivo(path)
    tabla = crearTabla(datos, n)
    sumas = sumarColumnas(tabla)            
    checksum = sumasToBytes(sumas)          
    resultado_hex = binascii.hexlify(checksum).decode('ascii').upper() 
    
    if reducir:
        resultado_hex = reducirSalida(resultado_hex, n)
    
    print(resultado_hex)
if __name__ == "__main__":
  
    archivo = Path("entrada.txt")   
    n = 16                  
    reducir = True               

    main(archivo, n, reducir)


