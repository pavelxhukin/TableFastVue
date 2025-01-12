from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def get_hi():
    return 'hello from user app'

@app.get("/tables")
async def get_tables():
    return {
        'Monday': [
            {'time': '09:00-10:00', 'title': 'Математика', 'cabinet': '101', 'now': True}
        ],
        'Tuesday': [
            {'time': '10:00-11:00', 'title': 'Физика', 'cabinet': '205'},
            {'time': '14:00-15:00', 'title': 'Лабораторная', 'cabinet': '210'}
        ],
        'Wednesday': [
            {'time': '11:00-12:00', 'title': 'Встреча с куратором', 'cabinet': '302'}
        ],
        'Thursday': [],
        'Friday': [
              {'time': '09:00-10:00', 'title': 'Английский язык', 'cabinet': '107'},
              {'time': '13:00-14:00', 'title': 'История', 'cabinet': '110'}
          ]
      }