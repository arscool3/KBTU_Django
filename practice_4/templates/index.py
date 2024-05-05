<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Django Application</title>
</head>
<body>
    <h1>Practice5</h1>
    
    <h2>Authors:</h2>
    <ul>
        {% for author in authors %}
            <li>{{ author.name }}</li>
        {% endfor %}
    </ul>
    
    <h2>Publishers:</h2>
    <ul>
        {% for publisher in publishers %}
            <li>{{ publisher.name }}</li>
        {% endfor %}
    </ul>
    
    <h2>Create a New Book:</h2>
    <form method="post" action="{% url 'create_book' %}">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Create Book</button>
    </form>
</body>
</html>
