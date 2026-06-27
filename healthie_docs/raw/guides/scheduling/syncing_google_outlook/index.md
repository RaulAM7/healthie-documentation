---
title: Syncing with Google/Outlook | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/scheduling/syncing_google_outlook/index
  md: https://docs.gethealthie.com/guides/scheduling/syncing_google_outlook/index.md
---

# Syncing with Google/Outlook

Healthie supports a 2-way calendar sync with Google Calendar and Outlook, as well as a 1-way ICS calendar feed (to be used with iCal).

You can read information about the capabilities [here](https://help.gethealthie.com/article/146-sync-healthie-with-ical-google-and-outlook-calendars)

To enable Google/Outlook sync, the provider will need to authorize the sync via OAuth. By default, Healthie has its own verified OAuth apps with both Google and Outlook. Due to the nature of OAuth, utilizing those will ask the provider if they want to allow “Healthie” access to their calendar data, and redirect them back to a Healthie-controlled URL.

Here are the scopes that our OAuth apps request

| Service         | Scopes                                                                                    |
| --------------- | ----------------------------------------------------------------------------------------- |
| Google Calendar | ”email”, “calendar”, “userinfo.profile”                                                   |
| Outlook         | ’openid’, ‘email’, ‘offline\_access’, ‘<https://graph.microsoft.com/Calendars.ReadWrite>’ |

If you want to brand the OAuth connection (or have more direct control), you have a couple of options. Both involve your company creating and maintaing OAuth apps with Google Calendar and/or Outlook. You create the application, and provide Healthie with a Client ID and Secret for your apps.

For either option, our support team needs to make configuration changes to your account. Please reach out to us if you’d like to do either of the options.

### 1) Healthie-controlled redirect flow (Full Web Whitelabel Required)

If you have a full web whitelabel, Healthie can replace the links to our authorized OAuth apps with yours. Your users will be able to follow the same steps mentioned in the help article above to connect. However, they will be taken to authorize your OAuth app, and then be redirected back to your whitelabeled URL after. Healthie maintains the sync from there, and no development work is needed on your end.

### 2) Via the API (You handle the redirect/authorization flow)

If you do not have a full web whitelabel, or want to handle the connection without sending users to the (branded or otherwise) Healthie platform, you can use the API.

You handle the OAuth authorization flow and redirection yourself, fully outside of Healthie. Once you have the user’s authorize and refresh tokens, you can then make an API call to Healthie to store their calendar sync information. We then maintain the sync from there.
