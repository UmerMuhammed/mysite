from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from .models import Order,Category
from django.http import JsonResponse


def home(request):
    return render(request, 'home.html')

def form(request):
    return render(request, 'form.html')

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Order

def updateSurvey(request, pk, choice):
    # Retrieve the order object
    order = Order.objects.get(id=pk)

    # Update the feedback category
    order.feedback_category = choice
    order.save()

    # Redirect back to the survey page
    return redirect('/survey')
def save_order(request):
    if request.method == "PATCH" or request.method == "PUT":
        id = request.data.get("id")
        feedback_choice = request.data.get("feedback_choice")
       
    if request.method == 'POST':
        agent_name = request.POST.get('agentName')
        selection_type = request.POST.get('selectionType')
        cr_number = request.POST.get('crNumber')
        company_name = request.POST.get('companyName')
        phone = request.POST.get('phone')
        contact_person_information = request.POST.get('contactPersonInformation')
        customer_email = request.POST.get('customerEmail')
        block_number = request.POST.get('blockNumber')
        location = request.POST.get('location')
        feedback = request.POST.get('feedback')




        # Retrieve PDF files from request.FILES
        order_forms = request.FILES.get('orderForms')
        order_forms_part_2 = request.FILES.get('orderFormsPart2')

        # Save the data into the database
        order = Order.objects.create(
            agent_name=agent_name,
            selection_type=selection_type,
            cr_number=cr_number,
            company_name=company_name,
            phone=phone,
            contact_person_information=contact_person_information,
            customer_email=customer_email,
            block_number=block_number,
            location=location,
            feedback=feedback,
            order_forms=order_forms,
            order_forms_part_2=order_forms_part_2
        )

    category = request.POST.get('feedback')  # Assuming feedback contains 'good' or 'normal'
        
        # Save the data to the appropriate category in the database
    if category in ['good', 'normal']:

        return redirect('/form')  # Redirect to a success URL
    else:
        return redirect('/form')  # Redirect to a success URL




def survey(request):
    # Get the selected category from the request
    category = request.GET.get('category', 'all')
    
    # Filter orders based on the selected category
    if category == 'all':
        orders = Order.objects.all()  # Retrieve all orders
    else:
        orders = Order.objects.filter(feedback=category)  # Filter orders by category

    # Pass the filtered orders to the template
    return render(request, 'survey.html', {'orders': orders, 'category': category})

def clear_table(request):
    try:
        # Delete all entries from the Order table
        Order.objects.all().delete()
        return JsonResponse({'message': 'Table cleared successfully'}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    



def filter_table(request, category):
    orders = Order.objects.filter(feedback_category=category)

    return render(request, 'survey.html', {'orders': orders})

    # Add other category filtering logic as needed

def submitFeedback(request, row_id, feedback):
    if feedback == 'good':
        order = Order.objects.get(id=row_id)
        category = Category.objects.create(
            agent_name=order.agent_name,
            selection_type=order.selection_type,
            cr_number=order.cr_number,
            company_name=order.company_name,
            phone=order.phone,
            contact_person_information=order.contact_person_information,
            customer_email=order.customer_email,
            order_forms=order.order_forms,
            order_forms_part_2=order.order_forms_part_2,
            block_number=order.block_number,
            location=order.location,
            feedback=order.feedback
        )
        # Redi




def submitFeedback(request, order_id, feedback):
    # Retrieve the order object
    order = Order.objects.get(pk=order_id)

    if feedback == 'good':
        # Create an instance of GoodCategory and save the relevant details
        Category.objects.create(
            agent_name=order.agent_name,
            cr_number=order.cr_number,
            company_name=order.company_name,
            # Set other fields accordingly
        )

    # Redirect to the same page or a different page as needed
    return redirect('survey')