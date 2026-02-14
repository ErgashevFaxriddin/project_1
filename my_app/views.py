from django.http import HttpResponse


def first_view(request):
    html = f"""
    <h1>Welcome books world!</h1>
    <h2>Main</h2>
    <a href="blog/"> blog >> </a><br> 
    <a href="second/"> second page >> </a><br>
    <a href="pages/Muqaddima/"> Muqaddima </a><br>
    <a href="pages/Ilm%20olish%20sirlari/"> Ilm olish sirlari </a><br>
    <a href="pages/Savdogar%20sahobalar/"> Savdogar sahobalar </a><br>
    <a href="pages/Ulamolar%20nazdida%20vaqtning%20qadri/"> Ulamolar nazdidad vaqtning qadri</a>
    """
    return HttpResponse(html)


def second_view(request):
    html = f"""
    <h1>Second page</h1><br>
    <h2>second</h2>
    
    <a href="/"> << First page </a>
    """
    return HttpResponse(html)


def pages(request, page):
    if page == 'Muqaddima':
        html = f"""
        <h1>{page}</h1>
        <p>
        Muqaddima – Ibn Xaldunning mashhur asari bo‘lib, tarix, jamiyat, siyosat va iqtisodiyot qonuniyatlarini tahlil qiladi. U tarixni sabab‑oqibat bilan o‘rganish, ijtimoiy birdamlik (ʿasabiyyah) va sivilizatsiyalar rivojini tushuntirishga urg‘u beradi. Asar sotsiologiya va tarixshunoslikning poydevorlaridan biri hisoblanadi.
        </p>
        <a href="/"> << First page </a>
        """
    elif page == 'Ilm olish sirlari':
        html = f"""
        <h1>{page}</h1>
        <p>
        Bilim olish jarayoni faqat kitob o‘qish yoki ma’lumot yig‘ish bilan tugamaydi. Asosiy sir – o‘rganayotgan narsangizni ancha chuqur tushunish va amalda qo‘llashdir. Maqsadni aniq belgilash o‘rganish jarayonini samarali qiladi, chunki nima uchun o‘rganayotganingizni bilish diqqatni jamlashga yordam beradi. Takrorlash esa bilimni mustahkamlashning eng qudratli vositasidir, chunki bir marta o‘rganilgan narsalar vaqt o‘tishi bilan unutiladi.
        Diqqatni jamlash va chalg‘ituvchi narsalardan uzoq turish o‘rganishni tezlashtiradi. Nazariyani amaliyot bilan birlashtirish orqali o‘rganilgan bilimlar hayotiy tajribaga aylanadi. Shu bilan birga, o‘z so‘zlaring bilan tushuntirish – o‘rgangan narsani haqiqatan tushunganingizni anglashning eng yaxshi yo‘lidir.
        Oxir-oqibat, sifatli kitoblar va ishonchli manbalar bilan ishlash, savol berish va kichik bo‘laklarga ajratib o‘rganish bilimni tez va samarali egallashning asosiy sirlaridir
        </p>
        <a href="/"> << First page </a>
        """
    elif page == 'Savdogar sahobalar':
        html = f"""
        <h1>{page}</h1>
        <p>
        Islom tarixida bir necha sahobalar savdogarlik bilan shug‘ullangan. Ular halol, adolatli va ishonchli savdogarlar bo‘lib, tijorat orqali nafaqat dunyoviy, balki diniy fazilatlarni ham saqlashgan. Shu orqali ular Mol va savdo jihatidan hamjamiyatga namuna bo‘lgan
        </p>
        <a href="/"> << First page </a>
        """
    elif page == 'Ulamolar nazdida vaqtning qadri':
        html = f"""
        <h1>{page}</h1>
        <p>
        Ulamolar vaqtni eng qimmat ne’mat deb bilishgan. Ular uchun har bir daqiqa hisoblanadi, vaqtni behuda o‘tkazmaslik, ilm o‘rganish, ibodat va foydali ishlar bilan to‘ldirish eng muhim vazifa hisoblangan. Vaqtni to‘g‘ri rejalashtirish va samarali foydalanish – dunyo va oxirat farovonligiga olib boruvchi asosiy omil sifatida qaraladi
        </p>
        <a href="/"> << First page </a>
        """
    else:
        html = f"""
        <h1>Page {page}</h1>
        <h2>Unit {page}</h2>
        <a href="/"> << First page </a>
        """
    return HttpResponse(html)
