# Biblioteca de funciones de Python traducidas al español

# Importar módulos necesarios
import os

# Traducción de print()
def imprimir(*args, **kwargs):
    print(*args, **kwargs)

# Traducción de input()
def entrada(mensaje=""):
    return input(mensaje)

# Traducción de len()
def longitud(objeto):
    return len(objeto)

# Traducción de sum()
def sumar(iterable):
    return sum(iterable)

# Traducción de range()
def rango(*args):
    return range(*args)

# Traducción de sorted()
def ordenado(iterable, reverse=False):
    return sorted(iterable, reverse=reverse)

# Traducción de list()
def lista(iterable):
    return list(iterable)

# Traducción de dict()
def diccionario(**kwargs):
    return dict(**kwargs)

# Traducción de set()
def conjunto(iterable):
    return set(iterable)

# Traducción de tuple()
def tupla(iterable):
    return tuple(iterable)

# Traducción de map()
def mapa(funcion, iterable):
    return map(funcion, iterable)

# Traducción de filter()
def filtro(funcion, iterable):
    return filter(funcion, iterable)

# Traducción de zip()
def zipear(*iterables):
    return zip(*iterables)

# Traducción de enumerate()
def enumerar(iterable, start=0):
    return enumerate(iterable, start=start)

# Traducción de any()
def alguno(iterable):
    return any(iterable)

# Traducción de all()
def todos(iterable):
    return all(iterable)

# Traducción de min()
def minimo(iterable):
    return min(iterable)

# Traducción de max()
def maximo(iterable):
    return max(iterable)

# Traducción de abs()
def absoluto(numero):
    return abs(numero)

# Traducción de round()
def redondear(numero, ndigits=0):
    return round(numero, ndigits)

# Traducción de str()
def cadena(objeto):
    return str(objeto)

# Traducción de int()
def entero(objeto, base=10):
    return int(objeto, base)

# Traducción de float()
def flotante(objeto):
    return float(objeto)

# Traducción de bool()
def booleano(objeto):
    return bool(objeto)

# Traducción de type()
def tipo(objeto):
    return type(objeto)

# Traducción de dir()
def directorio(objeto):
    return dir(objeto)

# Traducción de help()
def ayuda(objeto):
    return help(objeto)

# Traducción de isinstance()
def es_instancia(objeto, clase):
    return isinstance(objeto, clase)

# Traducción de issubclass()
def es_subclase(clase, superclase):
    return issubclass(clase, superclase)

# Traducción de pow()
def potencia(base, exponente, modulo=None):
    return pow(base, exponente, modulo)

# Traducción de divmod()
def divmodulo(a, b):
    return divmod(a, b)

# Traducción de reversed()
def invertido(iterable):
    return reversed(iterable)

# Traducción de slice()
def rebanada(inicio, fin, paso=None):
    return slice(inicio, fin, paso)

# Traducción de hash()
def hash(objeto):
    return hash(objeto)

# Traducción de id()
def identificador(objeto):
    return id(objeto)

# Traducción de oct()
def octal(numero):
    return oct(numero)

# Traducción de hex()
def hexadecimal(numero):
    return hex(numero)

# Traducción de bin()
def binario(numero):
    return bin(numero)

# Traducción de chr()
def caracter(codigo):
    return chr(codigo)

# Traducción de ord()
def ordinal(caracter):
    return ord(caracter)
