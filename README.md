# VPN Service 🌐

VPN service with a web interface that allows users to add multiple sites and browse them securely using an internal proxy. Routing appears as `localhost/{domain_name}/{routes_on_original_site}`. Returned page content dynamically replaces link attributes for seamless navigation. Links to external resources remain the same. The dashboard includes VPN site statistics, tracking page visits, and sent/received data volumes.


## ⚙️ Installing using GitHub

Linux/MacOS:

```shell
git clone https://github.com/denys-source/vpn-service/
cd vpn-service/
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

Windows:
```shell
git clone https://github.com/denys-source/vpn-service/
cd vpn-service/
python venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 🐳 Running with docker

Docker should be installed
```shell
sudo docker-compose up --build
```

## 📍 Features

- **User Registration:** Users can register on the website, creating personal accounts.
- **Personal Dashboards:** Upon registration, users gain access to personalized dashboards for managing their information.
- **Data Editing:** Users can edit their personal data within the dashboard, enhancing customization.
- **Statistics Section:** The dashboard includes a statistics section, detailing page visits categorized by VPN-utilized sites.
- **Data Usage Tracking:** Users can monitor data volumes sent and received per site through the VPN.
- **Site Creation:** Clients can create multiple sites, each defined by a structure comprising URLs and names.
- **Secure Site Access:** After site creation, clicking "Go to Site" redirects through an internal proxy, ensuring secure browsing.
- **Dynamic Routing:** The routing structure appears as `localhost/{domain_name}/{routes_on_original_site}`.
- **Link Attribute Replacement:** Returned page content dynamically replaces link attributes, enabling seamless navigation.

## ✅ Demo

![image](https://github.com/denys-source/vpn-service/assets/72623693/433a06de-19ff-47f1-81e1-f3f9067888ff)

![image](https://github.com/denys-source/vpn-service/assets/72623693/4e4fba55-b5fc-453c-8f39-c468fc53da82)

![image](https://github.com/denys-source/vpn-service/assets/72623693/d696727c-d14f-45cd-8ee7-c26a4b57b51e)
