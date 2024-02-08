from fastapi import  FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'Message': 'Hello World'}

'''
# Operações e métodos:
    Existem o get, post, put and delete. Os mais usados estão exemplificados abaixo:
'''

@app.get('/home')
def home():
    return {'Message': 'This is home'}

@app.post('/profile')
def profile():
    return {'Message': 'This is your profile'}

'''
# Parametros de rotas:
'''

@app.get('/hello/{nome}')
def hello(nome: str):
    text = f'Hi {nome}, welcome to this place!'
    return {'Message': text}

@app.get('/square/{number}')
def calculate_square(number: int):
    square = number**2
    text = f'The square of {number} is {square}'
    return {'Message': text}

'''
# Parâmetros de Query: O parâmetro é passado na função. A maneira de chamar a f também está especificada abaixo.
'''
@app.get('/double')
def calculate_double(number: int):
    double = 2 * number
    return {f'The double of {number} is {double}'}

# /double?number=4 => Essa é a maneira de executar essa f.

@app.get('/area')
def rectangle_area (width: int, height: int=2):
    area = width * height
    return {f'The are of a rectangle of {width}x{height} is {area}'}
    