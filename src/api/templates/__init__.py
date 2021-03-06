import os

TEMPLATE_PATH = os.path.dirname(os.path.abspath(__file__))

INVITE_SUBJECT = u"You've been invited to ElasticKube"
REQUEST_INVITE_SUBJECT = u"Invite request to ElasticKube"
RESET_PASSWORD_EMAIL_SUBJECT = u"Reset your password"

with open(os.path.join(TEMPLATE_PATH, 'invite.html')) as invite_file:
    INVITE_TEMPLATE = invite_file.read()

with open(os.path.join(TEMPLATE_PATH, 'invite_message.html')) as invite_message_file:
    INVITE_MESSSAGE_TEMPLATE = invite_message_file.read()

with open(os.path.join(TEMPLATE_PATH, 'request_invite.html')) as request_invite_file:
    REQUEST_INVITE_TEMPLATE = request_invite_file.read()

with open(os.path.join(TEMPLATE_PATH, 'reset_password_email.html')) as reset_password_email_file:
    RESET_PASSWORD_EMAIL_TEMPLATE = reset_password_email_file.read()
