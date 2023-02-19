from bs4 import BeautifulSoup

html_doc = """
<html>

<head>
    <title>
        example
    </title>
</head>

<body>
    <ul>
        <li>Главная страница</li>
        <li>Товары</li>
        <li>Контакты</li>
        <li>Корзина</li>
    </ul>
    <div>
        <p>Информация о чем то тут..</p>
        <p>И тут..</p>
    </div>
    <div>
        <input type="text" placeholder="Напиши" class="input-form">
    </div>
</body>

</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.find(class_='input-form'))
