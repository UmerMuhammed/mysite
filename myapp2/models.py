from django.db import models


class Category(models.Model):
    agent_name = models.CharField(max_length=100)
    selection_type = models.CharField(max_length=100)
    cr_number = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=100)
    contact_person_information = models.CharField(max_length=255)
    customer_email = models.EmailField()
    order_forms = models.FileField(upload_to='order_forms/')
    order_forms_part_2 = models.FileField(upload_to='order_forms/')
    block_number = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    feedback = models.TextField()
    feedback_category = models.CharField(max_length=100, choices=[('good', 'Good'), ('normal', 'Normal')], default='normal')



class Order(models.Model):

    FEEDBACK_CHOICES = [
        ('Good', 'Good'),
        ('Normal', 'Normal'),
    ]
    feedback_category = models.CharField(max_length=10, choices=FEEDBACK_CHOICES, null=True, blank=True)



    AGENT_CHOICES = [
    ('Adriao Sebastiao', 'Adriao Sebastiao'),
    ('Afsal Kottilungal', 'Afsal Kottilungal'),
    ('Faseehullah Khan', 'Faseehullah Khan'),
    ('Kamran Khan', 'Kamran Khan'),
    ('AbdulRehman Tarig', 'AbdulRehman Tarig'),
    ('MD Maruf', 'MD Maruf'),
    ('Manilyn Hicken', 'Manilyn Hicken'),
    ('Mohammad Masud Howlader', 'Mohammad Masud Howlader'),
    ('Mohamed Nadeer Kundani', 'Mohamed Nadeer Kundani'),
    ('Mohammed Ashig', 'Mohammed Ashig'),
    ('Mohammed Biras', 'Mohammed Biras'),
    ('Mohammed Shihab', 'Mohammed Shihab'),
    ('Muhammadshiras Chellattanveedu', 'Muhammadshiras Chellattanveedu'),
    ('Muhammed Jasir', 'Muhammed Jasir'),
    ('Noufal thenginthodi', 'Noufal thenginthodi'),
    ('Reneesh Alakkandy', 'Reneesh Alakkandy'),
    ('Sanjul Padannakara', 'Sanjul Padannakara'),
    ('Shoib Hussain', 'Shoib Hussain'),
    ('Sonu Ravarikandi', 'Sonu Ravarikandi'),
    ('Sumesh Subhash', 'Sumesh Subhash'),
    ('Yasir Riaz', 'Yasir Riaz'),
    ('Satishchandra Yadav', 'Satishchandra Yadav'),
    ('Rajeev TR', 'Rajeev TR'),
    ('Mohammad Omar Faruk', 'Mohammad Omar Faruk'),
    ('Mohammed Ayub Ali', 'Mohammed Ayub Ali'),
    ('Mohamad Kamar S Bepari', 'Mohamad Kamar S Bepari'),
    # Add more names as needed
]

    SELECTION_CHOICES = [
        ('Order Submit', 'Order Submit'),
        ('Visit only', 'Visit only'),
    ]

    agent_name = models.CharField(max_length=100, choices=AGENT_CHOICES)
    selection_type = models.CharField(max_length=100, choices=SELECTION_CHOICES)
    cr_number = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)  # Increased max_length
    phone = models.CharField(max_length=100)
    contact_person_information = models.CharField(max_length=255)  # Increased max_length
    customer_email = models.EmailField()
    order_forms = models.FileField(upload_to='order_forms/')
    order_forms_part_2 = models.FileField(upload_to='order_forms/')
    block_number = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    feedback = models.TextField()  #



    