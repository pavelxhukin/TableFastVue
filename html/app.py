@app.route('/?')
def schedule_view():
    time_slots = ['09:00-10:00', '10:00-11:00', '11:00-12:00', '12:00-13:00', '13:00-14:00', '14:00-15:00']
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']


    schedule_data = {
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


    return render_template('index.html',
                            time_slots=time_slots,
                            days_of_week=days_of_week,
                            schedule_data=schedule_data)