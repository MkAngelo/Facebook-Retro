from django.shortcuts import render

posts = [
    {
        'content': 'Hola a todos esta es una nueva app.',
        'user': {
            'name': 'Miguel Sanchez',
            'picture': 'http://3.bp.blogspot.com/-2Nal4b1K6eg/U0ERumnTTWI/AAAAAAAAhUs/tNThBE-grDY/s1600/Bugs+Bunny+4.jpg'
        },
        'timestamp': 'Posted 12:30 pm',
        'likes':'30',
        'comments': '5',
        'share':'10'
    },
    {
        'content': 'Me esta gustando más esta app que el viejo Facebook.',
        'user': {
            'name': 'Diana UwU',
            'picture': 'https://i2.wp.com/www.bitme.gg/wp-content/uploads/2021/01/Naruto-Chica-realiza-un-cosplay-femenino-de-Naruto-Uzumaki.jpg?fit=1280%2C720&ssl=1'
        },
        'timestamp': 'Posted 2:30 pm',
        'likes':'30',
        'comments': '5',
        'share':'10'
    },
    {
        'content': 'Por fin ganamooooooooooooooossssss :)',
        'user': {
            'name': 'Ludovico Peluche',
            'picture': 'https://yt3.ggpht.com/a/AGF-l79gM-hKd-0McxdM8uLf-FZjO3HM5zYEbseV7A=s900-mo-c-c0xffffffff-rj-k-no'
        },
        'photo': 'https://phantom-marca.unidadeditorial.es/a06edc15a885ee473b2f288147ee88dc/resize/1980/f/jpg/assets/multimedia/imagenes/2021/05/31/16224329675106.jpg',
        'timestamp': 'Posted 2:30 pm',
        'likes':'30',
        'comments': '5',
        'share':'10'
    },
]

def home(request):
    return render(request, 'posts/home.html', {'posts':posts})