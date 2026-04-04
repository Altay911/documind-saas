from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Document
from .forms import DocumentForm
from .utils import ask_ai_about_pdf
from django.shortcuts import render, redirect, get_object_or_404
from .models import Document, APIUsage
from datetime import date

@login_required
def dashboard_home(request):
    # 1. Handle File Uploads
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # Pause the save! We need to attach the logged-in user first.
            doc = form.save(commit=False)
            doc.user = request.user
            doc.save()
            return redirect('dashboard_home') # Refresh the page to show the new file
    else:
        # If they are just visiting, give them an empty form
        form = DocumentForm()

    # 2. Fetch the User's Documents
    # This filters the database so a user ONLY sees their own PDFs, sorted by newest first
    user_docs = Document.objects.filter(user=request.user).order_by('-uploaded_at')

    # 3. Send the form and the documents to the HTML template
    context = {
        'form': form,
        'documents': user_docs
    }
    return render(request, 'dashboard/home.html', context)


def register(request):
    # ... (Keep your existing register function exactly as it is)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        
    return render(request, 'registration/register.html', {'form': form})

@login_required
def chat_with_pdf(request, doc_id):
    document = get_object_or_404(Document, id=doc_id, user=request.user)
    answer = ""
    error_message = ""
    
    # 1. Get their usage tracker (or create one if they are a brand new user)
    usage, created = APIUsage.objects.get_or_create(user=request.user)
    
    # 2. If it is a brand new day, reset their counter to 0!
    if usage.last_query_date != date.today():
        usage.queries_today = 0
        usage.last_query_date = date.today()
        usage.save()
        
    # Calculate how many free questions they have left
    DAILY_LIMIT = 20
    queries_left = DAILY_LIMIT - usage.queries_today

    if request.method == "POST":
        # 3. THE BOUNCER: Check if they are out of credits
        if usage.queries_today >= DAILY_LIMIT:
            error_message = "You have reached your daily limit of 5 free questions. Please come back tomorrow!"
        else:
            user_question = request.POST.get('question')
            pdf_path = document.uploaded_file.path
            
            answer = ask_ai_about_pdf(pdf_path, user_question)
            
            # 4. Success! Deduct a credit and save to database
            usage.queries_today += 1
            usage.save()
            queries_left = DAILY_LIMIT - usage.queries_today
        
    return render(request, 'dashboard/chat.html', {
        'document': document, 
        'answer': answer,
        'error_message': error_message,
        'queries_left': queries_left
    })

@login_required
def delete_document(request, doc_id):
    if request.method == 'POST':
        # Safely grab the document, ensuring it belongs to the logged-in user
        doc = get_object_or_404(Document, id=doc_id, user=request.user)
        # Delete the physical PDF from the Mac
        doc.uploaded_file.delete()
        # Delete the record from the Database
        doc.delete()
    return redirect('dashboard_home')

@login_required
def rename_document(request, doc_id):
    if request.method == 'POST':
        doc = get_object_or_404(Document, id=doc_id, user=request.user)
        new_title = request.POST.get('new_title')
        if new_title:
            doc.title = new_title
            doc.save()
    return redirect('dashboard_home')