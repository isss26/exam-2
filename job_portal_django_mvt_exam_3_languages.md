# Экзаменационная работа по Django MVT

## Тема экзаменационного проекта: Job Portal / Платформа вакансий

------------------------------------------------------------------------

# ЧАСТЬ I. РУССКИЙ ЯЗЫК

## Цель работы

Создать полноценный Django MVT-проект «Платформа вакансий», в котором
студент покажет, что умеет:

-   работать с архитектурой Django MVT;
-   создавать модели и связи между таблицами;
-   делать страницы через templates;
-   выполнять CRUD через FBV;
-   использовать QuerySet и поиск;
-   реализовать регистрацию и авторизацию;
-   работать с email confirmation, reset password и change password.

## Общее описание проекта

Нужно создать сайт «Платформа вакансий», где пользователи могут:

-   просматривать список вакансий;
-   искать вакансии;
-   фильтровать вакансии;
-   открывать подробную страницу вакансии;
-   добавлять, редактировать и удалять вакансии;
-   регистрироваться, входить и выходить из системы;
-   подтверждать email;
-   менять и сбрасывать пароль.

## Техническое задание

### 1. Структура проекта

Студент должен создать:

-   1 Django project;
-   минимум 1 app.

Проект должен запускаться без ошибок.

### 2. Модели

В проекте должны быть минимум следующие модели:

**1) Category**

Поля:

-   `name`

**2) Company**

Поля:

-   `name`
-   `description`
-   `website`

**3) Job**

Поля:

-   `title`
-   `description`
-   `salary`
-   `location`
-   `employment_type`
-   `created_at`
-   `company` → ForeignKey
-   `category` → ForeignKey
-   `created_by` → ForeignKey на User

**4) Application**

Поля:

-   `job` → ForeignKey
-   `user` → ForeignKey на User
-   `cover_letter`
-   `status`
-   `created_at`

### 3. Связи между моделями

В проекте обязательно должны быть показаны связи:

-   `Job` → `Company`: ForeignKey;
-   `Job` → `Category`: ForeignKey;
-   `Application` → `Job`: ForeignKey;
-   `Application` → `User`: ForeignKey.

Студент должен понимать и показать reverse relation.

Например:

-   у вакансии можно получить все отклики;
-   у компании можно получить все её вакансии;
-   у пользователя можно получить все его отклики.

### 4. Migrations

Студент обязан:

-   создать модели;
-   выполнить `makemigrations`;
-   выполнить `migrate`.

### 5. Admin panel

Через Django admin должно работать CRUD как минимум для:

-   Category;
-   Company;
-   Job;
-   Application.

### 6. Templates

В проекте обязательно должны быть templates:

-   `base.html`
-   главная страница
-   `job_list.html`
-   `job_detail.html`
-   `job_create.html`
-   `job_update.html`
-   `job_delete.html`
-   `register.html`
-   `login.html`
-   `profile.html`

Требования:

-   использовать template inheritance;
-   передавать данные из views в templates;
-   использовать template tags и template filters;
-   подключить static files;
-   настроить media files.

### 7. CRUD через FBV

Для модели `Job` нужно сделать полный CRUD через Function-Based Views:

-   Create
-   Read
-   Update
-   Delete

Обязательно использовать:

-   `render`;
-   `redirect`;
-   `get_object_or_404`;
-   обработку GET и POST.

### 8. QuerySet, filter и search

На странице списка вакансий нужно реализовать:

-   вывод всех вакансий;
-   поиск по названию вакансии;
-   фильтр по категории;
-   фильтр по компании;
-   исключение ненужных данных через `exclude()`;
-   получение одного объекта через `get()` или `get_object_or_404()`.

Нужно использовать следующие методы ORM:

-   `all()`;
-   `get()`;
-   `filter()`;
-   `exclude()`.

Lookup fields, например:

-   `title__icontains`;
-   `salary__gte`;
-   `salary__lte`.

### 9. Reverse relation

На странице детальной информации о вакансии нужно показать:

-   информацию о вакансии;
-   все отклики на эту вакансию;
-   название компании;
-   категорию вакансии.

Студент должен показать, что понимает обратные связи в Django ORM.

### 10. select_related и prefetch_related

В проекте обязательно показать оптимизацию запросов:

-   на странице списка вакансий использовать `select_related()` для
    компании и категории;
-   на странице деталей вакансии использовать `prefetch_related()` для
    откликов.

### 11. Aggregate и annotate

Нужно сделать отдельную страницу «Статистика» или вывести статистику на
главной странице.

Минимум нужно показать:

-   общее количество вакансий;
-   среднюю зарплату по вакансиям;
-   общее количество откликов;
-   количество вакансий у каждой компании.

Использовать:

-   `aggregate()`;
-   `annotate()`.

### 12. Authentication

Нужно реализовать:

-   Register;
-   Login;
-   Logout.

Требования:

-   только зарегистрированный пользователь может добавлять вакансию;
-   только автор записи или администратор может редактировать и удалять
    вакансию;
-   неавторизованный пользователь может только смотреть список и детали
    вакансий.

### 13. Email confirmation

После регистрации пользователь должен подтвердить email.

Для демонстрации можно использовать:

-   console backend;
-   Mailtrap;
-   другой тестовый email backend.

Главное --- показать логику подтверждения email.

### 14. Password features

Обязательно реализовать:

-   Reset password;
-   Change password.

### 15. Дизайн и аккуратность

Требования к оформлению:

-   страницы должны быть аккуратными и понятными;
-   навигация должна быть удобной;
-   код должен быть читаемым;
-   имена переменных и функций должны быть понятными.

### 16. Что нужно сдать

Студент должен сдать:

-   папку с проектом;
-   файл `requirements.txt`;
-   файл `README.md`, где указано:
    -   как запустить проект;
    -   какие есть страницы;
    -   какие функции реализованы;
-   скриншоты основных страниц.

Базу данных SQLite можно оставить в проекте.

### 17. Что студент должен показать на защите

На защите студент должен уметь объяснить:

-   что такое Django;
-   чем MVT отличается от MVC;
-   как request приходит в Django;
-   как работает view;
-   как данные попадают в template;
-   как работают модели и миграции;
-   как работает CRUD;
-   как работают QuerySet и фильтры;
-   как работает авторизация;
-   зачем нужны `select_related`, `prefetch_related`, `aggregate`,
    `annotate`.

## Краткое задание для студентов

Создайте Django-проект «Платформа вакансий», где есть вакансии,
компании, категории и отклики. Реализуйте модели, шаблоны, CRUD для
вакансий через FBV, поиск, фильтрацию, авторизацию, подтверждение email,
смену и сброс пароля. Покажите работу QuerySet, reverse relation,
`select_related`, `prefetch_related`, `aggregate` и `annotate`.

------------------------------------------------------------------------

# PART II. ENGLISH

# Django MVT Examination Project

## Project Topic: Job Portal

## Objective

Create a complete Django MVT project called "Job Portal" to demonstrate
the ability to:

-   work with the Django MVT architecture;
-   create models and relationships between database tables;
-   build pages using templates;
-   implement CRUD operations using Function-Based Views (FBVs);
-   use QuerySets and search functionality;
-   implement user registration and authentication;
-   work with email confirmation, password reset, and password change.

## Project Overview

Create a "Job Portal" website where users can:

-   view a list of job vacancies;
-   search for vacancies;
-   filter vacancies;
-   open a detailed vacancy page;
-   add, edit, and delete vacancies;
-   register, log in, and log out;
-   confirm their email address;
-   change and reset their password.

## Technical Requirements

### 1. Project Structure

The student must create:

-   1 Django project;
-   at least 1 app.

The project must run without errors.

### 2. Models

The project must contain at least the following models:

**1) Category**

Fields:

-   `name`

**2) Company**

Fields:

-   `name`
-   `description`
-   `website`

**3) Job**

Fields:

-   `title`
-   `description`
-   `salary`
-   `location`
-   `employment_type`
-   `created_at`
-   `company` → ForeignKey
-   `category` → ForeignKey
-   `created_by` → ForeignKey to User

**4) Application**

Fields:

-   `job` → ForeignKey
-   `user` → ForeignKey to User
-   `cover_letter`
-   `status`
-   `created_at`

### 3. Model Relationships

The project must demonstrate the following relationships:

-   `Job` → `Company`: ForeignKey;
-   `Job` → `Category`: ForeignKey;
-   `Application` → `Job`: ForeignKey;
-   `Application` → `User`: ForeignKey.

The student must understand and demonstrate reverse relationships.

For example:

-   retrieve all applications for a job;
-   retrieve all jobs belonging to a company;
-   retrieve all applications submitted by a user.

### 4. Migrations

The student must:

-   create the models;
-   run `makemigrations`;
-   run `migrate`.

### 5. Admin Panel

CRUD operations must work in Django admin for at least:

-   Category;
-   Company;
-   Job;
-   Application.

### 6. Templates

The project must include the following templates:

-   `base.html`
-   home page
-   `job_list.html`
-   `job_detail.html`
-   `job_create.html`
-   `job_update.html`
-   `job_delete.html`
-   `register.html`
-   `login.html`
-   `profile.html`

Requirements:

-   use template inheritance;
-   pass data from views to templates;
-   use template tags and template filters;
-   configure static files;
-   configure media files.

### 7. CRUD Using FBVs

Implement complete CRUD functionality for the `Job` model using
Function-Based Views:

-   Create
-   Read
-   Update
-   Delete

The implementation must use:

-   `render`;
-   `redirect`;
-   `get_object_or_404`;
-   GET and POST request handling.

### 8. QuerySet, Filtering, and Search

The job list page must provide:

-   displaying all job vacancies;
-   searching by job title;
-   filtering by category;
-   filtering by company;
-   excluding unnecessary records using `exclude()`;
-   retrieving a single object using `get()` or `get_object_or_404()`.

The following ORM methods must be used:

-   `all()`;
-   `get()`;
-   `filter()`;
-   `exclude()`.

Example lookup fields:

-   `title__icontains`;
-   `salary__gte`;
-   `salary__lte`.

### 9. Reverse Relationships

The job detail page must display:

-   job information;
-   all applications submitted for that job;
-   the company name;
-   the job category.

The student must demonstrate an understanding of reverse relationships
in the Django ORM.

### 10. select_related and prefetch_related

The project must demonstrate query optimization:

-   use `select_related()` for the company and category on the job list
    page;
-   use `prefetch_related()` for applications on the job detail page.

### 11. Aggregate and annotate

Create a separate "Statistics" page or display statistics on the home
page.

At minimum, display:

-   the total number of job vacancies;
-   the average salary across vacancies;
-   the total number of applications;
-   the number of vacancies belonging to each company.

Use:

-   `aggregate()`;
-   `annotate()`.

### 12. Authentication

Implement:

-   Register;
-   Login;
-   Logout.

Requirements:

-   only registered users can add job vacancies;
-   only the creator of a vacancy or an administrator can edit and
    delete it;
-   unauthenticated users can only view the job list and job details.

### 13. Email Confirmation

After registration, the user must confirm their email address.

For demonstration purposes, students may use:

-   console email backend;
-   Mailtrap;
-   another test email backend.

The main requirement is to demonstrate the email confirmation logic.

### 14. Password Features

The following features are required:

-   Reset password;
-   Change password.

### 15. Design and Code Quality

Requirements:

-   pages must be clean and easy to understand;
-   navigation must be convenient;
-   code must be readable;
-   variable and function names must be meaningful.

### 16. Submission Requirements

The student must submit:

-   the project folder;
-   a `requirements.txt` file;
-   a `README.md` file explaining:
    -   how to run the project;
    -   which pages are available;
    -   which features have been implemented;
-   screenshots of the main pages.

The SQLite database may be included in the project.

### 17. What the Student Must Demonstrate During the Defense

During the defense, the student must be able to explain:

-   what Django is;
-   the difference between MVT and MVC;
-   how a request reaches Django;
-   how a view works;
-   how data is passed to a template;
-   how models and migrations work;
-   how CRUD works;
-   how QuerySets and filters work;
-   how authentication works;
-   why `select_related`, `prefetch_related`, `aggregate`, and
    `annotate` are used.

## Short Assignment for Students

Create a Django project called "Job Portal" containing job vacancies,
companies, categories, and applications. Implement models, templates,
CRUD operations for job vacancies using FBVs, search, filtering,
authentication, email confirmation, password change, and password reset.
Demonstrate the use of QuerySets, reverse relationships,
`select_related`, `prefetch_related`, `aggregate`, and `annotate`.

------------------------------------------------------------------------

# ҚИСМИ III. ЗАБОНИ ТОҶИКӢ

# Кори имтиҳонӣ аз фанни Django MVT

## Мавзӯи лоиҳаи имтиҳонӣ: Job Portal / Платформаи ҷойҳои корӣ

## Мақсади кор

Сохтани лоиҳаи пурраи Django MVT бо номи «Платформаи ҷойҳои корӣ», ки
дар он донишҷӯ бояд малакаҳои зеринро нишон диҳад:

-   кор бо меъмории Django MVT;
-   сохтани моделҳо ва робитаҳо байни ҷадвалҳои базаи маълумот;
-   сохтани саҳифаҳо бо истифода аз templates;
-   иҷрои CRUD тавассути Function-Based Views (FBV);
-   истифодаи QuerySet ва ҷустуҷӯ;
-   амалӣ кардани бақайдгирӣ ва авторизатсия;
-   кор бо тасдиқи email, барқарорсозии парол ва иваз кардани парол.

## Тавсифи умумии лоиҳа

Бояд сомонаи «Платформаи ҷойҳои корӣ» сохта шавад, ки дар он
истифодабарандагон имконият доранд:

-   рӯйхати ҷойҳои кориро бинанд;
-   ҷойҳои кориро ҷустуҷӯ кунанд;
-   ҷойҳои кориро аз рӯйи шартҳои муайян филтр кунанд;
-   саҳифаи муфассали ҳар як ҷойи кориро кушоянд;
-   ҷойи нави корӣ илова, таҳрир ва нест кунанд;
-   дар сомона сабти ном шаванд, ворид ва хориҷ шаванд;
-   email-и худро тасдиқ кунанд;
-   паролро иваз ё барқарор намоянд.

## Талаботи техникӣ

### 1. Сохтори лоиҳа

Донишҷӯ бояд созад:

-   1 Django project;
-   ҳадди ақал 1 app.

Лоиҳа бояд бе ягон хато фаъол шавад.

### 2. Моделҳо

Дар лоиҳа бояд ҳадди ақал моделҳои зерин мавҷуд бошанд:

**1) Category**

Майдонҳо:

-   `name`

**2) Company**

Майдонҳо:

-   `name`
-   `description`
-   `website`

**3) Job**

Майдонҳо:

-   `title`
-   `description`
-   `salary`
-   `location`
-   `employment_type`
-   `created_at`
-   `company` → ForeignKey
-   `category` → ForeignKey
-   `created_by` → ForeignKey ба User

**4) Application**

Майдонҳо:

-   `job` → ForeignKey
-   `user` → ForeignKey ба User
-   `cover_letter`
-   `status`
-   `created_at`

### 3. Робитаҳои байни моделҳо

Дар лоиҳа ҳатман бояд робитаҳои зерин нишон дода шаванд:

-   `Job` → `Company`: ForeignKey;
-   `Job` → `Category`: ForeignKey;
-   `Application` → `Job`: ForeignKey;
-   `Application` → `User`: ForeignKey.

Донишҷӯ бояд робитаҳои баръаксро фаҳмад ва дар амал нишон диҳад.

Масалан:

-   гирифтани ҳамаи дархостҳо барои як ҷойи корӣ;
-   гирифтани ҳамаи ҷойҳои кории як ширкат;
-   гирифтани ҳамаи дархостҳои як истифодабаранда.

### 4. Migrations

Донишҷӯ вазифадор аст:

-   моделҳоро созад;
-   фармони `makemigrations`-ро иҷро кунад;
-   фармони `migrate`-ро иҷро кунад.

### 5. Admin panel

Дар Django admin барои моделҳои зерин бояд CRUD кор кунад:

-   Category;
-   Company;
-   Job;
-   Application.

### 6. Templates

Дар лоиҳа бояд templates-и зерин мавҷуд бошанд:

-   `base.html`
-   саҳифаи асосӣ
-   `job_list.html`
-   `job_detail.html`
-   `job_create.html`
-   `job_update.html`
-   `job_delete.html`
-   `register.html`
-   `login.html`
-   `profile.html`

Талабот:

-   истифодаи template inheritance;
-   интиқол додани маълумот аз views ба templates;
-   истифодаи template tags ва template filters;
-   пайваст кардани static files;
-   танзим кардани media files.

### 7. CRUD тавассути FBV

Барои модели `Job` бояд CRUD-и пурра тавассути Function-Based Views
амалӣ карда шавад:

-   Create;
-   Read;
-   Update;
-   Delete.

Истифодаи ҳатмӣ:

-   `render`;
-   `redirect`;
-   `get_object_or_404`;
-   коркарди дархостҳои GET ва POST.

### 8. QuerySet, filter ва search

Дар саҳифаи рӯйхати ҷойҳои корӣ бояд имкониятҳои зерин амалӣ карда
шаванд:

-   нишон додани ҳамаи ҷойҳои корӣ;
-   ҷустуҷӯ аз рӯйи номи ҷойи корӣ;
-   филтр аз рӯйи категория;
-   филтр аз рӯйи ширкат;
-   хориҷ кардани маълумоти нолозим бо истифода аз `exclude()`;
-   гирифтани як объект бо истифода аз `get()` ё `get_object_or_404()`.

Методҳои зерини ORM бояд истифода шаванд:

-   `all()`;
-   `get()`;
-   `filter()`;
-   `exclude()`.

Намунаҳои lookup fields:

-   `title__icontains`;
-   `salary__gte`;
-   `salary__lte`.

### 9. Reverse relation

Дар саҳифаи маълумоти муфассали ҷойи корӣ бояд нишон дода шаванд:

-   маълумоти ҷойи корӣ;
-   ҳамаи дархостҳои пешниҳодшуда барои ин ҷойи корӣ;
-   номи ширкат;
-   категорияи ҷойи корӣ.

Донишҷӯ бояд нишон диҳад, ки робитаҳои баръаксро дар Django ORM
мефаҳмад.

### 10. select_related ва prefetch_related

Дар лоиҳа ҳатман оптимизатсияи дархостҳои базаи маълумот нишон дода
шавад:

-   дар саҳифаи рӯйхати ҷойҳои корӣ барои ширкат ва категория
    `select_related()` истифода шавад;
-   дар саҳифаи муфассали ҷойи корӣ барои дархостҳо `prefetch_related()`
    истифода шавад.

### 11. Aggregate ва annotate

Саҳифаи алоҳида бо номи «Омор» сохта шавад ё омор дар саҳифаи асосӣ
нишон дода шавад.

Ҳадди ақал маълумоти зерин бояд нишон дода шавад:

-   шумораи умумии ҷойҳои корӣ;
-   маоши миёнаи ҷойҳои корӣ;
-   шумораи умумии дархостҳо;
-   шумораи ҷойҳои кории ҳар як ширкат.

Истифодаи методҳои зерин ҳатмист:

-   `aggregate()`;
-   `annotate()`.

### 12. Authentication

Бояд имкониятҳои зерин амалӣ карда шаванд:

-   Register;
-   Login;
-   Logout.

Талабот:

-   танҳо истифодабарандаи сабти номшуда метавонад ҷойи нави корӣ илова
    кунад;
-   танҳо муаллифи эълон ё администратор метавонад ҷойи кориро таҳрир ё
    нест кунад;
-   истифодабарандаи авторизатсиянашуда танҳо рӯйхат ва маълумоти
    муфассали ҷойҳои кориро дида метавонад.

### 13. Email confirmation

Пас аз бақайдгирӣ истифодабаранда бояд email-и худро тасдиқ кунад.

Барои намоиш додани ин имконият истифода бурдан мумкин аст аз:

-   console backend;
-   Mailtrap;
-   дигар email backend-и тестӣ.

Муҳим он аст, ки мантиқи тасдиқи email амалӣ карда шавад.

### 14. Password features

Амалӣ кардани имкониятҳои зерин ҳатмист:

-   Reset password --- барқарор кардани парол;
-   Change password --- иваз кардани парол.

### 15. Дизайн ва тартиби код

Талабот ба намуди зоҳирӣ ва код:

-   саҳифаҳо бояд зебо, фаҳмо ва ботартиб бошанд;
-   паймоиш дар сомона бояд қулай бошад;
-   код бояд хонданбоб бошад;
-   номҳои тағйирёбандаҳо ва функсияҳо бояд фаҳмо бошанд.

### 16. Чӣ бояд супорида шавад

Донишҷӯ бояд маводи зеринро супорад:

-   папкаи лоиҳа;
-   файли `requirements.txt`;
-   файли `README.md`, ки дар он нишон дода шудааст:
    -   чӣ тавр лоиҳаро фаъол кардан мумкин аст;
    -   кадом саҳифаҳо мавҷуданд;
    -   кадом имкониятҳо амалӣ карда шудаанд;
-   скриншотҳои саҳифаҳои асосӣ.

Базаи маълумотии SQLite метавонад дар дохили лоиҳа нигоҳ дошта шавад.

### 17. Донишҷӯ дар вақти ҳимоя бояд чиро нишон диҳад

Дар вақти ҳимоя донишҷӯ бояд мафҳумҳои зеринро фаҳмонад:

-   Django чист;
-   фарқи MVT аз MVC дар чист;
-   request чӣ тавр ба Django ворид мешавад;
-   view чӣ тавр кор мекунад;
-   маълумот чӣ тавр ба template интиқол дода мешавад;
-   моделҳо ва migrations чӣ тавр кор мекунанд;
-   CRUD чӣ тавр кор мекунад;
-   QuerySet ва филтрҳо чӣ тавр кор мекунанд;
-   авторизатсия чӣ тавр кор мекунад;
-   `select_related`, `prefetch_related`, `aggregate` ва `annotate`
    барои чӣ лозиманд.

## Супориши кӯтоҳ барои донишҷӯён

Лоиҳаи Django бо номи «Платформаи ҷойҳои корӣ» созед, ки дар он ҷойҳои
корӣ, ширкатҳо, категорияҳо ва дархостҳо мавҷуд бошанд. Моделҳо,
шаблонҳо, CRUD барои ҷойҳои корӣ тавассути FBV, ҷустуҷӯ, филтркунӣ,
авторизатсия, тасдиқи email, иваз ва барқарор кардани паролро амалӣ
намоед. Истифодаи QuerySet, reverse relation, `select_related`,
`prefetch_related`, `aggregate` ва `annotate`-ро нишон диҳед.
