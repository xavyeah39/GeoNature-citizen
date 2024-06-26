import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Optional

from flask import current_app
from itsdangerous import URLSafeTimedSerializer

default_mail_from_addr = current_app.config["MAIL"]["MAIL_AUTH_LOGIN"]


def send_user_email(
    subject: str,
    to: str,
    from_addr: str = default_mail_from_addr,
    plain_message: Optional[str] = None,
    html_message: Optional[str] = None,
):
    """User mail sending"""
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to

    if plain_message:
        plain_msg = MIMEText(
            plain_message,
            "html",
        )
        msg.attach(plain_msg)

    if html_message:
        html_msg = MIMEText(
            html_message,
            "html",
        )
        msg.attach(html_msg)

    try:
        if current_app.config["MAIL"]["MAIL_USE_SSL"]:
            server = smtplib.SMTP_SSL(
                current_app.config["MAIL"]["MAIL_HOST"],
                int(current_app.config["MAIL"]["MAIL_PORT"]),
            )
        else:
            server = smtplib.SMTP(
                current_app.config["MAIL"]["MAIL_HOST"],
                int(current_app.config["MAIL"]["MAIL_PORT"]),
            )

        server.ehlo()
        if current_app.config["MAIL"]["MAIL_STARTTLS"]:
            server.starttls()
        if current_app.config["MAIL"]["MAIL_AUTH_LOGIN"]:
            server.login(
                str(current_app.config["MAIL"]["MAIL_AUTH_LOGIN"]),
                str(current_app.config["MAIL"]["MAIL_AUTH_PASSWD"]),
            )
        server.sendmail(
            from_addr,
            to,
            msg.as_string(),
        )
        server.quit()

    except Exception as e:
        current_app.logger.warning("send email failled. %s", str(e))
        return {"message": """ send email failled: "{}".""".format(str(e))}


def confirm_user_email(newuser, with_confirm_link=True):
    token = generate_confirmation_token(newuser.email)
    subject = f"[{current_app.config['appName']}] {current_app.config['CONFIRM_EMAIL']['SUBJECT']}"
    to = newuser.email

    # Check URL_APPLICATION:
    url_application = current_app.config["URL_APPLICATION"]
    if url_application[-1] == "/":
        url_application = url_application
    else:
        url_application = url_application + "/"
    activate_url = url_application + "confirmEmail/" + token

    # Record the MIME  text/html.
    template = current_app.config["CONFIRM_EMAIL"]["HTML_TEMPLATE"]
    if not with_confirm_link:
        template = current_app.config["CONFIRM_EMAIL"]["NO_VALIDATION_HTML_TEMPLATE"]
    from_addr = current_app.config["CONFIRM_EMAIL"]["FROM"]
    try:
        send_user_email(
            subject,
            to,
            from_addr,
            html_message=template.format(
                activate_url=activate_url,
                app_url=current_app.config["URL_APPLICATION"],
                app_name=current_app.config["appName"],
            ),
        )

    except Exception as e:
        current_app.logger.warning("send confirm_email failled. %s", str(e))
        return {"message": """ send confirm_email failled: "{}".""".format(str(e))}


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
    return serializer.dumps(email, salt=current_app.config["CONFIRM_MAIL_SALT"])


def confirm_token(token):
    serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
    try:
        email = serializer.loads(
            token,
            salt=current_app.config["CONFIRM_MAIL_SALT"],
        )
    except Exception as e:
        current_app.logger.warning("confirm_token failled. %s", str(e))
    return email
