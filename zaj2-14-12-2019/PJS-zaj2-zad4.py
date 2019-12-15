#Exercise 1. Build a grant webpage using Jinja2
# It should consist of block and extends tags for template inheritance. The following features should be implemented:
#    footer should be added to the layouts,
#    create one layout that adds with block the following partials: the menu, current page name and the content (below),
#    the content can be a list of grants, the grant details page, deletion page.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
 {% include 'menu.html' %}
 {% block content %}{% endblock %}
 {% include 'footer.html' %}
</body>
</html>

In [ ]:

<a href="/list_of_grants">List of grants</a>
<a href="/add_grant">List of grants</a>
<a href="/delete_grant">List of grants</a>
<a href="/show_grant">List of grants</a>

In [ ]:

<div id="footer">This is the footer</div>

In [ ]:

<h1>Grants</h1>
{% for grant in grants %}
  <h3>{{ grant.title }}</h3>
  <span class="date">{{ grant.date }}</span>
  {{ grant.description }}
{% endfor %}



