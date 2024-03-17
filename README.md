# <p align='center'>Email Campaign Manager</p>
<p align='center'>:made by d33pster:</p>
<p align='center'>
    <a href=='#Design'>Design</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='#Usage'>Usage</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='#Features'>Features</a>
</p>

#### About
This project was made during the Fix Factory Make-a-thon conducted by VIT Chennai during the month of March in 2024 specifically for M.Tech and MCA branches.

#### Problem Statement
###### <p align='center'>Hackathon Challenge</p>
Streamline Agency Email Marketting with a Centralized Platform <br>
We, Wikiprospects, are a high-growth marketing agency with 50 users managing our daily email workflow mannually. We lack a unified platform for organizing lists, designing campaigns, and tracking performance, leading to inefficiencies and inconsistencies.<br>
We're looking for your “Super intelligent” team to build the solution:
###### <p align='center'>Unified Dashboard</p>
Design a user-friendly dashboard for managing all email marketing activities, including contact lists, campaign creation, scheduling, and performance tracking with user and admin access.
###### <p align='center'>Flexible Integrations</p>
Develop seamless integrations with our existing Email Service Providers (SendGrid, Mailchimp, etc) via API connections. With flexibility for IMAP/POP for all the ISP (Yahoo, Gmail ,AOL , Microsoft, etc) future integrations is crucial.
###### <p align='center'>Advanced List Management</p>
Allow effortless segmentation, tagging, and suppression of email lists based on demographics, behavior, and opt-in/out preferences.
###### <p align='center'>Campaign Workflow Automation</p>
Implement tools for automated follow-up sequences, drag-and-drop email design, and template building.
###### <p align='center'>In-depth Analytics</p>
Build comprehensive reporting dashboards that track opens, clicks, conversions, and other key metrics across all campaigns and ESPs.
###### <p align='center'>Collaborative Features</p>
Integrate internal communication tools such as chat or annotations for better team collaboration on email campaigns.
###### <p align='center'>Success Metrics</p>
- Increased efficiency and campaign consistency.
- Improved email deliverability and engagement rates.
- Reduced manual effort and streamedlined workflow.
- Enhanced data visibility and actionable insights.
- Flexible and robust platform that adapts to our evolving needs.
###### <p align='center'>Focus for your Hackathon Team</p>
- Design an intuitive and user-friendly interface for managing all email marketing tasks.
- Craft seamless integrations with popular ESP APIs like Mailchimp, SendGrid, Constant Contact, etc. 
- Develop insightful reports and analytics dashboards with real-time data visualization.
- Ensure scalability and security for handling large volumes of data and email activities.
<br>
By building this centralized email marketing platform, you can empower us to achieve our marketing goals with greater efficiency, collaboration, and data-driven decision-making. We're excited to see your innovative solutions during the hackathon!

###### <p align='center'>Important Note</p>
We are not looking for the team to build the email sending technology itself. The focus is on creating a platform that integrates with existing ESPs and other email tools through API connections and simplifies workflow management for our agency.

#### Design
###### <p align='center'>Tabs</p>
<p id="ctab"><img src='images/_campaigns_tab_.png'></p>
<p id="mtab"><img src='images/_mailinglist_tab_.png'></p>
<p id="stab"><img src='images/_schedule_tab_.png'></p>
<p id="chat1"><img src='images/team_chat_register.png'></p>
<p id="chat2"><img src='images/team_chat_login.png'></p>

###### <p align='center'>Steps</p>

1. Add Campaign  [<a href='#ctab'>Campaign Tab</a>]
2. Add Mailing List  [<a href="#mtab">Mailing List Tab</a>]
3. Schedule the campaign  [<a href="#stab">Schedule Tab</a>]
4. Enter the mailchimp API and Sever-info(last part of api; example: us8, us1) when asked by popup

###### <p align='center'>How to Run</p>

```console
## for unix/Linux based systems

## in the terminal run:
$ chmod a+x ./main.py
$ ./main.py

## if you want to simulate team chat, open two more terminal

## in the second terminal, run:
$ chmod a+x ./server.py; ./server.py

## in the third terminal run:
$ ./main.py
```
- Minimize all the terminals.
- In the two instances of the app that is opened, go to team chat tab [<a href='#chat1'>Team Chat Tab</a>] and register as a user.<br>
ps. registering will log u in
- type and send a message.
- Repeat with the other instance.