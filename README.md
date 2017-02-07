# Trello History Visualizer: [Website](https://jasonwarta.com/trello)
Simple webpage for playing back the history of a trello board from the activity log.

####Usage
Upload a trello activity log JSON file, set the playback speed, and click 'Load'.

**_Note:_**
I am not peforming any validation on the json object; upload invalid files at your own risk.


Unfortunately trello doesn't track labels in the activity log, so my current workaround requires adding a comment with a valid css color code to a given card. Comments disappear from the activity log when the are deleted by an admin, so this is not a good long-term solution either.