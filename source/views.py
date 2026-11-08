class RenderTemplate:
    def __init__(self, client):
        self.client = client

    def render(self, body, client):
        client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "view_1",
            "title": {"type": "plain_text", "text": "StandUp Bot"},
            "submit": {"type": "plain_text", "text": "Submit"},
            "blocks": [
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": "Setup your event's own standup bot!"},
                },
                {
                    "type": "input",
                    "block_id": "daily_inp",
                    "label": {"type": "plain_text", "text": "Custom Daily Message"},
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "dreamy_input",
                        "multiline": True
                    }
                },
                {
                    "type": "input",
                    "block_id": "bi_hourly_inp",
                    "label": {"type": "plain_text", "text": "Custom Bi-Hourly Message"},
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "dreamy_input",
                        "multiline": True
                    }
                },
                {
                    "type": "section",
                    "block_id": "section678",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Select Standup Channel"
                    },
                    "accessory": {
                        "action_id": "text1234",
                        "type": "multi_static_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select Channel"
                        },
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "*this is plain_text text*"
                                },
                                "value": "value-0"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "*this is plain_text text*"
                                },
                                "value": "value-1"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "*this is plain_text text*"
                                },
                                "value": "value-2"
                            }
                        ]
                    }
                }
            ]
        }
    )