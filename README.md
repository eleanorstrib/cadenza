# cadenza
Overview
cadenza is an application that enables users to record any value via text and retrieve those values via text or a web based dashboard.
Is is live at [mycadenza.io](https://mycadenza.io).

#### Use cases/target users
Cadenza is based on texting because it is a very accessible method available on mobile devices regardless of operating system, so it is not dependent on OS versions, updates or platforms.  Anyone on a phone with texting capabilities can use it, no app download required.

In this first version, usage is very general and could include the following
- Parents recording information about their young children, like feedings, sleep and diapers
- People recording their moods for later review to better quantify and track (changes in) feelings
- Anyone tracking food consumption or exercise

#### Features
- Sign up/in on the website
- Two factor auth using text messages
- Submit a string via text — any value
- Receive confirmation text back with date and time recorded
- Create a name for your tracker, one per user
- Pay $2/month to cover cost (Stripe API)
- Text “data” to get a list of your entries for the last 30 days
- Text “last” to get last entry with date and time
- Website secured with an SSL certificate
- Web design mobile friendly, front end built with React

#### Tech stack
- Text message: Twilio API
- Web framework: Django
- Front end: React, Materialize, HTML/CSS, JS, Jquery
- SSL: Comodo/dnsimple
- Hosting: Heroku
- Authentication: Django/Authy
- Payments: Stripe
