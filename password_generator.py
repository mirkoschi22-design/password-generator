# 🔐 Password Generator - Roldán Edition
# Autor: Mirko David Schiavi
# GitHub: https://github.com/mirkoschi22-design
# Ubicación: Roldán, Santa Fe, Argentina
# Año: 2026
# Licencia: MIT License

import secrets
import string

print("🔐 GENERADOR DE CONTRASEÑAS SEGURAS")
print("By Mirko David Schiavi\n")

try:
    longitud = int(input("Longitud de la contraseña (ej: 16): "))
    cantidad = int(input("Cuántas contraseñas querés generar (ej: 5): "))

    caracteres = string.ascii_letters + string.digits + string.punctuation

    print("\n--- CONTRASEÑAS GENERADAS ---\n")
    for i in range(cantidad):
        password = ''.join(secrets.choice(caracteres) for _ in range(longitud))
        print(f"{i+1}. {password}")

    print("\n✅ ¡Hecho! Copiá la que más te guste.")

except ValueError:
    print("❌ Tenés que poner un número.")
def generar_password(longitud=16, mayus=True, numeros=True, simbolos=True):
    """Generador de contraseñas seguras - By Mirko Schiavi"""
    caracteres = string.ascii_lowercase
    
    if mayus:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Usamos secrets para seguridad real
    password = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return password

def main():
    print("🔐 GENERADOR DE CONTRASEÑAS SEGURAS")
    print("By Mirko David Schiavi\n")
    
    try:
        longitud = int(input("Longitud (default 16): ") or 16)
        cantidad = int(input("Cuántas querés generar? (default 5): ") or 5)
        
        print(f"\n--- {cantidad} CONTRASEÑAS GENERADAS ---\n")
        for i in range(cantidad):
            pwd = generar_password(longitud)
            print(f"{i+1}. {pwd}")
            
        print("\n✅ Copiá la que más te guste y no la compartas!")
        
    except ValueError:
        print("❌ Poné solo números, capo")

if __name__ == "__main__":
    main()