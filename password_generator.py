import random
import string
import secrets

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