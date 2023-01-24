"""password_api_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from ninja import Schema


class Rule(Schema):
    rule: str
    value: str


class Item(Schema):
    password: str
    rules: list[Rule]


class processedRules(Schema):
    verify: bool
    noMatch: list[str]


api = NinjaAPI()


def process_rules(password, rules):
    noMatch = []
    verify = True
    for rule in rules:
        if rule.rule == "minSize":
            if len(password) < int(rule.value):
                noMatch.append(rule.rule)
                verify = False
        if rule.rule == "minUppercase":
            if sum(1 for char in password if char.isupper()) < int(rule.value):
                noMatch.append(rule.rule)
                verify = False
        if rule.rule == "minLowercase":
            if sum(1 for char in password if char.islower()) < int(rule.value):
                noMatch.append(rule.rule)
                verify = False
        if rule.rule == "minDigit":
            if sum(1 for char in password if char.isdigit()) < int(rule.value):
                noMatch.append(rule.rule)
                verify = False
        if rule.rule == "minSpecialChars":
            if sum(1 for char in password if "!@#$%^&*()-+\/{}[]".find(char)) < int(rule.value):
                noMatch.append(rule.rule)
                verify = False
        if rule.rule == "noRepeted":
            for char in range(1, len(password)):
                if password[char] == password[char-1]:
                    noMatch.append(rule.rule)
                    verify = False
                    break
    return processedRules(verify=verify, noMatch=noMatch)


@api.get("/")
def add(request, item: Item):
    return process_rules(item.password, item.rules)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("verify/", api.urls),
]
