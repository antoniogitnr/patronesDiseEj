class TokenGenerator:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def generate_token(self):
        # Aquí puedes agregar la lógica para generar tu token
        token = "tu_token_generado"
        return token

# Ejemplo de uso
token_generator = TokenGenerator()
token = token_generator.generate_token()
print(token)