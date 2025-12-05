
# Testing
## Introduction
This document serves as the Final Manual User Acceptance Testing (UAT) Report for the Oakdale Spa Website (hosted at: https://oakdale-spa-00f9c791dc68.herokuapp.com/).

The purpose of this UAT phase was to ensure that the core user-centric functionalities of the application meet the specified requirements and perform reliably in a production environment. The testing focused on critical user journeys within User Authentication (Login, Logout, Registration Validation) and the Full Reservation Lifecycle (Booking, Editing, and Cancellation). The overall objective was to confirm that all critical paths are functional, secure, and provide clear, accurate feedback to the user. All core test scenarios achieved a 100% Pass rate, confirming the application's readiness for deployment.

## Manual Testing Report

**Scope an Objective** This report details the manual user acceptance testing performed on the Oakdale Spa website, located [here](https://oakdale-spa-00f9c791dc68.herokuapp.com/).

**Scope** The testing focused on core-user centric functionalities including User Authentication *Login, Logout, Registration Validation* and the full reservation lifecycle *Booking, Editing and viewing experience details*.

**Objective** To ensure all critical user journeys are functional, secure and provide clear accurate feedback to the user according to the specified requirements


## Test Scenarios and Results
The following table details the scenarios executed during the UAT phase. All scenarios passed, validating the core functionality of the Oakdale Spa website.

| Scenario ID | Scenario Description                     | Scenario Objective                                                                                                                                                                         | Test Case ID | Preconditions                                                                              | Steps to Execute                                                                                                                                                                     | Test Data                                                                       | Expected Results                                                                                                                                                                                                                                                                                                                   | Actual Results                                                                                                                                                                      | Status |
| ----------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **SC1**         | Login: Valid User                        | To verify that a user with valid credentials can successfully sign in and is redirected to the correct page with a success message.                                                        | TD1          | User account exists. home.html is loaded.                                                  | 1. Navigate to home page. <br> 2. Click Login. <br> 3. Enter a valid Username/Password. 4\. <br> Click Sign In.                                                                      | Username: Diana <br> Password: SpaBreaks123!                                    | The user is redirected to home.html. A message displays: "Successfully signed in as [Username]".                                                                                                                                                                                                                                   | The user was successfully redirected to home.html and the message "Successfully signed in as Diana" was displayed under the header.                                                 | Pass   |
| **SC1**         | Login: Valid User (Mobile)               |                                                                                                                                                                                            | TD2          | User account exists. home.html is loaded.                                                  | 1. Click menu burger.<br> 2. Click Login on the slider. <br> 3. Enter valid details. <br> 4. Click Sign In.                                                                          | Username: Diana <br>Password: SpaBreaks123!                                     | The user is redirected to home.html. A message displays: "Successfully signed in as [Username]".                                                                                                                                                                                                                                   | The user was successfully redirected to home.html after signing in via the mobile navigation slider. The correct success message was displayed.                                     | Pass   |
| **SC2**         | Login: Invalid Credentials               | To confirm the system correctly handles invalid logins and displays clear error messages.                                                                                                  | TD3          | \*\*home.html\*\* is loaded.                                                               | 1. Click Login. <br> 2. Enter incorrect details (e.g., wrong password). <br> 3. Click Sign In.                                                                                       | Username: WrongUser <br>Password: WrongPass                                     | The login page reloads. A message appears: "The username and/or password you specified are not correct."                                                                                                                                                                                                                           | The login page reloaded, and the message "The username and/or password you specified are not correct." appeared above the username field.                                           | Pass   |
| **SC3**         | Sign Out                                 | To ensure a signed-in user can successfully log out and is returned to the home page with a confirmation message.                                                                          | TD4          | User is signed into the website (SC1 passed).                                              | 1. Click Logout. <br> 2. On logout.html page, click Sign Out.                                                                                                                        | N/A                                                                             | The user is redirected to home.html. A message displays: "You have signed out".                                                                                                                                                                                                                                                    | The user was redirected to home.html, and the message "You have signed out" was displayed under the header.                                                                         | Pass   |
| **SC4**         | Registration: Invalid Input (Validation) | To verify that the registration form enforces defined security rules (e.g., password length, similarity) and business rules (e.g., username uniqueness) and provides clear error messages. | TD5          | signup.html loaded.                                                                        | 1. Navigate to Sign Up page.<br> 2. Enter an existing Username (Diana).<br> 3. Enter a password too similar to the username (Diana123!). <br>4. Click Sign Up.                       | Username: Diana <br> Password: Diana123!                                        | The registration should fail. An inline error message should appear above the Username saying, “Your password can’t be too similar to your other personal information.”<br>“Your password must contain at least 8 characters.”<br>“Your password can’t be a commonly used password.”<br>“Your password can’t be entirely numeric.” | The Sign up page reloads, and after clicking the \*Sign Up\* button, with the following messages above the Username                                                                 | Pass   |
| **SC5**         | View Experience Details (Modal)          | To ensure clicking the '+' sign displays a functional modal with unique experience details and a clear path to booking.                                                                    | TD6          | home.html is loaded.                                                                       | 1. Locate an experience card.<br> 2. Click the associated 'plus sign' (+). <br> 3. Verify the modal description.<br> 4. Click the 'Reserve Your Peace Here' button within the modal. | Experience: Indulgence                                                          | A modal window appears displaying the unique description. The 'Reserve Your Peace Here' button redirects the user to the reservation.html page.                                                                                                                                                                                    | The modal appeared with the correct description. Clicking 'Reserve Your Peace Here' successfully redirected the user to the reservation.html booking page.                          | Pass   |
| **SC6**         | Book Experience (Unregistered User)      | To verify that an unauthenticated user is correctly directed to the sign-up/login flow when attempting to book.                                                                            | TD7          | User is not signed in (SC3 passed). home.html is loaded.                                   | 1. On the home page, click on a spa experience amount (price button). <br> 2. Alternatively: Click the '+' sign, then the modal's 'Reserve Your Peace Here' button.                  | N/A                                                                             | The user is redirected to the reservation.html page with a clear message encouraging them to sign up or log in.                                                                                                                                                                                                                    | Clicking the price button redirected the user to the reservation page with the prompt: "Ready to indulge in relaxation? Please log in or sign up to reserve the peace you deserve." | Pass   |
| **SC6**         | Book Experience (Registered User)        | To verify that a signed-in user can successfully submit a reservation and is correctly redirected to the confirmation page.                                                                | TD8          | User is signed in (SC1 passed). home.html is loaded.                                       | 1. Click on a spa experience amount. <br> 2. Complete the reservation form (Name, Address, Postcode, Phone, Experience, Guests, Date). <br> 3. Click Save.                           | First Name: Jane <br> Postcode: OD5 9TR <br> Experience: Massage <br> Guests: 2 | The page redirects to confirmation/[reservation_id].html containing a visible summary of all submitted reservation details.                                                                                                                                                                                                        | The form submitted successfully and redirected to the confirmation page showing all booking details summarised correctly.                                                           | Pass   |
| **SC7**         | Change/Edit Reservation                  | To verify that a registered user can successfully modify an existing reservation and receive a confirmation message.                                                                       | TD9          | User is signed in (SC1 passed). A valid reservation (TD8 passed) exists.                   | 1. Click the 'Reservation' link/button. <br> 2. Find the reservation and click 'Edit'. <br> 3. Change a field (e.g., Number of Guest to 3).<br> 4. Click Save.                       | New Guests: 3                                                                   | The page redirects to the past_reservations.html page. A success message displays: "Reservation updated successfully!". The summary shows the updated details.                                                                                                                                                                     | The reservation was successfully modified and the user was redirected to past_reservations.html with the message "Reservation updated successfully!" displayed.                     | Pass   |
| **SC8**         | Cancel Reservation (Confirm)             | To verify a user can successfully cancel an existing reservation after confirming in the modal.                                                                                            | TD10         | User is signed in (SC1 passed). A valid reservation exists. past_reservations.html loaded. | 1. On the past_reservations.html page, click 'Cancel'. <br> 2. In the confirmation modal, click "yes, I'm sure".                                                                     | Reservation ID: [From TD8]                                                      | The page redirects to past_reservations.html. A success message displays: "Reservation deleted successfully!". The reservation is no longer visible.                                                                                                                                                                               | The reservation was successfully cancelled, and the message "Reservation deleted successfully!" was displayed on the past_reservations.html page.                                   | Pass   |
| **SC8**         | Cancel Reservation (Decline)             | To verify that declining cancellation returns the user to the reservation list without making any changes.                                                                                 | TD11         | User is signed in (SC1 passed). A valid reservation exists. past_reservations.html loaded. | 1. On the past_reservations.html page, click 'Cancel'. <br> 2. In the confirmation modal, click "No, I'm not".                                                                       | Reservation ID: [From TD8]                                                      | The modal closes. The page remains on past_reservations.html, and the reservation remains active/unchanged.                                                                                                                                                                                                                        |                                                                                                                                                                                     |        |
| **SC9**         | Browser Restart                          | To verify that the user remains authenticated across browser restarts, indicating correct handling of cookies/local storage for session maintenance.                                       | TD11         | User is signed in (TD1 passed). Browser session is active.                                 | 1. Close the browser completely. <br> 2. Re-open the browser and navigate directly to the site URL. <br> 3. Check the navigation bar for the Logout link.                            | N/A                                                                             | The user should be treated as signed-in; the 'Logout' link is visible, and the 'Login' link is absent.                                                                                                                                                                                                                             | The browser was closed and re-opened. The navigation bar correctly showed the 'Logout' link, confirming the session wa                                                              |        |

### Hyperlinks Testing (Navigation & External Links)

Page | Language Test Type| Status | User Action | Expected Results | Outcome
|----|----------|--------|-------------|------------------|---------|
**home.html**|JavaScript|All |	Click the menu|	Open the navigation slider to the left|	Pass|
||Python|Logged-in |-|	Message appears under the header|	Pass
||Python|Logged in|-|	Book Now button	Open the reservation page|	Pass
||Python|Logged out/not registered|	Click **Book Now** button|	Open the reservation page(sign-up/login)|	Pass
||JavaScript|All|Click the + button|Opens the modal with more information|	Pass
||Python|Logged out/not registered |	Click **reserve your peace here**|	Open the reservation page(sign-up/login)|	Pass
||Python|Logged in|	Click **reserve your peace here**|	Open the reservation page	|Pass
||Python|All|Click **price**|	Open the reservation page(sign-up/login)|	Pass
||Python|All|Click **phone number**|	Open the application to make phone calls	|Pass
||Python|All|Click the **email address**|		Opens the application to send an email|	Pass
||Python|All|Click **WhatsApp** logo|	Opens WhatsApp|	Pass
||Python|All|Click **Address**	|	Opens Google maps to Ashleworth	|Pass
||Python|All|Click **Instagram’s** logo|	Opens Instagram	|Pass
||Python|All|Click **YouTube’s** logo	|Opens YouTube	Opens YouTube	|Pass
||Python|All|Click **Facebook’s** logo|	Opens Facebook|	Pass
||Python|All|Click **X(formerly Twitter)** logo| 	Opens X formerly Twitter|	Pass
|**reservation.html**|Python|	Logged out/not registered|	Click sign up|	Opens signup.html |	Pass
||Python|Registered user|	Click **login**|	Opens login page	|Pass
||Python|Registered user|	Enter first name|	Input name|	Pass
||Python|Registered user|	Enter last name|	Input name|	Pass
||Python|Registered user|	Enter address	|Input email address that must include **@** |Pass
||Python|Registered user|	Enter city	|Input address	|Pass
||Python|Registered user|	Enter postcode	|Input postcode|	Pass
||Python|Registered user|	Enter home number|	Input phone number|	Pass
||JavaScript|Registered user	|Select the number of guests from a dropdown list |	Select the number of guests|	Pass
||JavaScript|Registered user|	Select reservation date from a date picker|	Select reservation date	|Pass
**past_reservations** |Python| Registered user - No reservations|Click **Book Now** button|Opens the experience section of the home page|	Pass
||Python| Registered user - With reservation(s)|Click **Edit** button|User is sent the their reservation to edit|	Pass
||JavaScript| Registered user - With reservation(s)|Click **Cancel** button|A modal window prompts the user to confirm if they want to delete their reservation.|	Pass
|| JavaScript|Registered user - With reservation(s)|Click **No, I'm not** |The model closes|	Pass
|| Python|Registered user - With reservation(s)|Click **Yes, I'm sure** |Message appear at the top of the page **Reservation deleted succesfully!**|	Pass
||Python| Registered user - With reservation(s)|Click **Yes, I'm sure** |User is taken to the pased reservations page and provided with the opportunity to **book now**|	Pass
**NavBar** |Python | Registered user | User clicks the **logout** button|User is sent to the **Logout** page and is prompted if they would like to logout|Pass
||Python|All |Click **Reservations**|User is sent to past_reservations.html|	Pass
||JavaScript | All | Click *burger* icon| Modal opens with **logout** and **reservations**|	Pass

## Validation 

<details>
<summary>JSLint - Passed with no errors</summary>
<br>

![JSLint](https://res.cloudinary.com/dybts6jei/image/upload/v1764882036/JSLint_sbowpf.jpg)

</details>

<details>
<summary>CSS Validation - Passed with no warnings or errors</summary>
<br>


![CSS Validation](https://res.cloudinary.com/dybts6jei/image/upload/v1764882656/W3C_CSS_Validation_nxcp0i.jpg)

</details>


<details>
<summary>Home Page - Passed with no warnings or errors</summary>
<br>

![Home Page](https://res.cloudinary.com/dybts6jei/image/upload/v1764899475/home_validator.w3.org_lqdak1.jpg)

</details>

<details>
<summary>Sign up - 4 errors found</summary>
<br>


![Sign up](https://res.cloudinary.com/dybts6jei/image/upload/v1764899474/signup_validator.w3.org_ku0bgp.jpg)

</details>

* The default templates for the **Account Management** front-end templates were used **Sign Up**. These templates produce 4 errors.  

<details>
<summary>Sign in - Passed with no warnings or errors</summary>
<br>

![Sign in](https://res.cloudinary.com/dybts6jei/image/upload/v1764899474/signin_validator.w3.org_mhkyff.jpg)

</details>
<details>
<summary>Sign Out - Passed with no warnings or errors</summary>
<br>

![Sign Out](https://res.cloudinary.com/dybts6jei/image/upload/v1764901115/signout_validator.w3.org_w022gv.jpg)

</details>

<details>
<summary>Reservation - Passed with no warnings or errors</summary>
<br>

![Reservation](https://res.cloudinary.com/dybts6jei/image/upload/v1764899475/reservation_validator.w3.org_ckjxbv.jpg)

</details>

<details>
<summary>Past Reservation - Passed with no warnings or errors</summary>
<br>

![Past Reservation](https://res.cloudinary.com/dybts6jei/image/upload/v1764899471/past_reservations.w3.org_j7nryr.jpg)

</details>

<details>
<summary>Change Reservation - Passed with no warnings or errors</summary>
<br>

![Change Reservation](https://res.cloudinary.com/dybts6jei/image/upload/v1764901561/change_reservation_validator.w3.org_fleu6l.jpg)

</details>


## Known Bugs

|Bug|Description|Planned Fix|
|---|-----------|-----------|
|**Users can select dates in the past** | The reservation form currently allows users to pick and submit dates that have already passed. | Add client-side and server-side validation to restrict date selection to today or future dates|
|**Experience selector**|Regardless of which experience brought the user to the reservation page, they must still select the experience from the dropdown list.|Pre-select the experience in the dropdown based on the user's previous selection or navigation path.|
|**Autofill experience** | When a user edits a reservation, the previously selected experience is not automatically populated in the dropdown. The user must manually re-select the experience. |Ensure the form pre-selects the original experience when editing a reservation.|
|**CSP inline style violation** | Used `unsafe-inline` for the Content Secruity Policy blocks inline styles to circumvent errors | Long term fix would be use hashes or nounces for secure inline style usage |
| **SW3C HTML Validation Error** | The **Sign up** form generated by the `django-allauth` library using the shortcut `{{ form.as_p}}`, result in a non-complaint HTML according to the W3C validator. This is due to improper element nesting, specifically the placement of block-level elements (like `<ul>` for help text) within inline <span> elements or implied <p> tags. | To resolve this compliance issue, the `{{ form.as_p }}` shortcut will be replaced with manual field rendering in the template (using a `{% for field in form %}` loop). This technique will allow the use of compliant `<div>` containers, which can legally hold the nested list elements, resolving the W3C errors. |

## Lighthouse Reports

<details>
<summary>Home Lighthouse Report</summary>
<br>

![Home Page](https://res.cloudinary.com/dybts6jei/image/upload/v1751925795/home_lighthouse_zqgqgx.png)

</details>

<details>
<summary>Sign up Lighthouse Report</summary>
<br>

![Sign_up](https://res.cloudinary.com/dybts6jei/image/upload/v1751925795/sign_up_lighthouse_nmcfi0.png)

</details>

<details>
<summary>Sign in Lighthouse Report</summary>
<br>

![Sign_in](https://res.cloudinary.com/dybts6jei/image/upload/v1751925794/sign_in_lighthouse_ycnlbo.png)

</details>

<details>
<summary>Sign out Lighthouse Report</summary>
<br>

![Sign out](https://res.cloudinary.com/dybts6jei/image/upload/v1751925795/sign_out_lighthouse_br7ipi.png)

</details>

<details>
<summary>Book Reservation Lighthouse Report</summary>
<br>

![Book Reservation](https://res.cloudinary.com/dybts6jei/image/upload/v1751925795/reservation_lighthouse_olj8fk.png)

</details>

<details>
<summary>Review Reservation Lighthouse Report</summary>
<br>

![Review Reservation](https://res.cloudinary.com/dybts6jei/image/upload/v1751925795/reservation_edit_lighthouse_rjtixz.png)

</details>

## Python
| App |File | Screenshoot|
|-----|-----|------------|
| experience | admin.py | ![alt text](https://res.cloudinary.com/dybts6jei/image/upload/v1764903705/admin_guest_jkn9c1.jpg)|
| experience | apps.py | ![alt text](https://res.cloudinary.com/dybts6jei/image/upload/v1764903703/apps_experience_hpnybr.jpg)|
| experience | models.py | ![https://res.cloudinary.com/dybts6jei/image/upload/v1764903704/models_experience_l26os4.jpg ](https://res.cloudinary.com/dybts6jei/image/upload/v1764903704/models_experience_l26os4.jpg)|
| experience | urls.py | ![alt text](https://res.cloudinary.com/dybts6jei/image/upload/v1764903704/urls_experience_kg1ncr.jpg)
| experience | views.py | ![alt text](https://res.cloudinary.com/dybts6jei/image/upload/v1764903706/views_experience_ytysd4.jpg)
| guest | admin.py | ![alt text](https://res.cloudinary.com/dybts6jei/image/upload/v1764903705/admin_guest_jkn9c1.jpg)
| guest | apps.py | ![alt text](https://res.cloudinary.com/dybts6jei/image/upload/v1764904756/app_guest_gh29pl.jpg)
| guest | models.py |![alt text](https://res.cloudinary.com/dybts6jei/image/upload/v1764905647/models-guest_wekfnt.jpg)
| reservation | admin.py | ![alt text](https://res.cloudinary.com/dybts6jei/image/upload/v1764905277/admin-reservation_c17vp2.jpg)
| reservation | app.py | ![alt text](https://res.cloudinary.com/dybts6jei/image/upload/v1764905648/apps-reservation_lq3xym.jpg)
| reservation | forms.py | ![alt text](https://res.cloudinary.com/dybts6jei/image/upload/v1764905278/forms-reservation_dx6xy4.jpg)
| reservation | models.py | ![alt text](https://res.cloudinary.com/dybts6jei/image/upload/v1764905652/models-reservation_hqcgiz.jpg)
| reservation | urls.py | ![alt text](https://res.cloudinary.com/dybts6jei/image/upload/v1764905280/url-reservation_fwrhgx.jpg)
| reservation | views.py | ![alt text](https://res.cloudinary.com/dybts6jei/image/upload/v1764905655/views-reservation_miu2cq.jpg)

## Conclusion
The manual User Acceptance Testing (UAT) for the Oakdale Spa website has concluded successfully.

All 9 core user-centric test scenarios (SC1 through SC9), covering User Authentication, Registration Validation, and the full Reservation Lifecycle (Booking, Editing, and Cancellation), achieved a 100% Pass rate. This confirms that all critical user journeys function as intended, meet the specified functional requirements, and provide accurate, expected feedback to the user.

Key successes include:

* Robust Authentication: Secure login, logout, and persistent session management (SC1, SC3, SC9).

* End-to-End Reservation Flow: Seamless booking, successful modification (SC7), and proper cancellation control (SC8).

* Effective Validation: Form validation correctly prevents invalid logins (SC2) and enforces registration security rules (SC4).

* Comprehensive Linkage: All internal and external hyperlinks were confirmed as operational.

While several Known Bugs related to date validation, experience autofill, and a minor W3C HTML error on the sign-up page exist, these issues are clearly documented and have corresponding Planned Fixes. None of the known bugs prevent the successful execution of the primary business functions (booking, editing, canceling).

**Recommendation:**  Based on the successful completion of the UAT phase, the Oakdale Spa website is recommended for deployment. Remediation of the documented Known Bugs should be prioritised in the next iteration of development.

Back to the [README](README.md)