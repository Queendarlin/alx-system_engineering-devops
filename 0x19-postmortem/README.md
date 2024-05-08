My First Postmortem: Website Outage Due to Database Overload
Have you ever experienced that sinking feeling when your website goes down? Yeah, us, too. Downtime can impact user trust and business operations significantly. Even brief outages can substantially impact customer trust and brand perception. Recently, our team experienced a 45-minute outage that disrupted the smooth functioning of our Customer Portal. This postmortem report details the incident, analyzes the root cause, and outlines corrective and preventative measures to prevent similar occurrences in the future. Understanding the cause of this outage and implementing the proposed actions will strengthen your development and deployment processes, ultimately fostering a more reliable website for your users.
Issue Summary
Duration:  This outage occurred on May 5th, 2024, between 1:30 PM PST and 2:15 PM PST (45 minutes).
Impact: Our website became unresponsive during this time. Users attempting to access the website encountered a "503 Service Unavailable" error message, which impacted 100% of website visitors during the outage window.
Timeline
At 1:30 PM PST, monitoring alerts were triggered due to a significant increase in database connection requests exceeding predefined thresholds. An on-call engineer immediately investigated, suspecting a traffic spike as a common cause of outages. To address this possibility, the team scaled up the web server instances at 1:32 PM PST. However, this action didn't resolve the issue, as the database load remained high. 

By 1:35 PM PST, further investigation revealed a recently deployed code change associated with the new product launch marketing campaign was causing inefficient database queries. To minimize downtime, the problematic code was identified and disabled by 1:50 PM PST, allowing the database load to return to normal levels.

By 2:00 PM PST, the website functionality was restored, and stakeholders were informed about the outage and its resolution. The focus then shifted towards a permanent fix. The development team reviewed and refactored the disabled code between 2:15 PM PST and 3:00 PM PST to optimize the database queries.

Finally, at 3:00 PM PST, the refactored code was successfully redeployed, restoring the full functionality of the marketing campaign on the website.
Root Cause and Resolution
The root cause of the outage was a recently deployed code change that resulted in inefficient database queries. These queries overloaded the database server, making it unresponsive to incoming requests. The issue was resolved by identifying and disabling the problematic code, allowing the database to recover. Subsequently, the code was refactored to optimize the queries and then redeployed.
Corrective and Preventative Measures
To prevent similar outages in the future, here are several ways:
Improved Code Review Process: You can integrate database profiling tools into the development workflow. These tools will analyze potential bottlenecks in database queries during development, allowing for early identification and correction of performance issues.
Proactive Performance Monitoring: You can implement automated load testing that simulates real-world traffic patterns. These tests will measure the impact on the database server and identify potential performance issues before the code is deployed.
Develop Database Monitoring Dashboards: You can also create more comprehensive database monitoring dashboards to provide real-time insights into server health and identify potential overload scenarios before they impact user experience. These dashboards will display critical metrics like database load, query execution times, and connection pool utilization.
Conclusion
By implementing the corrective and preventative measures outlined above, we aim to minimize the risk of future database-related outages and ensure a more stable user experience for our website visitors. This incident highlights the essence of a robust development and deployment process that incorporates performance considerations at every stage. It also emphasizes the need for collaboration and communication between development, operations, and database administration teams.
