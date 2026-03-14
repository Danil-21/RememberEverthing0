from django.shortcuts import render, redirect, get_object_or_404
from .models import Email


# Create your views here.
def send_message(request):
    """
    Отображает форму отправки письма
    Сохраняет письмо в БД
    """

    if request.method == "POST":

        sender = request.POST['sender']
        receiver = request.POST['receiver']
        title = request.POST['title']
        body = request.POST['body']

        Email.objects.create(
            sender=sender,
            receiver=receiver,
            title=title,
            body=body,
            folder='outbox'
        )

        return redirect('/sendMessage')
    
    return render(request, "sendMessage.html")


def view_inbox(request):
    """
    Отображает страницу со входящими письмами
    Передает в шаблон письма с меткой 'inbox'
    """

    emails = Email.objects.filter(folder='inbox')

    context = {
        "emails": emails
    }

    return render(request, "inbox.html", context)


def view_outbox(request):
    """
    Отображает страницу с исходящими письмами
    Передает в шаблон письма с меткой 'outbox'
    """

    emails = Email.objects.filter(folder='outbox')

    context = {
        "emails": emails
    }

    return render(request, "outbox.html", context)


def view_message(request, message_id):
    """
    Отображает страницу с конкретным письмом
    Передает в шаблон письмо по его id

    params:
        message_id: идентификатор письма
    """

    email = get_object_or_404(Email, id=message_id)
    
    if not email.is_read:
        email.is_read = True
        email.save()

    context = {
        "email": email
    }

    return render(request, "viewMessage.html", context)


def move_message(request, message_id):
    """
    Перемещает письмо в архив или корзину

    params:
        message_id: идентификатор письма
    """
        
    email = get_object_or_404(Email, id=message_id)

    new_folder = request.POST['folder']
    email.folder = new_folder
    email.save()

    return redirect("/inbox")


def delete_message(request, message_id):
    """
    Удаляет письмо по его id

    params:
        message_id: идентификатор письма
    """

    email = get_object_or_404(Email, id=message_id)
    email.delete()

    return redirect("/inbox")

def view_archive(request):
    """
    Отображает страницу архива
    Передает в шаблон письма с меткой 'archive'
    """

    emails = Email.objects.filter(folder='archive')

    context = {
        "emails": emails
    }

    return render(request, "archive.html", context)


def view_trash(request):
    """
    Отображает страницу корзины
    Передает в шаблон письма с меткой 'trash'
    """

    emails = Email.objects.filter(folder='trash')

    context = {
        "emails": emails
    }

    return render(request, "trash.html", context)