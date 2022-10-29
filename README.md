# EPI-HELP


Design for Mobile app
---------------------
+ Figma: https://www.figma.com/file/nHnH8UV0BUxbRlYUiH6Rzz/Epi-help?node-id=226%3A165

--------------------------------------------------------------------


# Documentation for EPI-HELP!

Singup | Login
--------------
* POST: http://127.0.0.1:8000/account/register/ - Registration
* POST: http://127.0.0.1:8000/account/login/ - Login
* POST: http://127.0.0.1:8000/account/login/refresh/ - Token refresh

--------------------------------------------------------------------

Content
-------
* GET: http://127.0.0.1:8000/api/content/ - Content list
* GET: http://127.0.0.1:8000/api/content/<id> - Content

--------------------------------------------------------

Contact
-------
* POST: http://127.0.0.1:8000/api/contact/ - Add contact
* GET: http://127.0.0.1:8000/api/contact/ - Contact list
* PUT: http://127.0.0.1:8000/api/contact/<id> - Update contact
* DELETE: http://127.0.0.1:8000/api/contact/<id> - Delete contact

------------------------------------------------------------------

Type Trigger
------------
* POST: http://127.0.0.1:8000/api/type-trigger/ - Add type trigger
* GET: http://127.0.0.1:8000/api/type-trigger/ - Type trigger list
* GET: http://127.0.0.1:8000/api/type-trigger/<id> - Type trigger by index

-----------------------------------------------------------------

Type Seizure
------------
* POST: http://127.0.0.1:8000/api/type-seizure/ - Add type seizure
* GET: http://127.0.0.1:8000/api/type-seizure/ - Type seizure list
* GET: http://127.0.0.1:8000/api/type-seizure/<id> - Type seizure by index

-----------------------------------------------------------------

Type Aura
---------
* POST: http://127.0.0.1:8000/api/type-aura/ - Add type aura
* GET: http://127.0.0.1:8000/api/type-aura/ - Type aura list
* GET: http://127.0.0.1:8000/api/type-aura/<id> - Type aura by index

--------------------------------------------------------------------

Report Event
------------
* POST: http://127.0.0.1:8000/api/report-event/ - Add Report event
* GET: http://127.0.0.1:8000/api/report-event/ - Report event list
* GET: http://127.0.0.1:8000/api/report-event/<id> - Report event by index

-----------------------------------------------------------------

Seizure
------------
* POST: http://127.0.0.1:8000/api/seizure/ - Add seizure
* GET: http://127.0.0.1:8000/api/seizure/ - Seizure list
* GET: http://127.0.0.1:8000/api/seizure/<id> - Seizure by index

-----------------------------------------------------------------

Aura
---------
* POST: http://127.0.0.1:8000/api/aura/ - Add aura
* GET: http://127.0.0.1:8000/api/aura/ - Aura list
* GET: http://127.0.0.1:8000/api/aura/<id> - Aura by index

--------------------------------------------------------------------

General Settings
----------------
* PUT: http://127.0.0.1:8000/api/general-settings/ - Update settings

--------------------------------------------------------------------

My Profile
----------------
* PUT: http://127.0.0.1:8000/api/my-profile/ - Update profile

--------------------------------------------------------------------
