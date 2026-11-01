# Test Run Output

Run:

python manage.py test

Actual output:
----------------------------------------------------------------------

(venv) PS C:\Users\Vishnu\Desktop\box_selection_system> python manage.py test           
Found 9 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.........
----------------------------------------------------------------------
Ran 9 tests in 0.070s

OK
Destroying test database for alias 'default'...


### Test Cases – AI-Assisted Box Selection System
1. Product Management Test Cases
----------------------------------------------------------------------------------------------
Test ID	                Test scenario	                             Expected result

TC01	    Create a product with valid details	            Product should be created successfully
TC02	    Create a product with missing name	            Validation error should appear
TC03	    Enter negative product dimensions	            Product should be rejected
TC04	    Enter zero product weight	                    Product should be rejected
TC05	    Update existing product details	                Product should be updated
TC06	    Delete an existing product	                    Product should be deleted if relationships allow it

2. Box Management Test Cases
----------------------------------------------------------------------------------------------------
Test ID	                Test scenario	                               Expected result

TC07	    Create a box with valid dimensions	             Box should be created successfully
TC08	    Enter negative box dimensions	                 Validation error should appear
TC09	    Enter invalid maximum weight capacity	         Box should be rejected
TC10	    Enter negative box cost	                         Box should be rejected
TC11	    Update box dimensions	                         Box details should be updated
TC12	    Delete an existing box	                         Box should be deleted if relationships allow it

3. Order Management Test Cases
---------------------------------------------------------------------------------------------------------------
Test ID	                Test scenario	                               Expected result

TC13	    Create an order with valid products	                Order should be created
TC14	    Add multiple products to an order	                All products should be associated with the order
TC15	    Add a product with quantity greater than zero	    Order item should be created
TC16	    Add a product with zero quantity	                Validation error should appear
TC17	    Add a product with negative quantity	            Validation error should appear
TC18	    Calculate total order weight	                    Total weight should be calculated correctly
TC19	    Retrieve order details	                            Correct order and product information should appear

4. Box Selection Algorithm Test Cases
------------------------------------------------------------------------------------------------------------------
Test ID	                Test scenario	                                Expected result

TC20	    Single product fits inside a box	                Suitable box should be recommended
TC21	    Product fits only after rotation	                Algorithm should identify a valid orientation
TC22	    Product dimensions exceed all available boxes	    No suitable box should be returned
TC23	    Order weight exceeds box capacity	                Box should be rejected
TC24	    Multiple products fit inside one box	            Box should be recommended
TC25	    Multiple products overlap during placement	        Invalid packing arrangement should be rejected
TC26	    Multiple products fit individually but not together	Box should be rejected
TC27	    Different product quantities are added	            All product quantities should be considered
TC28	    Multiple suitable boxes have different costs	    Cheapest valid box should be selected
TC29	    Multiple suitable boxes have the same cost	        A valid box should be selected consistently
TC30	    No available boxes exist	                        Appropriate no-box-found message should appear
TC31	    Empty order is submitted for recommendation	        Appropriate validation error should appear

5. Django Admin Test Cases
------------------------------------------------------------------------------------------------------------------
Test ID	                Test scenario	                                 Expected result

TC32	Login using valid admin credentials	                    Admin dashboard should open
TC33	Login using invalid credentials	                        Authentication should fail
TC34	View registered Product model	                        Product records should appear
TC35	Manage Box records	                                    Admin should be able to manage boxes
TC36	Manage Order records	                                Order information should appear
TC37	View OrderItem inline records	                        Associated order items should appear

6. Database and Migration Test Cases
------------------------------------------------------------------------------------------------------------------
Test ID	                Test scenario	                                  Expected result

TC38	Run makemigrations	                                    Migration files should be generated
TC39	Run migrate	                                            Database tables should be created
TC40	Retrieve Product records using Django ORM	            Product records should be returned
TC41	Restart the application	                                Existing database records should remain available
TC42	Verify foreign-key relationships	                    Related records should be retrieved correctly

7. Frontend and Integration Test Cases
------------------------------------------------------------------------------------------------------------------
Test ID	                Test scenario	                                Expected result

TC43	Open dashboard	                                        Dashboard should display correctly
TC44	Navigate between application pages	                    Navigation should work
TC45	Submit product creation form	                        Product should be saved
TC46	Submit box creation form	                            Box should be saved
TC47	Create an order through the frontend	                Order should be saved
TC48	Request a box recommendation	                        Recommendation results should appear
TC49	Submit invalid form information	                        Validation messages should appear
TC50	Access application on mobile screen	                    Layout should adjust responsively

Environment:
----------------------------------------------------------------------
- Python version: 3.13.14
- Django version: 5.2.18
- Operating system: windows
- Date tested: 01/11/2026
