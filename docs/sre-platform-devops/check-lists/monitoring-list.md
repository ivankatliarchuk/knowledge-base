---
title: monitorin readiness lists
summary: monitoringt guidance to follow
authors: ["ivan k"]
tags: ["checklist", "architecture", "monitoring", "readiness", "alerting"]
date: 2021-03-8
source:
published: true
---

# Monitoring Check List


- [X] Logging in code

: Modern programming languages come with logging packages that allow you to add lines of text to a log file as the application is running. Taking advantage of these packages will give you a papertrail of what your application is doing as users interact with it. Smart use of logging will allow you to spot bugs in your code, diagnose incorrect behavior in your application, troubleshoot user issuers, and raise alerts when cyber-attacks occur.

- [X] Key Elements in Log Statements

: Each entry written to a log file should contain a timestamp, the log message, and an indication of where in the code the entry is being written from - in other words, the code file and line number. Depending on what type of functionality the code is handling, it is also useful to include some of the following:

    * [X] The server name if more than one server is writing to the log file.
    * [X] The URL, HTTP status code and incoming IP address if the code is handling an incoming HTTP request.
    * [X] The username if the code is being executed in response to an action by a logged-in user.
    * [X] Timing information if the code is executing a time-sensitive action.
    * [X] Diagnostic information - for instance, if any action had to re-tried, or if a component is responding slowly.
    * [X] Error messages and stack traces if an error occurs.

- [X] What Events to Log

: You should log every HTTP request and the corresponding response, being sure to include the URL, the HTTP response code, and the time taken to service the request. You should also log any significant actions performed by your web application, including:

    * [X] Input validation failures, e.g. when the code encounters unexpected parameter names or values.
    * [X] Authentication successes and failures.
    * [X] Authorization (access control) failures.
    * [X] Session management failures, e.g. when session cookies are rejected as invalid.
    * [X] Application errors and system events.
    * [X] Startup and shutdown events - including timing information!
    * [X] User events like sign-ups, password changes and account deletions.
    * [X] Administrative events, e.g. when permissions are changed by an admin.
    * [X] Calls to third-party services or APIs.
    * [X] Legal and other opt-ins, e.g. when a user accepts the terms of use.

- [X] Log Levels

: By convention, most logging packages allow you to mark logging statements with one of at least four “log levels” - typically named DEBUG, INFO, WARNING and ERROR, in order of importance. You should mark each logging statement with an appropriate log level to make it easy to filter out the noise in log files. Servers can be configured so only statements marked with a particular log level are written to the log file: a server configured with the INFO log-level will write INFO, WARNING and ERROR messages to the log file, but omit DEBUG messages.

: Low-level diagnostic events should be marked as DEBUG statements, and typically only show up in non-production environments. The INFO log level should be used for normal running: the events expected to occur when users interact with your website. Unexpected events should be logged with the WARNING level, and errors should be marked with the ERROR log level.

- [X] Make sure your team has access to these logs too when diagnosing issues.

: In addition to the logging statements added to your code, other applications in your stack will typically output log files. A web server like Apache, Nginx or IIS will log HTTP request and response information. Databases will typically write log files too, which are useful for diagnosing performance issues.

- [X] log aggregation and storage

: Logs should be centralized and stored securely so they can be viewed by administrators. “Log servers” like LogStash, Graylog, Splunk and PaperTrail will aggregate log files from different sources and allow them to be searched and analyzed in realtime. Log servers are often available as services, and can be added as plug-ins if you run on cloud-based services.

- [X] monitoring is paired with logging

: The process of continuously assessing whether your site is running as expected. Monitoring software often pulls key “metrics” from log files to diagnose the health of a web application. Let’s discuss the various ways you can monitor your application.

- [X] Uptime Monitoring is in place

: The most basic form of monitoring is checking that your site is available. “Uptime monitors” like Uptime Robot and Pingdom are free services that will check whether a URL is responding to HTTP requests successfully. (More complex or frequent checks are usually available as a paid option.) This is a simple way to achieve peace-of-mind: if your site ever becomes unavailable, the monitoring software will send an email or text alert to your team.

- [X] Error Reporting

: Capturing unexpected errors that occur on your website is key to detecting cyber-attacks and ensuring software quality. Errors conditions can either be extracted from log files, or recorded using plug-ins provided by services like Rollbar or Airbrake. Error reporting services even allow you to capture error conditions that occur in JavaScript in the browser, which typically won’t appear in server-side logs.

- [X] Performance Metrics

: Capturing performance metrics will give you granular information about the state of your web application. Your monitoring should keep track of:

- [X] Responsiveness: how long it takes to respond to each web request.
- [X] Throughput: how many requests per second are hitting your site.
- [X] Memory usage and server load: how much of each server’s memory space is being used up, and how close each server is to full capacity.
- [X] Database performance: how many queries are being run per second and how many concurrent connections there are.

---

- [X] Alerting

: You should configure your monitoring software to alert your team when unusual errors occur or when performance metrics reach critical conditions. Alerts can be sent over email, instant messaging or text. Large organizations will have support rotas, so at least one engineer is available to respond to alerts at all times.

- [X] [Response Plans](./incident-response-plan)

: Being alerted to errors is only useful if there are actions your support engineers can undertake to fix the error condition! Make sure you put together a trouble-shooting plan for a responding engineer to follow, and keep it up to date as you develop your system.

: Troubleshooting steps may consist of restarting servers, adding extra servers in times of high load, blacklisting IP addresses when you see malicious traffic, or escalating to team specialists (like network engineers and database administrators) when particular parts of the application appear to be the problem. If the issue starts to affect users, making an announcement on a status page or in a website banner will earn you goodwill.

---

- [ ] What Not to Log

: Writing sensitive information to your logs is a security risk - imagine what an attacker could do if they stole your log files! Make sure your logging statements never contain any of the following:

    * [ ] User or system passwords.
    * [ ] Encryption keys.
    * [ ] Database connection strings.
    * [ ] API keys for third-party services.
    * [ ] Personally identifiable information about users.
    * [ ] Payment information like credit card numbers.
    * [ ] Sensitive HTTP headers, such as Authorization headers.
    * [ ] Session IDs or session cookies.
    * [ ] Access tokens - for example, those used during sign-ups or password resets.
    * [ ] Information a user has opted out of collection. The “right to be forgotten” is law in many parts of the world, and this includes data in log files.
