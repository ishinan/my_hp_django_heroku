# Django Own Homepage Project

- This project is to port my_homepage generated from a static site generator to Django web framework.
- The lastest site is available at http://masayana.herokuapp.com in Heroku service

## Main pages

- **Home** page
  - A welcome page with my short profile
- **Projects** page
  - Summary of my project. Currently there is no real project displayed
- **Blog** page
  - Summary of my blog. Currently there  is no real blog available
    - Click a blog link to go to each blog page (Currently not linked)
- **Github** Repo page
  - List my github public repo with its last updated date information
- **Contact** Me page
  - Sending email to me and send a confirmation to the sender

## Python Modules  

- Python 3.7
- Django web framework
  - This site is using django open source web framework
- Jinja2 templating
  - Instead of using Django template, I'm using Jinja2 tempalte. 
  - [Here](https://www.dyspatch.io/blog/python-templating-performance-showdown-django-vs-jinja/) is a link to an interesting article about the comparisen between the two python templates.
- Markdown plain text markup language
  - Content files for blogs are using markdown format to include metadata
- External APIs
  - github Repository: accessing my github repository data
  - Mailgun: Sending emails from **Contact** page