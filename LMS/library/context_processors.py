# library/context_processors.py

from django.utils import timezone
from datetime import timedelta
from .models import IssuedBook

def notifications_processor(request):
    # Calculate tomorrow's date
    tomorrow = timezone.now().date() + timedelta(days=1)
    
    # Find all issued books that are due tomorrow
    due_soon_books = IssuedBook.objects.filter(return_date=tomorrow)
    
    # Find all issued books that are overdue
    today = timezone.now().date()
    overdue_books = IssuedBook.objects.filter(return_date__lt=today)
    
    # Combine the counts for the notification badge
    notification_count = due_soon_books.count() + overdue_books.count()
    
    # This dictionary is what gets added to every template's context.
    # It must be returned at the end.
    return {
        'due_soon_books': due_soon_books,
        'overdue_books': overdue_books,
        'notification_count': notification_count
    }