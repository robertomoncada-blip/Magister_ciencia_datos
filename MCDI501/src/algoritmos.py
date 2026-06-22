"""Módulo de algoritmos estructurados y recursivos — Fase 3.

Implementa algoritmos de ordenamiento y búsqueda con análisis de complejidad
aplicados al dataset AI Impact on Jobs 2030.

Algoritmos
----------
merge_sort        : O(n log n) tiempo, O(n) espacio — divide y vencerás recursivo
merge_sort_key    : variante con función key y orden configurable
busqueda_binaria  : O(log n) tiempo, O(log n) espacio — recursivo sobre lista ordenada
bubble_sort       : O(n²) tiempo, O(n) espacio — referencia de comparación (copia defensiva)
"""

from __future__ import annotations


# ---------------------------------------------------------------------------
# Merge Sort recursivo
# ---------------------------------------------------------------------------

def merge_sort(arr: list) -> list:
    """Ordena una lista de menor a mayor mediante merge sort recursivo.

    Complejidad: O(n log n) tiempo, O(n) espacio auxiliar.
    Caso base : len(arr) <= 1 → retorna sin llamada recursiva.
    Caso recur: divide por la mitad, ordena cada mitad y las combina.

    Parameters
    ----------
    arr : list
        Lista de elementos comparables.

    Returns
    -------
    list
        Nueva lista ordenada ascendentemente (el original no se muta).
    """
    if len(arr) <= 1:          # caso base
        return arr
    mid = len(arr) // 2
    izquierda = merge_sort(arr[:mid])   # caso recursivo — mitad izquierda
    derecha = merge_sort(arr[mid:])     # caso recursivo — mitad derecha
    return _merge(izquierda, derecha)


def _merge(izq: list, der: list) -> list:
    """Combina dos listas ya ordenadas en una sola lista ordenada. O(n)."""
    resultado, i, j = [], 0, 0
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado


# ---------------------------------------------------------------------------
# Merge Sort con función key (versión generalizada)
# ---------------------------------------------------------------------------

def merge_sort_key(arr: list, key=lambda x: x, descendente: bool = False) -> list:
    """Merge sort recursivo con función key y dirección configurable.

    Complejidad: O(n log n) tiempo, O(n) espacio auxiliar.

    Parameters
    ----------
    arr : list
        Lista de elementos.
    key : callable
        Función que extrae el valor de comparación de cada elemento.
    descendente : bool
        True para orden descendente; False (default) para ascendente.

    Returns
    -------
    list
        Lista ordenada según key y dirección.
    """
    if len(arr) <= 1:           # caso base
        return arr
    mid = len(arr) // 2
    izq = merge_sort_key(arr[:mid], key, descendente)
    der = merge_sort_key(arr[mid:], key, descendente)
    return _merge_key(izq, der, key, descendente)


def _merge_key(izq: list, der: list, key, descendente: bool) -> list:
    """Función auxiliar de mezcla con key y dirección. O(n)."""
    resultado, i, j = [], 0, 0
    while i < len(izq) and j < len(der):
        val_i = key(izq[i])
        val_j = key(der[j])
        if descendente:
            tomar_izq = val_i >= val_j
        else:
            tomar_izq = val_i <= val_j
        if tomar_izq:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado


# ---------------------------------------------------------------------------
# Búsqueda binaria recursiva
# ---------------------------------------------------------------------------

def busqueda_binaria(arr: list, objetivo, bajo: int = 0, alto: int = None) -> int:
    """Búsqueda binaria recursiva sobre una lista ordenada ascendentemente.

    Complejidad: O(log n) tiempo, O(log n) espacio (pila de recursión).
    Caso base 1 : bajo > alto → elemento no encontrado, retorna -1.
    Caso base 2 : arr[mid] ≈ objetivo → encontrado, retorna mid.
    Caso recur  : busca en la mitad izquierda o derecha según comparación.

    Parameters
    ----------
    arr : list
        Lista ordenada de menor a mayor.
    objetivo : float | int
        Valor a encontrar.
    bajo : int
        Límite inferior del rango de búsqueda (default 0).
    alto : int | None
        Límite superior del rango (default len(arr)-1 en la primera llamada).

    Returns
    -------
    int
        Índice del elemento en arr, o -1 si no se encuentra.
    """
    if alto is None:
        alto = len(arr) - 1
    if bajo > alto:                      # caso base 1: no encontrado
        return -1
    mid = (bajo + alto) // 2
    if abs(arr[mid] - objetivo) < 1e-9:  # caso base 2: encontrado
        return mid
    if arr[mid] < objetivo:              # caso recursivo: mitad derecha
        return busqueda_binaria(arr, objetivo, mid + 1, alto)
    return busqueda_binaria(arr, objetivo, bajo, mid - 1)  # mitad izquierda


# ---------------------------------------------------------------------------
# Bubble Sort (referencia de comparación O(n²))
# ---------------------------------------------------------------------------

def bubble_sort(arr: list) -> list:
    """Ordenamiento burbuja iterativo. O(n²) tiempo, O(n) espacio extra (copia defensiva).

    Se incluye únicamente como referencia para comparar con merge_sort
    y demostrar experimentalmente la diferencia entre O(n²) y O(n log n).
    No debe usarse en producción para n > unos pocos cientos.

    Parameters
    ----------
    arr : list
        Lista de elementos comparables.

    Returns
    -------
    list
        Nueva lista ordenada ascendentemente.
    """
    arr = list(arr)   # copia para no mutar el original
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
