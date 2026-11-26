import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from views import RenderTemplate


load_dotenv()

SLACK_APP_TOKEN = os.environ.get("SLACK_APP_TOKEN")
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET")

app = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET,
)

render_template = RenderTemplate(app.client)

daily_message = ""
bi_hourly_message = ""
channel = ""

@app.command("/setup")
def setup(ack, body, client, logger):
    ack()
    try:
        result = render_template.render(body, client)
        logger.info(result)
    except Exception as e:
        logger.error(f"Error opening modal: {e}")

@app.view("setup-modal")
def handle_submission(ack, body, view, client, logger):
    ack()
    try:
        print(f"{view["state"]["values"]}")
        daily_message = view['state']['values']['daily_inp']['daily_inp']['value']
        bi_hourly_message = view['state']['values']['bi_hourly_inp']['bi_hourly_inp']['value']
        channel = view['state']['values']['channel_inp']['channel_select']['selected_conversation']
    except Exception as e:
        logger.error(f"Error handling view submission: {e}")

# @app.action("submit_setup")
# def submit_setup(ack, body, client, logger):
#     ack()
#
#     logger.info(body)


if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()