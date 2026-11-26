class RenderTemplate:
    def __init__(self, client):
        self.client = client

    def render(self, body, client):
        client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "setup-modal",
            "title": {"type": "plain_text", "text": "StandUp Bot"},
            "submit": {"type": "plain_text", "text": "Submit"},
            "close": {"type": "plain_text", "text": "Cancel"},
            "blocks": [
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": "Setup your event's own standup bot"},
                },
                {
                    "type": "input",
                    "block_id": "daily_inp",
                    "label": {"type": "plain_text", "text": "Custom Daily Message"},
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "daily_inp",
                        "placeholder": { "type": "plain_text", "text": "Good morning! Time for your daily check in, type a message in this thread with your updates." },
                        "multiline": True
                    }
                },
                {
                    "type": "input",
                    "block_id": "bi_hourly_inp",
                    "label": {"type": "plain_text", "text": "Custom Bi-Hourly Message"},
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "bi_hourly_inp",
                        "placeholder": { "type": "plain_text", "text": "@User1 @User2 @User3, Please do your check in." },
                        "multiline": True
                    }
                },
                {
                    "type": "input",
                    "block_id": "channel_inp",
                    "label": {"type": "plain_text", "text": "Staff Channel"},
                    "element": {
                        "type": "conversations_select",
                        "action_id": "channel_select",
                        "placeholder": { "type": "plain_text", "text": "Select Channel" },
                        "filter": {"include": ["public", "private"]},
                    }
                }
            ]
        }
    )