

# def send_email_view(request):
#     subject = 'Test Email'
#     message = 'This is a test email sent from Django.'
#     from_email = 'shivmohan.s@zecdata.com'
#     recipient_list = ['shiv8085official@gmail.com']
#     send_mail(subject, message, from_email, recipient_list, fail_silently=False)


# views.py
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponseRedirect

def home_page(request):
    print("home page request")
    friends = ['rahul', 'Aman', 'Rohit', 'Yesh', 'vicky']
    return JsonResponse(friends, safe=False)

def send_email_view(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        recipient_list = request.POST.get('recipient_list', '').split(',')

        # Remove any leading/trailing spaces from email addresses
        recipient_list = [email.strip() for email in recipient_list]

        from_email = 'shivmohan.s@zecdata.com'
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        # Redirect to a page to show that the email has been sent successfully
        return HttpResponseRedirect('/email_sent/')
    
    # If the request method is not POST, render the email form page
    return render(request, 'email_form.html')

def email_sent_view(request):
    # This view simply renders the email_sent.html template
    return render(request, 'email_sent.html')
