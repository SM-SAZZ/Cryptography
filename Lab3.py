"""
№ 6 Реализовать программный продукт построения всех примитивов
заданного поля GF(2n). Указать все промежуточные результаты, то есть
- первичный перебор с указанием проверенных элементов поля и поянением,
почему они не примитивы;
- вывод всех примитивов с указанием степеней образующего элемента.
"""
def binary_to_polynomial(binary, n):
    """Преобразует двоичное число в строку-многочлен."""
    terms = []
    for i in range(n - 1, -1, -1):
        if binary & (1 << i):
            if i == 0:
                terms.append("1")
            elif i == 1:
                terms.append("x")
            else:
                terms.append(f"x^{i}")
    if not terms:
        return "0"
    return " + ".join(terms)

def gf2_multiply(a, b, mod):
    """Умножение в GF(2^n) по модулю mod."""
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        if a & (1 << n):
            a ^= mod
        b >>= 1
    return result

def gf2_pow(element, power, mod):
    """Возведение в степень в GF(2^n)."""
    result = 1
    while power > 0:
        if power & 1:
            result = gf2_multiply(result, element, mod)
        element = gf2_multiply(element, element, mod)
        power >>= 1
    return result

def is_primitive(element, mod, field_size):
    """Проверка, является ли элемент примитивным."""
    for k in range(1, field_size):
        if gf2_pow(element, k, mod) == 1:
            print(f"Элемент {binary_to_polynomial(element, n)} не примитивен: ({binary_to_polynomial(element, n)})^{k} = 1")
            return False
    return True

def find_primitive_elements(n, mod):
    """Поиск всех примитивных элементов в GF(2^n)."""
    field_size = 2**n - 1
    primitive_elements = []
    for element in range(1, 2**n):
        if is_primitive(element, mod, field_size):
            primitive_elements.append(element)
            print(f"Элемент {binary_to_polynomial(element, n)} примитивен")
    return primitive_elements

def print_all_powers(primitive_elements, mod, n):
    """Вывод всех степеней для каждого примитивного элемента."""
    for element in primitive_elements:
        print(f"\nСтепени примитивного элемента {binary_to_polynomial(element, n)}:")
        for k in range(1, 2**n):
            power = gf2_pow(element, k, mod)
            print(f"({binary_to_polynomial(element, n)})^{k} = {binary_to_polynomial(power, n)}")

# Ввод данных с клавиатуры
n = int(input("Введите степень n для поля GF(2^n): "))
mod_input = input("Введите примитивный полином в двоичном виде: ")
mod = int(mod_input, 2)  # Преобразуем двоичную строку в число

# Проверка, что полином имеет степень n
if mod.bit_length() - 1 != n:
    print(f"Ошибка: Полином должен иметь степень {n}.")
    exit()

# Поиск примитивных элементов
print(f"\nПоиск примитивных элементов в GF(2^{n})...")
primitive_elements = find_primitive_elements(n, mod)

# Вывод всех примитивных элементов
print("\nВсе примитивные элементы:")
for element in primitive_elements:
    print(binary_to_polynomial(element, n))

# Вывод степеней для каждого примитивного элемента
if primitive_elements:
    print("\nВывод степеней для всех примитивных элементов:")
    print_all_powers(primitive_elements, mod, n)
else:
    print("Примитивные элементы не найдены.")