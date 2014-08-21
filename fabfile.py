from fabric.api import local

def prepare_deployment():
    local('python manage.py test observer')
    # local('git add -p && git commit') # or local('hg add && hg commit')
